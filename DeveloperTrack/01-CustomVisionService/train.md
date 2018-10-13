# Part 1 - Model training and evaluation

In this part of the lab we will train, evaluate, and test a custom image classification model using Custom Vision Service web interface. 

## Create Custom Vision Service project

The first step is to create the Custom Vision Service project.The project is a container for model development artifacts, including training data, model iterations, history of training runs, etc. 

1. Navigate to Custom Vision Service web portal

https://customvision.ai

2. Sign in with you Azure account

3. On the Custom Vision Service's home page click on **NEW PROJECT**

![Custom vision](images/projects.png)

4. In the **Resource Group** field select the resource group you created during the lab setup.

5. Select *Classification* for the project type, *Multiclass* for the classification type, and *General* for the domain type. Then click on **create new** *Resource Group*

![new project](images/newproject.png)

 6. Click on **Create project**


## Prepare training data
Download and unzip training data to your local drive.

https://azureailabs.blob.core.windows.net/aerialsamples/aerial.zip


## Upload and tag training images
1. Navigate to the project section of Custom Vision Service Web GUI.

https://customvision.ai/projects

2. Click on the project you created in the previous steps.

![Select the project](images/img4.PNG)

3. To add the first set of images to your project, use the **Add images** button. Navigate to `aerial/train/Barren` and select and add all images.

![Add images](images/img5.PNG)


4. To set the tag, enter *Barren* in the **My Tags** field. 

5. Repeat for images in `Cultivated` and `Developed` subfolders, using the respective tags.

## Train and evaluate the first iteration of the model
1. To train the classifier, click on the **Train** button.

![Train](images/img6.PNG)

2. After training is completed you will see the screen with the evaluation metrics. Your instructor will explain how to interpret the metrics.


![Evaluate](images/img7.PNG)


## Test your model
1. You can perform a quick test of the model on unseen data by clicking the **Quick Test** button located to the right of the **Train**. This action opens a window labeled **Quick Test**.
2. In the **Quick Test** window click the Browse local files button and select a local image file. The testing images for our lab can be found in `aerial/test`

![Quick est](images/img8.PNG)


## Improve the model
You can use many strategies to improve performance of your model. Your instructor will elaborate on the most common techniques. 

In the following steps you will apply two approaches. First you will review your training data looking for potentially mislabeled instances. Second, you will add more samples of the class for which the classifier did not perform well. 

Recall that the images tagged as *Developed* had the lowest performance metrics. As such we will focus on improving the performace of our classifier on this class.

1. Browse through the images labeled as *Developed*. You will notice some images with questionable tagging.

![Mislabeled](images/img9.PNG)
![Mislabeled](images/img10.PNG)

2. You can re-label the image(s) by selecting it and clicking on the **Tag images** button. Re-label the images in question to the class that in your opinion is the right label.

3. You will also add additional images to the *Developed* class. You can find them in `aerial/train/Developed-SecondBatch`. Select and label all images from that folder.

4. Click on **Train** button to retrain the model. You will notice the second iteration of the model after the training is completed. Your instructor will explain the concept of the iteration in more detail. 

5. Review the new evaluation metrics. Both **Precision** and **Recall** should be higher. Note that your numbers may be slightly different than ours.

![Second iteration](images/img11.PNG)


## Test the model 
You can test the model by clicking on **Quick Test** and using one of the images in the `test` subfolder of the downloaded dataset.

Congratulations! 

[Next step](export.md)

