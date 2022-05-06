clear-host
$headers = @{
            "Ocp-Apim-Subscription-Key" = "$env:LANGUAGE_API_KEY";
            "content-type" = "application/json"
            }

########################################################
#  Uncomment the line below and the one below it
#    to enable opinion mining to demo
#$uri = ($env:LANGUAGE_ENDPOINT) + "/text/analytics/V3.1/sentiment"
$uri = $env:LANGUAGE_ENDPOINT + "/text/analytics/V3.1/sentiment?opinionMining=true"
########################################################

$body = @"
        {
            "documents": [
                            {
                            "id": "1",
                            "text": "The stay was great.  I loved the room.  The food was not good though.",
                            "language": "en"
                            }
                        ]
        }
"@

$response = Invoke-RestMethod -Method Post -Headers $headers -Uri $uri -Body $body 

$response | convertto-json -Depth 10 
$response | convertto-json -Depth 10 | out-file 01_sentiment/output.json
