from src.conexion.mysql_queries import MySQLQueries
from src.model.Animal import Animal
from src.model.Especie import Especie
from typing import List, Any


class AnimalDAO:
    def __init__(self):
        self.banco = MySQLQueries()

    def salvar(self, animal: Animal) -> bool:
        # ATENÇÃO: Aqui assumo que animal.get_especie() tem um ID ou você tem esse ID.
        # Se sua classe Especie não tem ID, você terá que passar o id_especie separado.
        sql = """
        INSERT INTO ANIMAL (id_especie, nome, idade, sexo, raca, cor, porte, castrado, vacinado, adotado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Ajuste aqui conforme sua classe Especie (se tem get_id() ou não)
        id_especie = 1  # <--- MUDE ISSO para animal.get_especie().get_id()

        val = (id_especie, animal.get_nome(), animal.idade, animal.sexo,
               animal.raca, animal.cor, animal.porte,
               animal.castrado, animal.vacinado, animal.adotado)

        return self.banco.execute_query(sql, val)

    def listar_todos(self) -> List[Animal]:
        # Aquele SQL com JOIN que fizemos antes
        sql = """
        SELECT A.*, E.nome as nome_especie 
        FROM ANIMAL A
        INNER JOIN ESPECIE E ON A.id_especie = E.id_especie
        """
        tuplas = self.banco.execute_select(sql)
        # Lógica de conversão igual à que fizemos no teste.py
        # ... (implementar loop de conversão aqui)
        return []  # Retorne a lista preenchida
