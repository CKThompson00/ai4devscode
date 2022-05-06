########################################################
#                         Imports
########################################################
import os.path
from pprint import pprint
import time
from io import BytesIO
from random import random
import uuid

from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
import azure.cognitiveservices.vision.contentmoderator.models
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

########################################################
#                     Variables
########################################################
load_dotenv()
endpoint = os.environ["COGSVC_ENDPOINT_CM"]
subscription_key = os.environ["COGSVC_API_KEY_CM"]

########################################################
#                Create Client Creds
########################################################
client = ContentModeratorClient(
    endpoint=endpoint,
    credentials=CognitiveServicesCredentials(subscription_key)
)

TEXT_FOLDER = os.path.join(os.path.dirname(
    os.path.realpath(__file__)))

########################################################
# Create list
########################################################
print("\nCreating list")
custom_list = client.list_management_term_lists.create(
    content_type="application/json",
    body={
        "name": "Term list name",
        "description": "Term list description",
    }
)
print("List created:")
pprint(custom_list.as_dict())
list_id = custom_list.id

########################################################
# Update list details
########################################################
print("\nUpdating details for list {}".format(list_id))
updated_list = client.list_management_term_lists.update(
    list_id=list_id,
    content_type="application/json",
    body={
        "name": "New name",
        "description": "New description"
    }
)
pprint(updated_list.as_dict())

########################################################
# Add terms
########################################################
print("\nAdding terms to list {}".format(list_id))
client.list_management_term.add_term(
    list_id=list_id,
    term="term1",
    language="eng"
)
client.list_management_term.add_term(
    list_id=list_id,
    term="term2",
    language="eng"
)

########################################################
# Get all terms ids
########################################################
print("\nGetting all term IDs for list {}".format(list_id))
terms = client.list_management_term.get_all_terms(
    list_id=list_id, language="eng")
terms_data = terms.data
pprint(terms_data.as_dict())

########################################################
# Refresh the index
########################################################
print("\nRefreshing the search index for list {}".format(list_id))
refresh_index = client.list_management_term_lists.refresh_index_method(
    list_id=list_id, language="eng")
pprint(refresh_index.as_dict())

# LATENCY_DELAY = 1
# print("\nWaiting {} minutes to allow the server time to propagate the index changes.".format(
#     LATENCY_DELAY))
# time.sleep(LATENCY_DELAY * 60)

########################################################
# Screen text
########################################################
with open(os.path.join(TEXT_FOLDER, 'content_moderator_term_list.txt'), "rb") as text_fd:
    screen = client.text_moderation.screen_text(
        text_content_type="text/plain",
        text_content=text_fd,
        language="eng",
        autocorrect=False,
        pii=False,
        list_id=list_id
    )
    pprint(screen.as_dict())

########################################################
# Delete list
########################################################
print("\nDelete the term list {}".format(list_id))
client.list_management_term_lists.delete(list_id=list_id)