# Databricks notebook source
# MAGIC %md
# MAGIC # Transfer Learning with Deep Learning Pipelines

# COMMAND ----------

# dbutils.fs.rm('/datasets/aerialsmall', recurse=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data preparation

# COMMAND ----------

# MAGIC %md
# MAGIC ### Download and extract images

# COMMAND ----------

# MAGIC %sh
# MAGIC # wget https://azureailabs.blob.core.windows.net/aerialtar/aerialsmall.tar.gz
# MAGIC # tar -xzf aerialsmall.tar.gz &> /dev/null
# MAGIC ls /databricks/driver/aerialsmall

# COMMAND ----------

# MAGIC %md
# MAGIC ### Copy images to DBFS

# COMMAND ----------


img_dir = '/datasets/aerialsmall/'

# dbutils.fs.mkdirs(img_dir)
# dbutils.fs.cp('file:/databricks/driver/aerialsmall/', img_dir + '/', recurse=True)
display(dbutils.fs.ls(img_dir))

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Prepare training and validation dataframes

# COMMAND ----------

# MAGIC %md
# MAGIC #### Load images to a dataframe

# COMMAND ----------

from pyspark.ml.image import ImageSchema
from pyspark.sql.functions import lit

img_df = ImageSchema.readImages(img_dir, recursive=True)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Add the labels and split into training and validation datasets.

# COMMAND ----------

from pyspark.sql.functions import regexp_extract, col
from pyspark.ml.feature import StringIndexer

img_labeled = img_df.withColumn('label', regexp_extract(col('image.origin'), '(.)(aerialsmall/)(\w+)', 3))
img_train, img_validate = img_labeled.randomSplit([0.7, 0.3])
img_train = img_train.repartition(64).cache()
img_validate = img_validate.repartition(64).cache()
img_train.printSchema()
img_train.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Train and Evaluate the image classifier

# COMMAND ----------

# MAGIC %md
# MAGIC #### Prepare a training pipeline

# COMMAND ----------

from pyspark.ml import Pipeline
from sparkdl import DeepImageFeaturizer 
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer



# Create a label indexer that will convert string labels to numeric.
labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(img_validate)

# Create a featurizer based on a pretrained InceptionV3 DNN
featurizer = DeepImageFeaturizer(inputCol="image", outputCol="features", modelName="ResNet50")

# Create a RandomForest model
classifier = RandomForestClassifier(labelCol="indexedLabel", featuresCol="features", numTrees=100, maxDepth=30)

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

# COMMAND ----------

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

validated_df = model.transform(img_validate)
evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
print("Test set accuracy = " + str(evaluator.evaluate(validated_df.select("prediction", "indexedLabel"))))
                                                                          


# COMMAND ----------

