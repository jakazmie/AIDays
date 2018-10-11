# Data Science Track

This folder contains hands-on labs that demonstrate how to develop and operationalize custom AI/ML models using Azure AI Machine Learning services: Azure Databricks and Azure Machine Learning service. **The labs are designed to be led by an instructor.**  They can be used for self-study but the commentary is terse and it is expected
that the instructor will walk participants through the lab, deep dive into the code, and answer any arising questions. The labs are independent and self-contained and can be executed in arbitrary combinations. 


## Pre-requisties

- An Azure subscription. You will need to be able to provision Azure Machine Learning workspace and Azure Batch AI clusters with NC6 VMs
- Chrome browser

You can use Azure Data Science Virtual Machine or Azure Notebooks as your lab environment


### To set up Azure Notebooks

* Navigate to: https://notebooks.azure.com
* Login to Azure Notebooks using credentials bound to your Azure subscription
* Click on **Libraries**
* Click on **New Library**
* Enter **Library Name** - any name you want
* Enter **Library ID** - any ID you want
* Click on **Create**
* After your Library is ready
* Click on **+** icon
* Click on **From URL**
* In **File Url** paste the below link

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/01-experiment.ipynb

* Repeat for

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/02-train.ipynb

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/03-deploy.ipynb

**Important**. Make sure to set the kernel of each notebook in the lab to *Python 3.6*.





### To set up Azure Data Science Virtual Machine

1. Follow the below link to provision Data Science Virtual Machine. 
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

# logout from VM
exit
```

3. Use Chrome browser to connect to Jupyter Hub at `http://<your machine's IP address>:8000`. You may receive a warning that `Your connection is not private`. Ignore it and press on **ADVANCED** to proceed.

3. Use your username and password to log in to Jupyter

4. This step is a temporary walk-around to address issues with AML Widgets on Azure Data Science Machine
```
# Log back to your DSVM
ssh <your username>@<vm ip address>
source activate py36

# Install modules required by the lab which are missing from the default configuration
pip install h5py

# Enable AML widgets. This is to address the bug in DSVM default configuration
jupyter nbextension enable --py --user azureml.train.widgets
```



**Important**. Make sure to set the kernel of each notebook in the lab to *Python 3.6 - AzureML*.



You are now ready to proceed to labs. Some labs may require additionao setup. If this is the case, the setup steps will described in the lab's notes.

Enjoy.
