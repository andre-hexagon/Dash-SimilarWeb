import mysql.connector
import pandas as pd
import credenciales

HOST = credenciales.HOST
DATABASE = credenciales.DATABASE
USER = credenciales.USER
PASSWORD = credenciales.PASSWORD

class sql_connection():
    def __init__(self):
        self.cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
        
    def exec_query(self, query_str):
        cursor = self.cnx.cursor()
        cursor.execute(query_str)

        df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
        # for col in df.columns[df.dtypes==object]:
        #     df[col]=df[col].apply(lambda x: str(x).encode('iso8859-1').decode('utf-8','ignore'))

        return df
#####
# USE CASE
#####
# SQL = sql_connection(USER, PASSWORD, HOST, DATABASE)
# query_str = "SELECT * FROM table LIMIT 100"
# df = SQL.query_to_df(query_str)
#####