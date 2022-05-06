Clear-Host
##########################################################################
#                               VARIABLES
##########################################################################
$API_KEY = ($env:COGSVC_API_KEY_MP)
$endpoint = ($env:COGSVC_ENDPOINT_MP)
$endpointURL = $endpoint + "text/analytics/v3.1/entities/linking"

##########################################################################
#                               ALLOW ARGS
##########################################################################
$pwd
if ($args[0] -eq "" -or $null -eq $args[0])
{
    $jsonFile = "01_entity_linking_01.json"
}   
else 
{
    $jsonFile =  $args[0]
}

##########################################################################
#                               READ FILE
##########################################################################
$body = Get-Content $jsonFile

##########################################################################
#                               CALL API
##########################################################################
$jsonResults = Invoke-WebRequest `
                    -Uri $endpointURL `
                    -Method Post `
                    -Headers @{
                                "Ocp-Apim-Subscription-Key"=$API_KEY;
                                "Content-Type"="application/json"
                              } `
                    -Body $body

##########################################################################
#                               PARSE/PROCESS
##########################################################################
$entities = $jsonResults.Content | ConvertFrom-Json   
$jsonResults.Content | Out-File -FilePath ($jsonFile + ".output.json")
foreach ($entity in $entities.documents.entities) 
{
    $entity
} 
