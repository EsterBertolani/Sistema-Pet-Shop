import mysql.connector
from src.utils.config import db_config


class MySQLQueries:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(**db_config)
            self.cursor = self.cnx.cursor()
            print("Conexão estabelecida com sucesso!")

        except mysql.connector.Error as err:
            print(f"Erro ao conectar com o banco de dados: {err}")

    def execute_select(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()

        except mysql.connector.Error as err:
            print(f"Erro ao consultar: {err}")
            return []
        
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.cnx.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao executar: {err}")

    def close(self):
        self.cursor.close()
        self.cnx.close()
        print("Encerrando conexão...")
