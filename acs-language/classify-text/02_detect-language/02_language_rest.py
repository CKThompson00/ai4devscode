import sys
import os
from requests import get, post
from dotenv import load_dotenv
import json
import os

###############################################################################
#    API Variables
###############################################################################
# Endpoint URL
load_dotenv()
endpoint = os.environ["LANGUAGE_ENDPOINT"]
apim_key = os.environ["LANGUAGE_API_KEY"]
API_version = 'V3.1'

###############################################################################
#    Call DetectLanguage API
###############################################################################
def DetectLanguage(body):
    headers = {
        'Ocp-Apim-Subscription-Key': apim_key,
    }
    get_url = endpoint + "/text/analytics/%s/languages" % (API_version)
    resp = post(url = get_url, headers = headers, data = body)

    json = resp.json()
    if resp.status_code == 200:
        return json
    else:
        return ""

###############################################################################
#    Main
###############################################################################
def main(argv):

    ##############################
    #  Text to score
    ##############################
    body = """{
                "documents": [
                    {
                    "id": "1",
                    "text": "This is a document written in English."
                    },
                    {
                    "id": "2",
                    "text": "Bonjour tout le monde."
                    },
                    {
                    "id": "3",
                    "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."
                    }
                ]
                }
            """
    resp_json = DetectLanguage(body.encode("utf-8"))
    print(json.dumps(resp_json, indent=2))

if __name__ == '__main__':
    main(sys.argv[1:])

