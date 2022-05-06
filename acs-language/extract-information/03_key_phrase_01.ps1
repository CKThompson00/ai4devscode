Clear-Host
##########################################################################
#                               VARIABLES
##########################################################################
$API_KEY = ($env:COGSVC_API_KEY_MP)
$endpoint = ($env:COGSVC_ENDPOINT_MP)

### Optionally use v3.2-preview.2 for the v3.1 to show preview
$endpointURL = $endpoint + "text/analytics/v3.1/keyPhrases"

##########################################################################
#                               ALLOW ARGS
##########################################################################
if ($args[0] -eq "" -or $null -eq $args[0])
{
    $jsonFile = "03_key_phrase_02.json"
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
$phrases = $jsonResults.Content | ConvertFrom-Json   
$jsonResults.Content | Out-File -FilePath ($jsonFile + ".output.json")

$phrases.documents
foreach ($document in $phrases.documents)
{
    Write-Output ("Document ID: " + $document.id)
    foreach ($keyPhrase in $document.keyPhrases)
    {
        $keyPhrase
    }
    Write-Output ""
}
