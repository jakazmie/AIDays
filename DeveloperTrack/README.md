# Developer Track

This folder contains hands-on labs that demonstrate how to develop intelligent applications, agents, and knowledge mining solutions
using Cognitive Services, Bot Services, and Cognitive Search.

## Pre-requisties

To complete the labs you will need:
- An Azure subscription with enough credits - TBD
- Chrome browser
- Azure Data Science Virtual Machine
  

### To set up Azure Data Science Virtual Machine

1. Navigate to [link](https://portal.azure.com/#create/microsoft-dsvm.linux-data-science-vm-ubuntulinuxdsvmubuntu){:target="_blank"} to start provisioning. Create the VM as follows: 
   - Create a new resource group for your VM
   - Use **D8s_v3** as a VM type. Although, the labs will run on other configurations this is the minimum configuration we recommend. 
   - Shoose *username and password* as the authentication type. 
   - Use default values for all other parameters.

 https://portal.azure.com/#create/microsoft-dsvm.linux-data-science-vm-ubuntulinuxdsvmubuntu

2. When your VM is ready use Azure Portal Cloud Shell to configure it up for the labs

```
# Logon to your VM
ssh <your username>@<vm ip address>

# Clone the labs in the notebooks folder
cd notebooks
git clone https://github.com/jakazmie/AIDays.git

# Enable AML widgets. This is to address the bug in DSVM default configuration
source activate py36
jupyter nbextension enable --py --user azureml.train.widgets

# Install modules required by the lab which are missing from the default configuration
pip install h5py

# logout from VM
exit
```


3. Use Chrome browser to connect to Jupyter Hub at http://<your machine's IP address>:8000. You may receive a warning that `Your connection is not private`. Ignore it and press on **ADVANCED** to proceed.

3. Use your username and password to log in to Jupyter

4. This step is a temporary walk-around to address issues with AML Widgets on Azure Data Science Machine
```
# Log back to your DSVM
ssh <your username>@<vm ip address>

# Enable AML widgets. This is to address the bug in DSVM default configuration
source activate py36
jupyter nbextension enable --py --user azureml.train.widgets
```

5. You are ready to start the labs

**Important**. Make sure to set the kernel of each notebook in the lab to *Python 3.6 - AzureML*.




# The labs:


## 01-AzureDatabricks-DeepLearningPipelines
This lab walks you through building a custom image classification model using Transfer Learning and Azure Databricks Deep Learning Pipelines


## 02-AML-EndToEndWalkthrough
This lab demonstrates how to orchestrate an end-to-end machine learning workflow using Azure Machine Learning service. During the lab you will develop, fine-tune, and operationalize a custom image classification model using Transfer Learning and TensorFlow. 
