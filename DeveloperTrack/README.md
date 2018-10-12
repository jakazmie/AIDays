# Developer Track

This folder contains hands-on labs that demonstrate how to develop intelligent applications, agents, and knowledge mining solutions using Cognitive Services, Bot Services, and Cognitive Search.

## Pre-requisties

- An Azure subscription, and 
- Chrome browser
  
## Lab environmant setup

Follow the steps below to provision the services that will be utilized during the labs:

### Set up Cognitive Services

* Login to Azure Portal using credentials bound to your Azure subscription:
http://portal.azure.com

* Navigate to Cognitive Services blade in Azure Portal. You can browse through the portal starting with **Create a resource** link or take a shortcut using the following link. 
https://ms.portal.azure.com/#blade/Microsoft_Azure_Marketplace/GalleryResultsListBlade/selectedSubMenuItemId/%7B%22menuItemId%22%3A%22gallery%2FCognitiveServices_MP%2FCognitiveService%22%2C%22resourceGroupId%22%3A%22%22%2C%22resourceGroupLocation%22%3A%22%22%2C%22dontDiscardJourney%22%3Afalse%2C%22launchingContext%22%3A%7B%22source%22%3A%5B%22GalleryFeaturedMenuItemPart%22%5D%2C%22menuItemId%22%3A%22CognitiveServices_MP%22%2C%22subMenuItemId%22%3A%22CognitiveService%22%7D%7D


* Provision **Custom Vision Service**
  * Click on **Custom Vision (preview)**
  * Click on **Create**
  * Enter a name for the service
  * Choose **South Central US** location
  * Choose **F0** Prediction pricing tier
  * Choose **F0** Training pricint tier
  * Create **a new Resource group**
  
* Provision **Text Analytics Service**
  * Navigate back to the Cognitive Services blade
  * Click on **Text Analytics**
  * Click on **Create**
  * Enter a name for the service
  * Choose **South Central US** location
  * Choose **F0** Pricing tier
  * Choose the resource group you created for Custom Vision Services
  
* Provision  **Bing Speech Service**
  * Navigate back to the Cognitive Services blade
  * Click on **Bing Speech**
  * Click on **Create**
  * Enter a name for the service
  * Choose **South Central US** location
  * Choose **F0** Pricing tier
  * Choose the resource group you created for Custom Vision Services
  
* Provision  **Language Understanding Service**
  * Navigate back to the Cognitive Services blade
  * Click on **Language Understanding**
  * Click on **Create**
  * Enter a name for the service
  * Choose **South Central US** location
  * Choose **F0** Pricing tier
  * Choose the resource group you created for Custom Vision Services
  
### Set up Azure Notebooks

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

https://raw.githubusercontent.com/jakazmie/AIDays/master/DeveloperTrack/01-CustomVisionService/invoke_endpoint.ipynb

* Repeat for

https://raw.githubusercontent.com/jakazmie/AIDays/master/DeveloperTrack/02-TextAndSpeech/cognitive-services-text-speech.ipynb



You are now ready to proceed to the labs. Some labs may require additional setup. If this is the case, the setup steps will described in the lab's notes.

Enjoy.



