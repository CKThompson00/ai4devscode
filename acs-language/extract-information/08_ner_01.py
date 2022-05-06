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
def entity_recognition_example(client):

    try:
        documents = ["I had a wonderful trip to Seattle last week."]
        result = client.recognize_entities(documents = documents)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\tLength: \t", entity.length, "\tOffset: \t", entity.offset, "\n")

    except Exception as err:
        print("Encountered exception. {}".format(err))
        
##########################################################################
#                         CALL FUNCTION
##########################################################################
entity_recognition_example(client)
