Clear-Host
##########################################################################
#                               VARIABLES
##########################################################################
$API_KEY = ($env:LANGUAGE_API_KEY)
$endpoint = ($env:LANGUAGE_ENDPOINT)

$endpointURL = $endpoint + "text/analytics/v3.2-preview.2/analyze"

##########################################################################
#                               ALLOW ARGS
##########################################################################
if ($args[0] -eq "" -or $null -eq $args[0])
{
    $jsonFile = "11_custom_ner_01.json"
}   
else 
{
    $jsonFile =  $args[0]
}

##########################################################################
#                               READ FILE
##########################################################################
$body = Get-Content $jsonFile -Raw
$doc =  Get-Content ($jsonFile + ".txt") -Raw
$doc = $doc.Replace("""", "\""")
$body = $body.Replace("YOUR_DOCUMENT_HERE", $doc)

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

$summary = $jsonResults.Content | ConvertFrom-Json   

Write-Output ""
foreach ($task in $summary.tasks)
{
    foreach ($cner in $task.customEntityRecognitionTasks)
    {
        foreach ($results in $cner.results)
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
                }
            }
        }
        Write-Output ""
    }
}
