# Create Lab environment

## Prerequisites

- [ ] Your own laptop
    * (Windows or Mac)

- [ ] Azure subscription as:
    * Subscription contributor
    * Resource group onwer
    * South Central US or West Europe

- [ ]  4 or more vCore Quota for a Data Science VM
    * Any Azure region

- [ ] CloudShell

## Overview Architecture of this Lab

## [00. Run a Script to create the environment](00CreateLabEnv.md)

The script will create Azure Services includes DSVM, Blob SQL DB and also copy some sample data into your blob

## [01. Create Search Service](01CreateSearch.md)

## [02. Create Indexer for Structured Data](02CreateIndexerSQL.md)

02.01. Create data source object

02.02. Create schema

02.03. Run Indexer

## [03. Create Indexer for Unstructured Data](03CreateIndexerBlob.md)

03.01. Create data source object

03.02. Create Skillset

03.03. Create schema

03.04. Run Indexer

## [04. Integrate Search into your Web App](04IntegrateintonApp.md)

04.01. Import Notebook

04.02. Update codes and Run Sample

## [05. Clean up](05Cleanup.md)

---