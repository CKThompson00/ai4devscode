Clear-Host
$uri = ($env:ANOMALY_DETECTION_ENDPOINT) + "anomalydetector/v1.0/timeseries/last/detect"
$params = @"
],
    "maxAnomalyRatio": 0.25,
    "sensitivity": 80
  }
"@

$body = @"
{
    "series": [
"@

##################################
# Prepopulate 15 or so records
##################################
$counter = "\processor(_total)\% processor time"
$perfCollection = New-Object System.Collections.ArrayList

Write-Output "Preloading 15 data points..."
$index = 0
while ($index -lt 15)
{
  $perf = (Get-Counter -Counter $counter).CounterSamples  | Select-Object Path, InstanceName, CookedValue, RawValue, TimeStamp
  $perf.TimeStamp = $perf.TimeStamp.ToString()
  Start-Sleep -Seconds 2
  $index += 1
  $perfCollection.Add($perf) | out-null 
  Write-Output ("Data Point #: " + ($index).Tostring() + " - " + $perf.CookedValue.ToString())
}

Write-Output "Starting...."
while (1)
{

    $perf = (Get-Counter -Counter $counter).CounterSamples  | Select-Object Path, InstanceName, CookedValue, RawValue, TimeStamp
    $perf.TimeStamp = $perf.TimeStamp.ToString()
    Start-Sleep -Seconds 5
    $perfCollection.Add($perf) | out-null 

#    BuildJson()

    $body = @"
            { 
              "series": [
"@

    $firstTrip = $true
    foreach ($perfCounter in $perfCollection)
    {
      $ts = $perfCounter.Timestamp
      $value = $perfCounter.CookedValue

      if ($firstTrip)
      {
        $body += @"
        {
          "timestamp": "$ts",
          "value": "$value"
        }
"@      
      }
      else
      {
        $body += @"
        ,{
          "timestamp": "$ts",
          "value": "$value"
        }
"@      
      }
      $firstTrip = $false
    }

    # $body + $params
    $results = Invoke-WebRequest `
              -Uri $uri -Method Post `
              -Headers @{
                "Ocp-Apim-Subscription-Key"=($env:ANOMALY_DETECTION_API_KEY);
                "Content-Type"="application/json"
              } `
              -Body ($body + $params)
    
    $jsonResults = $results.Content | ConvertFrom-Json 

    # $source = ($body + $params) | ConvertFrom-Json
    $index = 0
    if ($jsonResults.isAnomaly)
    {
      Write-Output ("Is Anomaly; ActualValue == " + $perf.CookedValue + "; ExpectedValue == " + $jsonResults.expectedValue + "; LowerMargin == " + $jsonResults.lowerMargin + "; UpperMargin == " + $jsonResults.upperMargin)
    }
    else 
    {
      Write-Output ("Is NOT an Anomaly; ActualValue == " + $perf.CookedValue + "; ExpectedValue == " + $jsonResults.expectedValue + "; LowerMargin == " + $jsonResults.lowerMargin + "; UpperMargin == " + $jsonResults.upperMargin)
    }
}
Write-Output "`n"