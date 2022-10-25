import sqlalchemy
import pandas as pd

HOST = ''
DATABASE = ''
USER = ''
PASSWORD = ''

class sql_connection():
    def __init__(self):
        self.engine = None
        try:
            self.engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(user=USER,
                                                                                            pw=PASSWORD,
                                                                                            db=DATABASE,
                                                                                            host=HOST)
                                                    )
            self.connection = self.engine.connect()

        except:
            print("Error while connectingengine to SQL")

    def exec_query(self, query_str):
        return self.connection.execute(sqlalchemy.sql.text(query_str))

    def query_to_df(self, query_result):
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
#SQL = sql_connection()
#query = SQL.exec_query("SELECT * FROM table")
#df = query_to_df(query)
#####