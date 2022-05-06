# Demo Instructions for Extract Information APIs

## Entity Linking

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/entity-linking/quickstart?pivots=rest-api

### REST API
1. Open 01_entity_linking_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters
3. Show the 01_entity_linking_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 01_entity_linking_01.json.output.json and format -- show this as the raw output
7. Change the source input file in the.ps1 file to 01_entity_linking_02.json or run from the bash terminal with that file as a parameter 
8. Note Microsoft has 2 matches now

### Python
1. Open the 02_entity_linking_01.py file in VS Code
2. Show the 02_requirements.txt and explain they need to install that module
3. Walk through the code noting no JSON required for the SDK
4. Run the sample in VS Code
5. Walk through the output
6. Note the Python SDK is here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics
7. Note the C# SDK is here: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/textanalytics/Azure.AI.TextAnalytics
8. Note the Java SDK is here: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics
9. All of these can be found at this anchor: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/entity-linking/quickstart?pivots=rest-api

## Key Phrases 

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api

### REST API
1. Open 03_key_phrase_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters
3. Show the 03_key_phrase_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 03_key_phrase_01.json.output.json and format -- show this as the raw output
7. Change the source input file in the.ps1 file to 03_ke_phrase_02.json or run from the bash terminal with that file as a parameter 
8. Note the output - specifically the longer text and French

### Python
1. Open the 04_key_phrase_01.py file in VS Code
2. Show the 04_requirements.txt and explain they need to install that module
3. Walk through the code noting no JSON required for the SDK
4. Run the sample in VS Code
5. Walk through the output
6. Note the Python SDK is here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics
7. Note the C# SDK is here: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/textanalytics/Azure.AI.TextAnalytics
8. Note the Java SDK is here: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics
9. All of these can be found at this anchor: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/key-phrase-extraction/quickstart?pivots=rest-api


## PII

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api

### REST API
1. Open 05_pii_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters
3. Show the 05_pii_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 05_pii_01.json.output.json and format -- show this as the raw output
7. Change the source input file in the.ps1 file to 05_pii_02.json or run from the bash terminal with that file as a parameter 
8. Note the output

### Python
1. Open the 06_pii_01.py file in VS Code
2. Show the 06_requirements.txt and explain they need to install that module
3. Walk through the code noting no JSON required for the SDK
4. Run the sample in VS Code
5. Walk through the output
6. Note the Python SDK is here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics
7. Note the C# SDK is here: https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics
8. Note the Java SDK is here: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics
9. All of these can be found at this anchor: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/personally-identifiable-information/quickstart?pivots=rest-api

## Named Entity Recognition

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api

### REST API
1. Open 07_ner_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters
3. Show the 07_ner_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 07_ner_01.json.output.json and format -- show this as the raw output
7. Change the source input file in the.ps1 file to 07_ner_02.json or run from the bash terminal with that file as a parameter 
8. Note the output

### Python
1. Open the 08_ner_01.py file in VS Code
2. Show the 08_requirements.txt and explain they need to install that module
3. Walk through the code noting no JSON required for the SDK
4. Run the sample in VS Code
5. Walk through the output
6. Note the Python SDK is here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics
7. Note the C# SDK is here: https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics
8. Note the Java SDK is here: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics
9. All of these can be found at this anchor: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/named-entity-recognition/quickstart?pivots=rest-api

## Text Summarization

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/text-summarization/quickstart?pivots=rest-api

### REST API
1. Open 09_text_summarization_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters.  Also not this is an Asynchronous call.  Talk through how that works.
3. Show the 09_text_summarization_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 09_text_summarization_01.json.output.json and format -- show this as the raw output
7. Change the source input file in the.ps1 file to 09_text_summarization_02.json or run from the bash terminal with that file as a parameter 
8. Note the output

### Python
1. Open the 10_text_summarization_01.py file in VS Code
2. Show the 08_requirements.txt and explain they need to install that module
3. Walk through the code noting no JSON required for the SDK
4. Run the sample in VS Code
5. Walk through the output
6. Note the Python SDK is here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics
7. Note the C# SDK is here: https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics
8. Note the Java SDK is here: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics
9. All of these can be found at this anchor: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/text-summarization/quickstart?pivots=rest-api

## Custom Named Entity

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/custom-named-entity-recognition/quickstart?pivots=rest-api

### Project Setup

1. Follow this document to build a custom NER project and train - https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/custom-named-entity-recognition/quickstart?pivots=language-studio.

### Inferencing

#### REST API
1. Open 11_custom_ner_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters.  Also note this is an Asynchronous call.  Talk through how that works.
3. Show the 11_custom_ner_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 11_custom_ner_01.json.output.json and format -- show this as the raw output

## Healthcare

Reference: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/text-analytics-for-health/quickstart?pivots=rest-api

### REST API
1. Open 12_healthcare_01.ps1 file in VS Code
2. Walk through the code - note the rest endpoint and the parameters.  Also note this is an Asynchronous call.  Talk through how that works.
3. Show the 12_healthcare_01.json file as the input
4. Run in either VSCode or bash (pwsh if Bash)
5. Walk through the output 
6. Now show the 12_healthcare_01.json.output.json and format -- show this as the raw output

### Python
1. Open the 13_healthcare_01.py file in VS Code
2. Show the 13_requirements.txt and explain they need to install that module
3. Walk through the code noting no JSON required for the SDK
4. Run the sample in VS Code
5. Walk through the output
6. Note the Python SDK is here: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics
7. Note the C# SDK is here: https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics
8. Note the Java SDK is here: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics
9. All of these can be found at this anchor: https://docs.microsoft.com/en-us/azure/cognitive-services/language-service/text-analytics-for-health/quickstart?pivots=rest-api
