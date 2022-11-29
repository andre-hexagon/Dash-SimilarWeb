#importamos librerías
import mysql
import sqlalchemy


#Creamos la conexión
def query_database(query):
    #Parametros de conexion
    rds_host  =  credenciales['valor'].values[5]#a donde apuntamos
    name = credenciales['valor'].values[6] #nombre de usuario
    password = credenciales['valor'].values[7] #pswrd
    db_name = credenciales['valor'].values[8] #nombre de la base
    port = credenciales['valor'].values[9] #puerto de conexion
    
    #Estableciendo conexion
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                           .format(user=name,
                                   pw=password,
                                   db=db_name,
                                   host=rds_host))
    
   #BORRANDO DATOS PREVIOS
    connection = engine.connect()
    query = text(query)
    connection.execution_options(autocommit=True).execute(query)

    #insertando DATOS NUEVOS
    with engine.connect() as engine:
        data.to_sql('reports', con=engine, index=False,if_exists='append')
    
    return print("el archivo "+file+" se importo con exito")

