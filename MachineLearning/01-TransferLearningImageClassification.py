# Databricks notebook source
# MAGIC %sh 
# MAGIC curl -O https://azureailabs.blob.core.windows.net/aerial/aerial.tar.gz
# MAGIC tar xzf aerial.tar.gz &>/dev/null

# COMMAND ----------

dbutils.fs.ls('file:/databricks/driver/aerial/')

# COMMAND ----------

#img_dir = '/datasets/aerial'
#dbutils.fs.mkdirs(img_dir)

#dbutils.fs.cp('file:/databricks/driver/aerial/test', img_dir + "/test", recurse=True)
#dbutils.fs.cp('file:/databricks/driver/aerial/train', img_dir + "/train", recurse=True)


# COMMAND ----------

images_per_class = 1000
source_image_dir = 'file:/databricks/driver/aerial/'
dest_image_dir = '/datasets/aerialsmall/'
labels = [file.name for file in dbutils.fs.ls(source_image_dir + 'train')]
files = []
for dataset in ['train/', 'test/']:
  for label in labels:
    for file in dbutils.fs.ls(source_image_dir + dataset + label)[0:images_per_class]:
      dbutils.fs.cp(file.path, dest_image_dir + label + file.name)
    



# COMMAND ----------

dbutils.fs.rm('/datasets/aerialsmall', recurse=True)

# COMMAND ----------

dbutils.fs.ls('/datasets/aerialsmall')

# COMMAND ----------

