# Building a custom image classification solution with Custom Vision Service
In this lab we will train, evaluate, and deploy a custom image classification model using Microsoft Cognitive Services Custom Vision Service. 

The Custom Vision Service is an Azure Cognitive Service that lets you build custom image classifiers and object detectors. The Custom Vision Service provides a REST API and a web interface to orchestrate model training and operationalization.

The lab is designed to be instructor guided.  In addition to walking you through the lab's steps, the instructor will explain key concepts and as necessary deep dive into technical details. 

Don't hesitate to ask questions !

## What will you learn during the lab?
The lab consists of 2 parts:
- In the first part you will train, evaluate and test a custom image classification model.
- In the second part, you will export the trained model


## Scenario

You will train a custom image classification model to automatically classify the type of land shown in aerial images of 224-meter x 224-meter plots. Land use classification models can be used to track urbanization, deforestation, loss of wetlands, and other major environmental trends using periodically collected aerial imagery. The images used in this lab are based on imagery from the U.S. National Land Cover Database. U.S. National Land Cover Database defines six primary classes of land use: *Developed*, *Barren*, *Forested*, *Grassland*, *Shrub*, *Cultivated*. For the sake of simplicity, in this lab you will train and operationalize a classifier to recognize three classes: *Barren*, *Developed*, *Cultivated*.  Example images in each land use class are shown here:

Developed | Cultivated | Barren
--------- | ------ | ----------
![Developed](images/developed1.png) | ![Cultivated](images/cultivated1.png) | ![Barren](images/barren1.png)


## Lab Environment setup

* Navigate to your Library in Azure Notebooks
* Click on **+** icon
* Click on **From URL**
* In **File Url** paste the below link

https://raw.githubusercontent.com/jakazmie/AIDays/master/DeveloperTrack/01-CustomVisionService/train.ipynb

5. Click **Upload**

* Repeat for 

https://raw.githubusercontent.com/jakazmie/AIDays/master/DeveloperTrack/01-CustomVisionService/export.ipynb

You can walk through the lab in two ways:
- Using Custom Vision Service web interface
- Using Custom Vision Service Python SDK

If you prefer to use code-first interface start ` train.ipynb` notebook in Azure Notebooks.

Otherwise continue to the next step.

[Next step](train.md)


