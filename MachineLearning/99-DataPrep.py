# Databricks notebook source
# MAGIC %md
# MAGIC # Creating a TFRecords file on Azure Databricks
# MAGIC This notebook demonstrates how to create a TFRecords file from a Spark dataframe using `spark-tensorflow-connector` library.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Download and extract images

# COMMAND ----------

# MAGIC %sh
# MAGIC wget https://azureailabs.blob.core.windows.net/aerialsmall/aerialsmall.tar.gz
# MAGIC tar -xzf aerialsmall.tar.gz &> /dev/null
# MAGIC ls /databricks/driver/aerialsmall

# COMMAND ----------

# MAGIC %md
# MAGIC ## Copy images to DBFS

# COMMAND ----------

img_dir = '/datasets/aerialsmall/'

dbutils.fs.mkdirs(img_dir)
dbutils.fs.cp('file:/databricks/driver/aerialsmall/train', img_dir + '/train', recurse=True)
dbutils.fs.cp('file:/databricks/driver/aerialsmall/test', img_dir + '/test', recurse=True)
display(dbutils.fs.ls(img_dir))

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Load training images to a dataframe

# COMMAND ----------

from pyspark.ml.image import ImageSchema
from pyspark.sql.functions import lit

# Read training images to a dataframe
train_img_dir = '/datasets/aerialsmall/train'

image_df = ImageSchema.readImages(train_img_dir, recursive=True)

# COMMAND ----------

from pyspark.sql.functions import regexp_extract, col

image_labeled = image_df.withColumn('label', regexp_extract(col('image.origin'), '(.)(train/)(\w+)', 3))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load validation images to a dataframe

# COMMAND ----------

image_labeled.show()

# COMMAND ----------

image_df.printSchema()

# COMMAND ----------

