Clear-Host
##########################################################################
#                               VARIABLES
##########################################################################
$API_KEY = ($env:COGSVC_API_KEY_MP)
$endpoint = ($env:COGSVC_ENDPOINT_MP)

$endpointURL = $endpoint + "text/analytics/v3.2-preview.1/entities/recognition/general"

##########################################################################
#                               ALLOW ARGS
##########################################################################
if ($args[0] -eq "" -or $null -eq $args[0])
{
    $jsonFile = "07_ner_01.json"
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
$ner = $jsonResults.Content | ConvertFrom-Json   
$jsonResults.Content | Out-File -FilePath ($jsonFile + ".output.json")

$ner.documents
Write-Output ""
foreach ($document in $ner.documents)
{
    Write-Output ("Document ID: " + $document.id)
    foreach ($entity in $document.entities)
    {
        Write-Output "============================="
        Write-Output ("Text: " + $entity.text)
        Write-Output ("Category: " + $entity.category)
        Write-Output ("Confidence Score: " + $entity.confidenceScore)
        Write-Output ("Offset: " + $entity.offset)
        Write-Output ("Length: " + $entity.length)
    }
    Write-Output ""
}
