# Developer Track

This folder contains hands-on labs that demonstrate how to develop intelligent applications, agents, and knowledge mining solutions
using Cognitive Services, Bot Services, and Cognitive Search.

## Pre-requisties

To complete the labs you will need:
- An Azure subscription with enough credits - TBD
- Chrome browser
- Azure Data Science Virtual Machine
  

### To set up Azure Data Science Virtual Machine

1.To provision DSVM navigate to 

https://portal.azure.com/#create/microsoft-dsvm.linux-data-science-vm-ubuntulinuxdsvmubuntu 

Create the VM with the following configuration: 
   - Create a new resource group for your VM
   - Use **D8s_v3** as a VM type. Although, the labs will run on other configurations this is the minimum configuration we recommend. 
   - Shoose *username and password* as the authentication type. 
   - Use default values for all other parameters.


2. When your VM is ready use Azure Portal Cloud Shell to configure it up for the labs

```
# Logon to your VM
ssh <your username>@<vm ip address>

# Clone the labs in the notebooks folder
cd notebooks
git clone https://github.com/jakazmie/AIDays.git

exit
```

