# Databricks notebook source
# MAGIC %md
# MAGIC # Transfer Learning with Deep Learning Pipelines
# MAGIC 
# MAGIC Deep Learning  Pipelines is a new library in Azure Databricks that provides **high-level APIs** for scalable deep learning in Python with Apache Spark.
# MAGIC 
# MAGIC The library provides easy to use interfaces for:
# MAGIC 
# MAGIC Working with image data:
# MAGIC * **Loading images** natively in Spark DataFrames
# MAGIC * **Transfer learning**, a super quick way to leverage deep learning
# MAGIC * **Distributed hyperparameter tuning** via Spark MLlib Pipelines
# MAGIC * **Applying deep learning models at scale** to images, using your own or known popular models, to make predictions or transform them into features
# MAGIC 
# MAGIC Working with general tensors:
# MAGIC * **Applying deep learning models at scale** to tensors of up to 2 dimensions
# MAGIC 
# MAGIC Deploying Models in SQL:
# MAGIC * **Deploying models as SQL functions** to empower everyone by making deep learning available in SQL
# MAGIC 
# MAGIC In this lab we will focus on **Transfer Learning**.
# MAGIC 
# MAGIC Transfer learning is one of the fastest (code and run-time-wise) ways to start using deep learning. In a summary, transfer learning  is a machine learning technique that allows to reuse knowledge gained while solving one problem to a different but related problem. For example, knowledge gained while learning to recognize cars could apply when trying to recognize trucks. Transfer Learning makes it feasible to train very effective ML models on relatively small training data sets.
# MAGIC 
# MAGIC In this lab, your will use Transfer Learing to train a custom image classification model. You use a deep neural network pre-trained on a general computer vision domain (*imagenet* dataset) and specialize it to classify the type of land shown in aerial images of 224-meter x 224-meter plots. 
# MAGIC 
# MAGIC Land use classification models can be used to track urbanization, deforestation, loss of wetlands, and other major environmental trends using periodically collected aerial imagery. The images used in this lab are based on imagery from the U.S. National Land Cover Database. U.S. National Land Cover Database defines six primary classes of land use: *Developed*, *Barren*, *Forested*, *Grassland*, *Shrub*, *Cultivated*.  Example images in each land use class are shown here:
# MAGIC 
# MAGIC Developed | Cultivated | Barren
# MAGIC --------- | ------ | ----------
# MAGIC ![Developed](https://github.com/jakazmie/AIDays/raw/master/MachineLearning/01-AzureDatabricks-DeepLearningPipelines/images/developed1.png) | ![Cultivated](https://github.com/jakazmie/AIDays/raw/master/MachineLearning/01-AzureDatabricks-DeepLearningPipelines/images/cultivated1.png) | ![Barren](https://github.com/jakazmie/AIDays/raw/master/MachineLearning/01-AzureDatabricks-DeepLearningPipelines/images/barren1.png)
# MAGIC 
# MAGIC  
# MAGIC Forested | Grassland | Shrub
# MAGIC -------- | --------- | -----
# MAGIC ![Forested](https://github.com/jakazmie/AIDays/raw/master/MachineLearning/01-AzureDatabricks-DeepLearningPipelines/images/forest1.png) | ![Grassland](https://github.com/jakazmie/AIDays/raw/master/MachineLearning/01-AzureDatabricks-DeepLearningPipelines/images/grassland1.png) | ![Shrub](https://github.com/jakazmie/AIDays/raw/master/MachineLearning/01-AzureDatabricks-DeepLearningPipelines/images/shrub1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Collect and prepare data 

# COMMAND ----------

# MAGIC %md
# MAGIC ### Download and extract images
# MAGIC The images used for training and validation of the model can be downloaded from a public Azure Blob Storage container. The dataset contains 6000 labeled images - 1000 images per land class.

# COMMAND ----------

# MAGIC %sh
# MAGIC wget https://azureailabs.blob.core.windows.net/aerialtar/aerialmed.tar.gz
# MAGIC tar -xzf aerialmed.tar.gz &> /dev/null
# MAGIC ls /databricks/driver/aerialmed

# COMMAND ----------

