from src.conexion.mysql_queries import MySQLQueries
from src.model.Animal import Animal
from src.model.Especie import Especie
from typing import Any

banco = MySQLQueries()
resultado = banco.execute_select("SELECT * FROM ANIMAL")

print("\n--- LISTA DE ANIMAIS ---")

for linha in resultado:
    row: Any = linha

    id_especie_do_banco = str(row[10])

    obj_especie_provisorio = Especie(id_especie_do_banco)

    novo_animal = Animal(
        id_animal=int(row[0]),
        especie=obj_especie_provisorio,

        nome=str(row[1]),
        idade=int(row[2]),
        sexo=str(row[3]),
        raca=str(row[4]),
        cor=str(row[5]),
        porte=str(row[6]),

        castrado=bool(row[7]),
        vacinado=bool(row[8]),
        adotado=bool(row[9])
    )

    print(novo_animal)
