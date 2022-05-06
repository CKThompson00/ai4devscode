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
def key_phrase_extraction_example(client):

    try:
        documents = ["My cat might need to see a veterinarian."]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        
##########################################################################
#                         CALL FUNCTION
##########################################################################
key_phrase_extraction_example(client)