# MAGIC %md
# MAGIC ### Copy images to DBFS
# MAGIC 
# MAGIC The previous commands extracted the images to the local storage on a driver node. You need to move them to Azure Databricks DBFS

# COMMAND ----------


img_dir = '/datasets/aerial/'

dbutils.fs.mkdirs(img_dir)
dbutils.fs.cp('file:/databricks/driver/aerialmed/train/', img_dir + 'train', recurse=True)
dbutils.fs.cp('file:/databricks/driver/aerialmed/test/', img_dir + 'test', recurse=True)
display(dbutils.fs.ls(img_dir))

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Prepare training and validation dataframes
# MAGIC 
# MAGIC Deep Learning Pipelines require training and validation datasets to be in Spark data frames with a specific schema. The below code loads 6000 training images to a data frame. It than adds a new `label` column which annotates an image with a type of land it depicts. The  label is extracted from a pathname of an image.

# COMMAND ----------

# MAGIC %md
# MAGIC #### Load training images to a dataframe

# COMMAND ----------

from pyspark.ml.image import ImageSchema
from pyspark.sql.functions import lit

img_df = ImageSchema.readImages(img_dir + 'train', recursive=True)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Add the labels and split into training and validation datasets.

# COMMAND ----------

from pyspark.sql.functions import regexp_extract, col
from pyspark.ml.feature import StringIndexer

# Add a label columns
img_labeled = img_df.withColumn('label', regexp_extract(col('image.origin'), '(.)(train/)(\w+)', 3))
# Split a dataframe into training and validation dataframes
img_train, img_validate = img_labeled.randomSplit([0.7, 0.3])
# Repartition the data frames to enable better parallelization 
img_train = img_train.repartition(64).cache()
img_validate = img_validate.repartition(64).cache()

display(img_train.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Train and evaluate model 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Prepare a training pipeline

# COMMAND ----------

from pyspark.ml import Pipeline
from sparkdl import DeepImageFeaturizer 
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import IndexToString, StringIndexer

# Create a label indexer that will convert string labels to numeric.
labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(img_validate)

# Create a featurizer based on a pretrained ResNet50 DNN
featurizer = DeepImageFeaturizer(inputCol="image", outputCol="features", modelName="ResNet50")

# Create a RandomForest model
classifier = LogisticRegression(labelCol="indexedLabel", featuresCol="features", maxIter=500, regParam=0.06, elasticNetParam=0.06)

# Create a converter that will convert numeric labels back to original labels
labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel",
                               labels=labelIndexer.labels)

# Chain the components into a pipeline
pipeline = Pipeline(stages=[labelIndexer, featurizer, classifier, labelConverter])


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Train the model

# COMMAND ----------

model = pipeline.fit(img_train)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Evaluate the model
# MAGIC 
# MAGIC Calculate the model's `accuracy`  on a validation data set

# COMMAND ----------

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

validated_df = model.transform(img_validate)
evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
print("Test set accuracy = " + str(evaluator.evaluate(validated_df.select("prediction", "indexedLabel"))))
                                                                          


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Show some of the images the model failed to classify.

# COMMAND ----------

misclassified_df = validated_df.select('image', 'label', 'predictedLabel').filter(col('label') != col('predictedLabel')).limit(10)
display(misclassified_df)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Operationalize and manage

# COMMAND ----------

model.stages

# COMMAND ----------

# MAGIC %md
# MAGIC Remove StringIndexer and DeepImageFeaturizer

# COMMAND ----------

save_model = model.copy()
save_model.stages.pop(0)
save_model.stages.pop(0)
save_model.stages

# COMMAND ----------

save_model_path = '/models/landclassifier'
save_model.write().overwrite().save(model_path)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Load the model and insert DeepImageFeaturizer stage

# COMMAND ----------

from pyspark.ml import PipelineModel

landclassifier = PipelineModel.read().load(save_model_path)
featurizer = DeepImageFeaturizer(inputCol="image", outputCol="features", modelName="ResNet50")
landclassifier.stages.insert(0, featurizer)
landclassifier.stages

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC You can use the model as a regular transformer

# COMMAND ----------

