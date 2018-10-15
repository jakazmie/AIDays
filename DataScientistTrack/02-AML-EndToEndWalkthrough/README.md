# Azure Machine Learning service End-To-End Walkthrough

The goal of the lab is to introduce key components and features of Azure Machine Learning service. During the lab you will go through the full Machine Learning workflow from data preparation, through model training, to model operationalization.

The lab is not designed to explore all Azure ML features in detail. If you want to go deeper ask your instructor about Microsoft Technology Center Azure Machine Learning workshops.

## Lab environment set up

You can use Azure Data Science Virtual Machine or Azure Notebooks as your lab environment


### To set up Azure Notebooks

* Navigate to: https://notebooks.azure.com
* Login to Azure Notebooks using credentials bound to your Azure subscription
* Click on **Libraries**
* Click on **New Library**
* Enter **Library Name** - any name you want
* Enter **Library ID** - any ID you want
* Click on **Create**



### To set up Azure Data Science Virtual Machine

1. Follow the below link to provision Data Science Virtual Machine. 
   - Create a new resource group for your VM
   - Use **DS3_v2** as a VM type. Although, the labs will run on other configurations this is the minimum configuration we recommend. 
   - Choose *username and password* as the authentication type. 
   - Use default values for all other parameters.

 https://portal.azure.com/#create/microsoft-dsvm.linux-data-science-vm-ubuntulinuxdsvmubuntu

2. When your VM is ready use Azure Portal Cloud Shell to configure it up for the labs

```
# Logon to your VM
ssh <your username>@<vm ip address>

# Clone the labs in the notebooks folder
cd notebooks
git clone https://github.com/jakazmie/AIDays.git

# Install modules required by the lab which are missing from the default configuration
source activate py36
pip install h5py

# logout from VM
exit
```

3. Use Chrome browser to connect to Jupyter Hub at `http://<your machine's IP address>:8000`. You may receive a warning that `Your connection is not private`. Ignore it and press on **ADVANCED** to proceed.

3. Use your username and password to log in to Jupyter

4. The next step is a temporary walk-around to address issues with AML Widgets on Azure Data Science Machine
```
# Log back to your DSVM
ssh <your username>@<vm ip address>

# Enable AML widgets. This is to address the bug in DSVM default configuration
jupyter nbextension enable --py --user azureml.train.widgets
```



**Important**. Make sure to set the kernel of each notebook in the lab to *Python 3.6 - AzureML*.



You are now ready to proceed to labs. Some labs may require additionao setup. If this is the case, the setup steps will described in the lab's notes.

Enjoy.


If you are using Azure Data Science Virtual Machine and you have stepped through the setup instructions you are ready to go.

To set up the environment on Azure Notebooks upload the lab's Jupyter notebooks to your Azure Notebooks library:

1. Navigate to your Azure Notebooks library.
2. Click on **+** icon.
3. Click on **From URL**
4. In **File Url** paste the below link
https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/00-intro.ipynb
5. Click **Upload**
6. Repeat for:
https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/01-train.ipynb
https://raw.githubusercontent.com/jakazmie/AIDays/master/DataScientistTrack/02-AML-EndToEndWalkthrough/02-deploy.ipynb

Start `00-intro.ipynb` to begin the lab.

Enjoy.



