########### Python Form Recognizer Async Analyze #############
import pyodbc 
import json
import time
import getopt
import sys
import os
from requests import get, post
import uuid

###############################################################################
#    API Variables
###############################################################################
# Endpoint URL
endpoint = os.environ["COGSVC_ENDPOINT_MP"]
# Subscription Key
apim_key = os.environ["COGSVC_APIM_KEY_MP"]
# API version
API_version = os.environ["COGSVC_VERSION"]
API_version = 'V3.1'

###############################################################################
#    Call Sentiment API with opinionMining=true;
#        body = JSON document to score
###############################################################################
def GetSentiment(body):
    headers = {
        'Ocp-Apim-Subscription-Key': apim_key,
    }
    params = {
        "opinionMining": "true"
    }
    get_url = endpoint + "/text/analytics/%s/sentiment" % (API_version)
    resp = post(url = get_url, headers = headers, params = params, data = body)

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
                    "id": "DOCID",
                    "text": "TEXT",
                    "language": "en"
                    }
                ]
                }
            """
    index = 1
    with open("Restaurant_Reviews.tsv") as file:
        content = file.readlines()
    for line in content:
        json = body.replace('TEXT', line.split('\t')[0])
        json = json.replace("DOCID", str(index))
        resp_json = GetSentiment(json)
        if resp_json != "":
            print(line.split('\t')[0])
            writeToSql(resp_json)
        else:

            print("Skipping")
        index += 1

###############################################################################
#
#    writeToSql(fr_custom_results, fr_analyze_results, pdf_file, model_id)
#
###############################################################################
def writeToSql(resp_json):

    ###########################################################################
    #  Connection to SQL 
    ###########################################################################
    server = os.environ["AI4DEVS_SQL_SERVER"] 
    database = os.environ["AI4DEVS_SQL_SERVER_DB"]
    username = os.environ["AI4DEVS_SQL_SERVER_DB_USER"]
    password = os.environ["AI4DEVS_SQL_SERVER_DB_USER_PASSWORD"]

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    ###########################################################################
    #  Process the document
    ###########################################################################
    # print(json.dumps(resp_json))
    documents = resp_json['documents']

    document_index = 0
    for document in documents:
        # print(document['confidenceScores'])
        print("Document", document['id'], document['sentiment'], sep = " - ")
        ##################################
        #  INSERT DOCUMENT
        ##################################
        sql = """\
        EXEC InsertDocument @document_id=?,@sentiment=?,@positive_score=?,@neutral_score=?,@negative_score=?
        """        
        params = (document['id'], document['sentiment'], document['confidenceScores']['positive'], document['confidenceScores']['neutral'], document['confidenceScores']['negative'])
        cursor.execute(sql, params)
        document_id = cursor.fetchone()[0]

        ##################################
        #  INSERT SENTENCES
        ##################################
        sentence_index = 0
        for sentence in document['sentences']:
            # print('===================================')
            # print("Sentence", sentence['text'], sentence['sentiment'], sep = " - ")
            sql = """\
            EXEC InsertSentence @document_id=?,@sentiment=?,@sentence_text=?,@positive_score=?,@neutral_score=?,@negative_score=?
            """        
            params = (document_id, sentence['sentiment'], sentence['text'], sentence['confidenceScores']['positive'], sentence['confidenceScores']['neutral'], sentence['confidenceScores']['negative'])
            cursor.execute(sql, params)
            sentence_id = cursor.fetchone()[0]

            ##################################
            #  INSERT TARGETS
            ##################################
            target_index = 0
            for target in sentence['targets']:
                # print(doc_id, sent_id, targ_id, sep=" ")
                # print("Target", target['text'], target['sentiment'], sep = " - ")

                sql = """\
                EXEC InsertTarget @sentence_id=?,@sentiment=?,@target_text=?,@positive_score=?,@negative_score=?
                """        
                params = (sentence_id, target['sentiment'], target['text'], target['confidenceScores']['positive'], target['confidenceScores']['negative'])
                cursor.execute(sql, params)
                target_id = cursor.fetchone()[0]

                ##################################
                #  INSERT ASSESSMENTS
                ##################################
                relation_id = ""
                for relation in target['relations']:
                    if relation['relationType'] == 'assessment':
                        relation_id = relation['ref']

                assessment_index = 0
                for assessment in sentence['assessments']:
                    if relation_id == "#/documents/" + str(document_index) + "/sentences/" + str(sentence_index) + "/assessments/" + str(assessment_index):
                        sql = """\
                        EXEC InsertAssessment @target_id=?,@sentiment=?,@assessment_text=?,@positive_score=?,@negative_score=?,@is_negated=?
                        """        
                        params = (target_id, assessment['sentiment'], assessment['text'], assessment['confidenceScores']['positive'], assessment['confidenceScores']['negative'], assessment['isNegated'])
                        cursor.execute(sql, params)
                    assessment_index += 1
                target_index += 1
            sentence_index += 1
        document_index += 1

    print('********************************************')

    cnxn.commit()

if __name__ == '__main__':
    main(sys.argv[1:])

