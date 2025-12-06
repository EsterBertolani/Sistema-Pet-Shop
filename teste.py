from src.conexion.mysql_queries import MySQLQueries

banco = MySQLQueries()

resultado = banco.execute_select("SELECT * FROM ANIMAL")

print("\n--- LISTA DE ANIMAIS ---")
for animal in resultado:
    print(animal)
