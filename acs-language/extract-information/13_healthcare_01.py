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
def health_example(client):
    documents = [
        """
        Patient needs to take 50 mg of ibuprofen.
        """
    ]

    poller = client.begin_analyze_healthcare_entities(documents)
    result = poller.result()

    docs = [doc for doc in result if not doc.is_error]

    for idx, doc in enumerate(docs):
        for entity in doc.entities:
            print("Entity: {}".format(entity.text))
            print("...Normalized Text: {}".format(entity.normalized_text))
            print("...Category: {}".format(entity.category))
            print("...Subcategory: {}".format(entity.subcategory))
            print("...Offset: {}".format(entity.offset))
            print("...Confidence score: {}".format(entity.confidence_score))
        for relation in doc.entity_relations:
            print("Relation of type: {} has the following roles".format(relation.relation_type))
            for role in relation.roles:
                print("...Role '{}' with entity '{}'".format(role.name, role.entity.text))
        print("------------------------------------------")

##########################################################################
#                         CALL FUNCTION
##########################################################################

health_example(client)
