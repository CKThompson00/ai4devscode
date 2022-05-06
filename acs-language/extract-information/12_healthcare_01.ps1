Clear-Host
##########################################################################
#                               VARIABLES
##########################################################################
$API_KEY = ($env:COGSVC_API_KEY_MP)
$endpoint = ($env:COGSVC_ENDPOINT_MP)

$endpointURL = $endpoint + "text/analytics/v3.1/entities/health/jobs"

##########################################################################
#                               ALLOW ARGS
##########################################################################
if ($args[0] -eq "" -or $null -eq $args[0])
{
    $jsonFile = "12_healthcare_01.json"
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

$operationLoc = $jsonResults.Headers["operation-location"][0]
if ($jsonResults.StatusCode  -eq 202)
{
    while ($jsonResults.StatusCode  -eq 202) 
    {
        Start-Sleep -Seconds 5
        $jsonResults = Invoke-WebRequest `
        -Uri $operationLoc `
        -Method Get `
        -Headers @{
                    "Ocp-Apim-Subscription-Key"=$API_KEY;
                    "Content-Type"="application/json"
                  } `
    }
}

##########################################################################
#                               PARSE/PROCESS
##########################################################################
$jsonResults.Content | Out-File -FilePath ($jsonFile + ".output.json")

$health = $jsonResults.Content | ConvertFrom-Json   

Write-Output ""
foreach ($results in $health.results)
{
    foreach ($document in $results.documents)
    {
        Write-Output ("Document ID: " + $document.id)
        foreach ($entities in $document.entities)
        {
            Write-Output "============================="
            Write-Output ("Text: " + $entities.text)
            Write-Output ("Category: " + $entities.category)
            Write-Output ("Confidence Score: " + $entities.confidenceScore)
            Write-Output ("Offset: " + $entities.offset)
            Write-Output ("Length: " + $entities.length)
            Write-Output $entities.links
        }
    }
    Write-Output ""
}
