from src.conexion.mysql_queries import MySQLQueries
from src.model.Animal import Animal
banco = MySQLQueries()

resultado = banco.execute_select("SELECT * FROM ANIMAL")

print("\n--- LISTA DE ANIMAIS ---")
for animal in resultado:
    print(animal)
