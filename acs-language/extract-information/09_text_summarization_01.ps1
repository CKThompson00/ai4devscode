Clear-Host
##########################################################################
#                               VARIABLES
##########################################################################
$API_KEY = ($env:COGSVC_API_KEY_MP)
$endpoint = ($env:COGSVC_ENDPOINT_MP)

$endpointURL = $endpoint + "text/analytics/v3.2-preview.1/analyze"

##########################################################################
#                               ALLOW ARGS
##########################################################################
if ($args[0] -eq "" -or $null -eq $args[0])
{
    $jsonFile = "09_text_summarization_01.json"
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

$summary = $jsonResults.Content | ConvertFrom-Json   

Write-Output ""
foreach ($task in $summary.tasks)
{
    foreach ($est in $task.extractiveSummarizationTasks)
    {
        foreach ($results in $est.results)
        {
            foreach ($document in $results.documents)
            {
                Write-Output ("Document ID: " + $document.id)
                foreach ($sentences in $document.sentences)
                {
                    Write-Output "============================="
                    Write-Output ("Text: " + $sentences.text)
                    Write-Output ("Rank Score: " + $sentences.rankScore)
                    Write-Output ("Offset: " + $sentences.offset)
                    Write-Output ("Length: " + $sentences.length)
                }
            }
        }
        Write-Output ""
    }
}
