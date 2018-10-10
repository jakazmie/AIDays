import json
import os
import tensorflow as tf
from tensorflow.keras.applications import resnet50
from tensorflow.keras.preprocessing import image
import numpy as np
import random
from azureml.core.model import Model

def init():
    # Instantiate Resnet50 featurizer
    global featurizer
    featurizer = resnet50.ResNet50(
            weights = 'imagenet', 
            input_shape=(224,224,3), 
            include_top = False,
            pooling = 'avg')

    # Load the model
    global model
    # retreive the path to the model file using the model name
    model_path = Model.get_model_path('aerial_classifier')
    model = tf.keras.models.load_model(model_path)

def run(raw_data):
    # convert json to numpy array
    img = np.array(json.loads(raw_data)['data'])
    # img = np.expand_dims(img, axis=0)
    # normalize as required by ResNet50
    # img = resnet50.preprocess_input(img)
    # extract bottleneck features
    # features = featurizer.predict(img)
    # make prediction
    # predictions = model.predict(features)
    predictions = img.shape
    return json.dumps(predictions.tolist())