import pymysql
from Credentials import Credenciais

def Connection_DB():
    Cred = Credenciais()
    connection = pymysql.connect(
        host = Cred.host,
        user = Cred.user,
        password = Cred.password,
        database = Cred.database,
        port = Cred.port
    )
    return connection

def Insert_Class_Date(date)->None:
    connection = Connection_DB()
    cursor =  connection.cursor()
    cursor.execute(
                   f"INSERT INTO S2024_1 (DATA, PASSOU_LISTA, ASSINEI, DISC) VALUES ('{date}', 'N', 'N', 'Ondas')"
                   )
    connection.commit()
    cursor.close()
    connection.close()

def Modify_Status(date, PASSOU_LISTA, ASSINEI)->None:
    connection = Connection_DB()
    cursor =  connection.cursor()
    cursor.execute(
                   f"UPDATE S2024_1 SET PASSOU_LISTA = '{PASSOU_LISTA}', ASSINEI = '{ASSINEI}' WHERE DATA = '{date}' AND DISC = 'Ondas'"
                   )
    connection.commit()
    cursor.close()
    connection.close()

# def Modify_Name()->None:
#     connection = Connection_DB()
#     cursor =  connection.cursor()
#     cursor.execute(
#                    f"UPDATE S2024_1 SET DISC = 'Ondas' WHERE DISC = 'ONDAS'"
#                    )
#     connection.commit()
#     cursor.close()
#     connection.close()