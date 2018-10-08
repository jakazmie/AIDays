# Deploy a custom vision service container to Azure Container Instance

## Create a docker image from the exported zip file

## Create a resource group
```
az group create --name <resource group> --location <location>
```

## Create a container
```
az container create --resource-group <resource group> --name <container name> --image <image name> --dns-name-label <dns prefix> --ports 80
```

## Show the container's status
```
az container show --resource-group <Your resource group> --name <Container name> "
```
## Invoke the prediction point in the container
```
curl -X POST http://<container FQDN>/image -F imageData=@<image file>
```
