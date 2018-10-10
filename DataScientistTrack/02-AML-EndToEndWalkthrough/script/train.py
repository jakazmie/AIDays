
import os
import tensorflow as tf
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import to_categorical

import numpy as np
import random
    
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, Flatten, Input
from tensorflow.keras.regularizers import l1_l2

from azureml.core import Run



# This is a generator that yields batches of preprocessed images
class ImageGenerator(tf.keras.utils.Sequence):    
    
    def __init__(self, img_dir, preprocess_fn=None, batch_size=64):
        
        # Create the dictionary that maps class names into numeric labels 
        folders = os.listdir(img_dir)
        folders.sort()
        indexes = range(len(folders))
        label_map = {key: value for (key, value) in zip(folders, indexes)}
        self.num_classes = len(label_map)
        
        # Create a list of all images in a root folder with associated numeric labels
        labeled_image_list = [(os.path.join(img_dir, folder, image), label_map[folder]) 
                              for folder in folders 
                              for image in os.listdir(os.path.join(img_dir, folder))
                              ]
        # Shuffle the list
        random.shuffle(labeled_image_list)
        # Set image list and associated label list
        self.image_list, self.label_list = zip(*labeled_image_list) 
        # Set batch size
        self.batch_size = batch_size
       
        # Set the pre-processing function passed as a parameter
        self.preprocess_fn = preprocess_fn
        
        # Set number of batches
        self.n_batches = len(self.image_list) // self.batch_size
        if len(self.image_list) % self.batch_size > 0:
            self.n_batches += 1
            
    def __len__(self):
        
        return self.n_batches
    
    def __getitem__(self, index):
        pathnames = self.image_list[index*self.batch_size:(index+1)*self.batch_size]
        images = self.__load_images(pathnames)
        
        return images
    
    # Load a set of images passed as a parameter into a NumPy array
    def __load_images(self, pathnames):
        images = []
        for pathname in pathnames:
            img = image.load_img(pathname, target_size=(224,224,3))
            img = image.img_to_array(img)
            images.append(img)
        images = np.asarray(images)
        if self.preprocess_fn != None:
            images = self.preprocess_fn(images)   
        
        return images
    
    # Return labels in one-hot encoding
    def get_labels(self):
        
        return to_categorical(np.asarray(self.label_list), self.num_classes)
    

def fcn_classifier(input_shape=(2048,), units=512, classes=6,  l1=0.01, l2=0.01):
    features = Input(shape=input_shape)
    x = Dense(units, activation='relu')(features)
    x = Dropout(0.5)(x)
    y = Dense(classes, activation='softmax', kernel_regularizer=l1_l2(l1=l1, l2=l2))(x)
    model = Model(inputs=features, outputs=y)
    model.compile(optimizer='adadelta', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def train_evaluate(run):
   
    # Create bottleneck featurs
    train_images_dir = os.path.join(FLAGS.data_folder, 'train')
    valid_images_dir = os.path.join(FLAGS.data_folder, 'valid')

    train_generator = ImageGenerator(train_images_dir, resnet50.preprocess_input)
    valid_generator = ImageGenerator(valid_images_dir, resnet50.preprocess_input)

    featurizer = resnet50.ResNet50(
                weights = 'imagenet', 
                input_shape=(224,224,3), 
                include_top = False,
                pooling = 'avg')

    print("Generating bottleneck features")
    train_features = featurizer.predict_generator(train_generator, verbose=1)
    train_labels = train_generator.get_labels()

    valid_features = featurizer.predict_generator(valid_generator, verbose=1)
    valid_labels = valid_generator.get_labels()
    
    # Create a classifier
    model = fcn_classifier(input_shape=(2048,), units=FLAGS.units, l1=FLAGS.l1, l2=FLAGS.l2)
    
    # Start training
    print("Starting training")
    model.fit(train_features, train_labels,
          batch_size=64,
          epochs=20,
          shuffle=True,
          validation_data=(valid_features, valid_labels))
          
    # Save the trained model to outp'uts which is a standard folder expected by AML
    print("Training completed.")
    os.makedirs('outputs', exist_ok=True)
    model_file = os.path.join(FLAGS.save_model_dir, 'model.hd5')
    print("Saving model to: {0}".format(model_file))
    model.save(model_file)
    

FLAGS = tf.app.flags.FLAGS

# Default global parameters
tf.app.flags.DEFINE_integer('batch_size', 32, "Number of images per batch")
tf.app.flags.DEFINE_integer('epochs', 10, "Number of epochs to train")
tf.app.flags.DEFINE_integer('units', 512, "Number of epochs to train")
tf.app.flags.DEFINE_float('l1', 0.01, "Number of epochs to train")
tf.app.flags.DEFINE_float('l2', 0.01, "Number of epochs to train")
tf.app.flags.DEFINE_string('data_folder', 'aerialsmall', "Folder with training and validation images")
tf.app.flags.DEFINE_string('save_model_dir', './outputs', "A folder for saving trained model")


def main(argv=None):
    # get hold of the current run
    run = Run.get_submitted_run()
    train_evaluate(run)
  

if __name__ == '__main__':
    tf.app.run()