import mysql.connector
from mysql.connector import errorcode

config = {
    'user':'pr_user',
    'password':'Poptart1',
    'host':'165.227.61.245',
    'database':'patient_register'
    }

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print("err")
else:
    cnx.close()