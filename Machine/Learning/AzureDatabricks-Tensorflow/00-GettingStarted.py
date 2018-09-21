# Databricks notebook source
# MAGIC %md
# MAGIC # TensorFlow on Azure Databricks 
# MAGIC This is a set of labs that demonstrate how to use Azure Databricks to develop deep learning models using Tensorflow. The labs cover the following scenarios:
# MAGIC 
# MAGIC 1. Using Tensorflow on a single (driver) node
# MAGIC 2. Distributed training with Horovod
# MAGIC 3. Distributed training with TensorFlowOnSpark
# MAGIC 
# MAGIC All labs tackle the same scenario:
# MAGIC 
# MAGIC You will train a custom image classification model to automatically classify the type of land shown in aerial images of 224-meter x 224-meter plots. Land use classification models can be used to track urbanization, deforestation, loss of wetlands, and other major environmental trends using periodically collected aerial imagery. The images used in this lab are based on imagery from the U.S. National Land Cover Database. U.S. National Land Cover Database defines six primary classes of land use: *Developed*, *Barren*, *Forested*, *Grassland*, *Shrub*, *Cultivated*.  Example images in each land use class are shown here:
# MAGIC 
# MAGIC Developed | Cultivated | Barren
# MAGIC --------- | ------ | ----------
# MAGIC ![Developed](https://github.com/jakazmie/AIDays/raw/master/images/developed1.png) | ![Cultivated](https://github.com/jakazmie/AIDays/raw/master/images/cultivated1.png) | ![Barren](https://github.com/jakazmie/AIDays/raw/master/images/barren1.png)
# MAGIC 
# MAGIC 
# MAGIC Forested | Grassland | Shrub
# MAGIC -------- | --------- | -----
# MAGIC ![Forested](https://github.com/jakazmie/AIDays/raw/master/images/forest1.png) | ![Grassland](https://github.com/jakazmie/AIDays/raw/master/images/herbaceous.png) | ![Shrub](https://github.com/jakazmie/AIDays/raw/master/images/shrub1.png)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## GPU Cluster setup
# MAGIC You will need a GPU cluster to complete the labs. To start, provision a 2 node cluster - a driver and one worker node. Use **Standard_NC12 (beta)** node type for both nodes and  **4.1 ML Beta** runtime.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Prepare data
# MAGIC 
# MAGIC The training and validation data sets have been pre-processed into Tensorflow TFRecords format. The training file contains 6000 images and the validation files contains 1800 images. The files are in the public container in Azure Blob storage.
# MAGIC 
# MAGIC ### Download the training and validation files

# COMMAND ----------

# MAGIC %sh 
# MAGIC curl -O https://azureailabs.blob.core.windows.net/aerialsmall/aerialsmall_train.tfrecord
# MAGIC curl -O https://azureailabs.blob.core.windows.net/aerialsmall/aerialsmall_validate.tfrecord

# COMMAND ----------

dbutils.fs.ls('file:/databricks/driver/')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Copy the files to DBFS
# MAGIC The files have been downloaded to the driver's local file system. You can use the local file system for the first lab - single node training. Just remember  that this is not durable storage and will be destroyed when the cluster terminates. For the distributed training labs you need to move the files into DBFS.

# COMMAND ----------

tfrecords_dir = '/datasets/aerialsmall_tfrecords'
# dbutils.fs.mkdirs(tfrecords_dir)
# butils.fs.cp('file:/databricks/driver/aerialsmall_train.tfrecord', tfrecords_dir)
# dbutils.fs.cp('file:/databricks/driver/aerialsmall_validate.tfrecord', tfrecords_dir)
dbutils.fs.ls(tfrecords_dir)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Next steps
# MAGIC 
# MAGIC You are now ready to start the labs. The labs are interdependent so you can execute them in an arbitrary sequence:
# MAGIC 1. `01-SingleNode.py` - Use TensorFlow on a single (driver) node
# MAGIC 2. `02-Horovod.py` - Distributed training with Horovod
# MAGIC 3. `03-TensorFlowOnSpark.py` - Distributed training with TensorFlowOnSpark

# COMMAND ----------

