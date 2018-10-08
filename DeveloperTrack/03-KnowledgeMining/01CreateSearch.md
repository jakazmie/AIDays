# Create Search from Azure Portal

## Create an Azure Search service in the portal

Learn how to create or provision an Azure Search service in the portal.

## Find Azure Search
1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Click the plus sign ("+ Create Resource") in the top left corner.
3. Select **Web** > **Azure Search**.

![](./media/search-create-service-portal/find-search3.png)

## Name the service and URL endpoint

A service name is part of the URL endpoint against which API calls are issued: `https://your-service-name.search.windows.net`. Enter your service name in the **URL** field. 

Service name requirements:
   * It must be unique within the search.windows.net namespace
   * 2 and 60 characters in length
   * Use lowercase letters, digits, or dashes ("-")
   * Avoid dashes ("-") in the first 2 characters or as the last single character
   * No consecutive dashes ("--") anywhere

## Select a subscription
If you have more than one subscription, choose one that also has data or file storage services. Azure Search can auto-detect Azure Table and Blob storage, SQL Database, and Azure Cosmos DB for indexing via [*indexers*](search-indexer-overview.md), but only for services in the same subscription.

## Select a resource group
A resource group is a collection of Azure services and resources used together. For example, if you are using Azure Search to index a SQL database, then both services should be part of the same resource group.

## Select a hosting location 
As an Azure service, Azure Search can be hosted in datacenters around the world. Note that [prices can differ](https://azure.microsoft.com/pricing/details/search/) by geography.

## Select a pricing tier (SKU)
Standard is usually chosen for production workloads, but most customers start with the Free service.

A pricing tier cannot be changed once the service is created. If you need a higher or lower tier later, you have to re-create the service.

## Create your service

Remember to pin your service to the dashboard for easy access whenever you sign in.

![](./media/search-create-service-portal/new-service3.png)

---
[02.Create Indexer from Structured Data](02CreateIndexerSQL.md)
