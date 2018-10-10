# Create Hands-on Lab Environment

The script will create Azure Services includes DSVM, Blob SQL DB and also copy some sample data into your blob

1. Open browser and go to [Azure Portal](https://portal.azure.com)

1. __Click__ on _new Dashboard_

    ![new dashboard](./images/00.01.png)

1. __Type__ name of the dashboard as _Azure Workshop_

    ![new dashboard](./images/00.02.png)

1. Open cloud shell from the browser

    ![cloudshell](./images/00.03.png)

1. Download a script

    Run following commnad from the cloud shell prompt

    > Please copy below command and past it to cloud shell prompt


	```bash
	wget -O CreateLabEnv.azcli https://raw.githubusercontent.com/jakazmie/AIDays/master/DeveloperTrack/03-KnowledgeMining/script/00CreateLabEnv.azcli
	```

1. Run command to create a resource group and resource

    > Care with subscription name when you run the script

    ```bash
    sh ./CreateLabEnv.azcli
    ```

    ![run script](./images/env01.01.png)

    Make sure you use correct __Azure Subscription__ for the Hands-on lab.

1. Make sure you have a resource group and Blob in the resource group

---
[01. Create Azure Search](01CreateSearch.md)