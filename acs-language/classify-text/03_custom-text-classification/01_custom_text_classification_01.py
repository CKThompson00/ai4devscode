import sys
import os
from requests import get, post
import time
import os
from dotenv import load_dotenv

###############################################################################
#    API Variables
###############################################################################
# Endpoint URL
load_dotenv()
endpoint = os.environ["LANGUAGE_ENDPOINT"]
apim_key = os.environ["LANGUAGE_API_KEY"]
API_version = 'v3.2-preview.2'

###############################################################################
#    Call DetectLanguage API
###############################################################################
def Classify(body):
    headers = {
        'Ocp-Apim-Subscription-Key': apim_key,
    }
    get_url = endpoint + "/text/analytics/%s/analyze" % (API_version)
    resp = post(url = get_url, headers = headers, data = body)

    if resp.status_code == 202:
        oploc = resp.headers["Operation-Location"]
        while (resp.status_code != 200):
            time.sleep(5)
            resp = get(url = oploc, headers = headers)
        return resp.json()
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
            "tasks": {
            "customMultiClassificationTasks": [
            {
                "parameters": {
                    "project-name": "MovieGenres",
                    "deployment-name": "prod"
                }
            }
        ]
        },
        "displayName": "CustomTextPortal_multiClassification",
        "analysisInput": {
            "documents": [
                {
                    "id": "1",
                    "text": "The mining town of Cedar City, Utah, is ruled by Mr. Walthrope, a polygamous Mormon prophet , his son the marshall  and their band of ruffians. John Brad  is falsely accused of shooting in the back a gunfighter sent against him by the prophet and has to flee. Meanwhile, a train brings Jeff Groghan , a gunfighter called by Walthrope, and two Transylvanian immigrants, Traian  and Romulus Brad , who come to meet their brother John. Traian speaks only Romanian and Romulus tries to get by with his dictionary. On the station, Grogham is received with a gunfight and Traian has occasion to fire his Turkish gun, booty from the siege of Plevna. Upon arrival to the saloon, Traian is invited to play poker with Groghan, a former Confederate officer still in grey uniform and another man. Traian manages to win many dollars and Bob , the slave of the Confederate officer. The fun is interrupted by the arrival of the prophet. With very limited command of English, the Brads inform that they are looking for John, whose face they see in Wanted posters. They are judged by the inicuous drunkard Dolittle  who sentences them to hanging but the prophet takes them to his farm, where they toil as farm hands. The Brads and Bob escape and live in a hut under the Romanian flag where they fish and find gold nuggets. John tries to organize the miners against the prophet who sets the prices and takes their gold away to Salt Lake City, but the miners prefer to let the things as they are. Later, Walthrope's men assault one man and his daughter that is rescued by John Brad. John and the girl finally reach the Brads' hut. They team together to stop the party that carries the miners' gold stolen by the Mormons. In the ensuing gunfight, the Brads win and successfully defend the miners camp against the whole Walthrope band. Walthrope is captured and the Brads, Bob and the girl ride in the sunset.",
                    "language": "en"
                }
            ]
        }
    }"""
    print("Should be classified as Comedy")
    resp_json = Classify(body.encode("utf-8"))
    tasks = resp_json["tasks"]
    cmct = tasks["customMultiClassificationTasks"][0]
    for document in cmct["results"]["documents"]:
        for classification in document["classifications"]:
            print("Category: \t\t", classification["category"])
            print("Confidence Score: \t", classification["confidenceScore"])

if __name__ == '__main__':
    main(sys.argv[1:])

