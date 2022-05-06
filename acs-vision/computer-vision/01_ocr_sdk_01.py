# IMPORTS
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import os
import time
import shutil
from dotenv import load_dotenv

load_dotenv()
key = os.environ["VISION_API_KEY"]

# Variables for the API Call
region = "centralus"
raw = True
numberOfCharsInOperationId = 36
reading_order = 'basic'

# Setup the Vision Client using the API Key
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(
    endpoint="https://" + region + ".api.cognitive.microsoft.com/",
    credentials=credentials
)

# Loop through the directory, call the API, save files to ~/ocr
directory = os.fsencode("/home/chthomp/documents")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    with open ('documents/' + filename, 'rb') as f:
        rawHttpResponse = client.read_in_stream(f, language="en", raw=raw, reading_order=reading_order)
        f.close()
    print(filename)
    # Get ID from returned headers
    operationLocation = rawHttpResponse.headers["Operation-Location"]
    idLocation = len(operationLocation) - numberOfCharsInOperationId
    operationId = operationLocation[idLocation:]
    print(operationId)

    # SDK call
    result = client.get_read_result(operationId)
    while result.status != OperationStatusCodes.succeeded:
        result = client.get_read_result(operationId)
        time.sleep(5)
        print(result.status)

    # Get data
    if result.status == OperationStatusCodes.succeeded:
        with open("/home/chthomp/ocr/" + filename + ".txt", "w") as f:
            for pages in result.analyze_result.read_results:
                for line in pages.lines:
                    f.write(line.text)
                    f.write("\n")
            f.close()
    shutil.move("/home/chthomp/documents/" + filename, "/home/chthomp/processed/" + filename)
