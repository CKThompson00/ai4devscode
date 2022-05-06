##########################################################################
#                         VARIABLES
##########################################################################
import os
from dotenv import load_dotenv

load_dotenv()
endpoint = os.environ["COGSVC_ENDPOINT_MP"]
key = os.environ["COGSVC_API_KEY_MP"]

##########################################################################
#                         IMPORTS
##########################################################################
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

##########################################################################
#                         CREDENTIALS/AUTHN
##########################################################################
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

##########################################################################
#                         FUNCTION TO CALL SDK
##########################################################################
def pii_recognition_example(client):
    documents = [
        "The employee's SSN is 859-98-0987.",
        "The employee's phone number is 555-555-5555."
    ]
    response = client.recognize_pii_entities(documents, language="en")
    result = [doc for doc in response if not doc.is_error]
    for doc in result:
        print("Redacted Text: {}".format(doc.redacted_text))
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("\tCategory: {}".format(entity.category))
            print("\tConfidence Score: {}".format(entity.confidence_score))
            print("\tOffset: {}".format(entity.offset))
            print("\tLength: {}".format(entity.length))
        
##########################################################################
#                         CALL FUNCTION
##########################################################################
pii_recognition_example(client)
