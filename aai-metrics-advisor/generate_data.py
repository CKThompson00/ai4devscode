##########################################################################
#                         IMPORTS
##########################################################################
import os
import sys
import random
from dotenv import load_dotenv
import pyodbc 
from faker import Faker
import datetime

##########################################################################
#                         VARIABLES
##########################################################################

load_dotenv()
sql_server = os.environ["SQL_SERVER"]
sql_database = os.environ["SQL_SERVER_DB"]
sql_user = os.environ["SQL_SERVER_DB_LOGIN"]
sql_password = os.environ["SQL_SERVER_DB_PASSWORD"]

##########################################################################
#                                MAIN
##########################################################################
def main():
   
    print("Data Generation Starting")
    generateData()
    print("Data Generation Complete")

##########################################################################
#                                MAIN
##########################################################################
def generateData():

    faker = Faker()

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+sql_server+';DATABASE='+sql_database+';UID='+sql_user+';PWD='+ sql_password)
    cursor = cnxn.cursor()
    TOTAL_SECONDS = 60 # 1 minute
    start_date = datetime.datetime(2022, 4, 27, 22, 42, 1)
    
    series = faker.time_series(start_date=start_date, end_date='+3d', precision=TOTAL_SECONDS)

    for val in series:
        print(val[0])

        timestamp = val[0]
        anomaly = False

        if random.random() >= 0.95:
            anomaly = True
        
        ################################
        #  DB TPS
        ################################
        server = 'SERVER01'
        metric = 'TransactionsPerSecond'
        database = 'DB1'
        if anomaly:
            value = generateRandom(3000, 5000, 0)
        else:
            value = generateRandom(1, 1000, 0)
        generateDBMetric(cursor, server, metric, value, database, timestamp)

        database = 'DB2'
        if anomaly:
            value = generateRandom(200, 500, 0)
        else:
            value = generateRandom(1, 100, 0)
        generateDBMetric(cursor, server, metric, value, database, timestamp)

        ################################
        #  CPU
        ################################
        metric = 'CPU'
        if anomaly:
            value = generateRandom(80, 100, 3)
        else:
            value = generateRandom(1, 50, 3)
        generateInfraMetric(cursor, server, metric, value, timestamp)

        ################################
        #  OS Disk LatencyP
        ################################
        metric = 'AvgDiskSecPerRead'
        if anomaly:
            value = generateRandom(0.040, 0.500, 3)
        else:
            value = generateRandom(0.001, 0.010, 3)
        generateInfraMetric(cursor, server, metric, value, timestamp)
        
        cnxn.commit()

    cursor.close()
    cnxn.close()

##########################################################################
#                                
##########################################################################
def generateRandom(low, high, rounddec):
    return round(random.uniform(low,high),rounddec)

##########################################################################
#                                
##########################################################################
def generateInfraMetric(cursor, server, metric, value, timestamp):
    sql = """\
    EXEC InsertInfraMetric @server=?,@metric=?,@value=?,@timestamp=?
    """        
    params = (server, metric, value, timestamp)
    cursor.execute(sql, params)

##########################################################################
#                                
##########################################################################
def generateDBMetric(cursor, server, metric, value, database, timestamp):

    sql = """\
    EXEC InsertDBMetric @server=?,@metric=?,@value=?,@database=?,@timestamp=?
    """        
    params = (server, metric, value, database, timestamp)
    cursor.execute(sql, params)

if __name__ == '__main__':
    main()

