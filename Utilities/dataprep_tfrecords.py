# Databricks notebook source
# MAGIC %md
# MAGIC # Creating a TFRecords file using a driver node

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
# MAGIC ## Display sample images

# COMMAND ----------

import os
import matplotlib.pyplot as plt
from PIL import Image
 

img_dir = '/dbfs/datasets/aerialsmall/train' 

images = [(folder, os.listdir(os.path.join(img_dir, folder))[0])  for folder in os.listdir(img_dir)]
labels, paths = zip(*images)

figsize = (10, 7)
fig, axis = plt.subplots(len(images)//3, 3, figsize=figsize)
fig.tight_layout()
for ax, label, path in zip(axis.flat[0:], labels, paths):
  image_data = Image.open(os.path.join(img_dir, label, path))
  ax.set_title(label)
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  ax.imshow(image_data)

display(fig)


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Creatw training and validation TFRecord files

# COMMAND ----------

import numpy as np
import tensorflow as tf
from PIL import Image


    
def images_to_tfrecord(img_dir, outputfile): 
  
    def _int64_feature(value):
        return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

    def _bytes_feature(value):
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

    labels = {'Barren': 0,
          'Cultivated': 1,
          'Developed': 2,
          'Forest': 3,
          'Herbaceous': 4,
          'Shrub': 5}
    
    images = [ (labels[folder], os.path.join(img_dir, folder, path)) for folder in os.listdir(img_dir) for path in os.listdir(os.path.join(img_dir, folder))]
    
    i = 0
    with tf.python_io.TFRecordWriter(outputfile) as writer:
        for label, path in images:
            im = np.array(Image.open(path))
            example= tf.train.Example(
                features = tf.train.Features(
                    feature = {
                        'image': _bytes_feature(im.tostring()),
                        'label': _int64_feature(label)
                    }))
            writer.write(example.SerializeToString())
            i += 1
            if i%100 == 0:
              print('Wrote {0} records'.format(i))
    
    
        

# COMMAND ----------

#dbutils.fs.rm('/datasets/aerialsmall/aerial_test.tfrecord')

# COMMAND ----------

img_dir = '/dbfs/datasets/aerialsmall/' 
output_dir = '/dbfs/datasets/aerialsmall/'

for data in ['train', 'test']:
  images_to_tfrecord(os.path.join(img_dir, data), os.path.join(output_dir, 'aerialsmall_' + data + '.tfrecord'))

# COMMAND ----------

dbutils.fs.ls('/datasets/aerialsmall/aerialsmall_train.tfrecord')

# COMMAND ----------

import os
import tensorflow as tf

def _parse(example_proto):
  IMAGE_SHAPE = (224, 224, 3,)
  
  def scale_image(image):
    image = image / 127.5
    image = image - 1.
    return image
  
  features = {'label': tf.FixedLenFeature((), tf.int64, default_value=0),
              'image': tf.FixedLenFeature((), tf.string, default_value="")}
  
  parsed_features = tf.parse_single_example(example_proto, features)
  label = parsed_features['label']
  image = image = tf.decode_raw(parsed_features['image'], tf.uint8)
  image = tf.cast(image, tf.float32)
  #image = scale_image(image)
  image = tf.reshape(image, IMAGE_SHAPE)
  
  return label, image
  
                                         


# COMMAND ----------


filenames = ['/dbfs/datasets/aerialsmall/aerialsmall_train.tfrecord']

dataset = tf.data.TFRecordDataset(filenames)
dataset = dataset.map(_parse)

iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()
with tf.Session() as sess:
  value = sess.run(next_element)
  print(value)


# COMMAND ----------

fig, ax = plt.subplots()

ax.imshow(value[1]/255)

display(fig)

# COMMAND ----------

accountname = "azureailabs"
container = "aerialsmall"
folder = ""
mount_point = "/mnt/aerialsm"
accountkey = "k0sEc3OL07/c5Gy5L4LS4bPrvczX8Smktn2GGpISa9iQ4CGdPRvPQXZ71ZbAg5K3YCXpBJnk1kV/+ZahmO2KCA=="
fullname = "fs.azure.account.key." + accountname + ".blob.core.windows.net"
accountsource = "wasbs://" + container + "@" + accountname + ".blob.core.windows.net/" + folder

dbutils.fs.mount(
  source = accountsource,
  mount_point = mount_point,
  extra_configs = {fullname: accountkey})


# COMMAND ----------

dbutils.fs.ls('/mnt/aerialsm')

# COMMAND ----------

dbutils.fs.ls('/datasets/aerialsmall')

# COMMAND ----------

dbutils.fs.cp('/datasets/aerialsmall/aerialsmall_train.tfrecord', '/mnt/aerialsm/aerialsmall_train.tfrecord')

# COMMAND ----------

