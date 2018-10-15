# Azure Machine Learning service End-To-End Walkthrough

The goal of the lab is to introduce key components and features of Azure Machine Learning service. During the lab you will go through the full Machine Learning workflow from data preparation, through model training, to model operationalization.

The lab is not designed to explore all Azure ML features in detail. If you want to go deeper ask your instructor about Microsoft Technology Center Azure Machine Learning workshops.

## Lab environment set up

You can use Azure Data Science Virtual Machine or Azure Notebooks as your lab environment


### To set up Azure Notebooks

1. Navigate to: https://notebooks.azure.com
2. Login to Azure Notebooks using credentials bound to your Azure subscription
3. Click on **Libraries**
4. Click on **New Library**
5. Enter **Library Name** - any name you want
6. Enter **Library ID** - any ID you want
7. Click on **Create**
8. Click on **+** icon.
9. Click on **From URL**
10. In **File Url** paste the below link

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/00-intro.ipynb

11. Click **Upload**
12. Repeat for:

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/01-feature-engineering.ipynb

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/02-train.ipynb

https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/03-deploy.ipynb

Start `00-intro.ipynb` to begin the lab.

**Important. Make sure to set the kernel of each notebook in the lab to *Python 3.6*.**


### To set up Azure Data Science Virtual Machine

1. Follow the below link to provision Data Science Virtual Machine. 
   - Create a new resource group for your VM
   - Use **DS3_v2** or better as a VM type. Although, the labs will run on other configurations this is the minimum configuration we recommend. 
   - Choose *username and password* as the authentication type. 
   - Use default values for all other parameters.

 https://portal.azure.com/#create/microsoft-dsvm.linux-data-science-vm-ubuntulinuxdsvmubuntu

2. When your VM is ready use Azure Portal Cloud Shell to complete the configuration

```
# Logon to your VM
ssh <your username>@<vm ip address>

# Clone the labs in the notebooks folder
cd notebooks
git clone https://github.com/jakazmie/AIDays.git

exit
```

3. Use Chrome browser to connect to Jupyter Hub at `http://<your machine's IP address>:8000`. You may receive a warning that `Your connection is not private`. Ignore it and press on **ADVANCED** to proceed.

3. Use your username and password to log in to Jupyter

4. The next step is a temporary walk-around to address issues with AML Widgets on Azure Data Science Machine
```
# Log back to your DSVM
ssh <your username>@<vm ip address>

# Enable AML widgets. This is to address the bug in DSVM default configuration
source activate py36
jupyter nbextension enable --py --user azureml.train.widgets
```

**Important**. Make sure to set the kernel of each notebook in the lab to *Python 3.6 - AzureML*.


Enjoy.





