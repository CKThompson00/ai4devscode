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
#   Screen the input text: check for profanity,
#           do autocorrect text, and check for personally identifying
#           information (PII)
########################################################
with open(os.path.join(TEXT_FOLDER, 'content_moderator_text_moderation.txt'), "rb") as text_fd:
    screen = client.text_moderation.screen_text(
        text_content_type="text/plain",
        text_content=text_fd,
        language="eng",
        autocorrect=True,
        pii=True
    )

    pprint(screen.as_dict())
