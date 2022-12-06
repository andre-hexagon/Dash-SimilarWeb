import mysql.connector
import pandas as pd
import creds_sql

HOST = creds_sql.HOST
DATABASE = creds_sql.DATABASE
USER = creds_sql.USER
PASSWORD = creds_sql.PASSWORD

class sql_connection():
    def __init__(self, user, pswd, host, db):
        self.cnx = cnx = mysql.connector.connect(user=user, password=pswd, host=host, database=db, charset='latin1')
        
    def exec_query(self, query_str):
        cursor = self.cnx.cursor()
        cursor.execute(query_str)

        df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
        for col in df.columns[df.dtypes==object]:
            df[col]=df[col].apply(lambda x: x.encode('latin1').decode())

        return df
#####
# USE CASE
#####
#SQL = sql_connection(USER, PASSWORD, HOST, DATABASE)
#query_str = "SELECT * FROM table LIMIT 100"
#df = SQL.query_to_df(query_str)
#####