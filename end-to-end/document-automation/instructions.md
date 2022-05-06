# Demo Instructions for Document Automation

This demo will walk through an end to end document process automation scenario.

1. A document will be dropped into a storage account
2. A Logic App will pick up the file
3. The file will be sent to a an Image Classifier to determine document type
4. Once determined it is then sent to the approriate form recognizer API to extract name value pairs
5. The name value pairs are stored in a Cosmos DB
6. Cognitive Search is enabled to Index the files from Cosmos

## Assets
1. Storage Account
2. Logic App
3. Form Recognizer Endpoint
4. Custom Vision Inference Endpoint and project
5. Cosmos DB
6. Cognitive Search

## Setup

