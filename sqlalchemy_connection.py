import sqlalchemy
import pandas as pd

HOST = ''
DATABASE = ''
USER = ''
PASSWORD = ''
class sql_connection():
    def __init__(self, user, pswd, host, db):
        self.engine = sqlalchemy.create_engine(f"mysql+pymysql://{user}:{pswd}@{host}/{db}")
        
    def exec_query(self, query_str):
        with self.engine.connect() as connection:
            return connection.execute(sqlalchemy.sql.text(query_str))

    def query_to_df(self, query_str):
        query_result = self.exec_query(query_str)
        df = pd.DataFrame(query_result.fetchall())
        if len(df) > 0:
            df.columns = query_result.keys()
        else:
            columns = query_result.keys()
            df = pd.DataFrame(columns=columns)
        return df


#####
# USE CASE
#####
#SQL = sql_connection(USER, PASSWORD, HOST, DATABASE)
#query_str = "SELECT * FROM table LIMIT 100"
#df = SQL.query_to_df(query_str)
#####