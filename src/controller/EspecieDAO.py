from src.conexion.mysql_queries import MySQLQueries
from src.controller.interfaceDAO import interfaceDAO
from src.model.Especie import Especie
from typing import List, Any


class EspecieDAO(interfaceDAO):
    def __init__(self):
        self.banco = MySQLQueries()

    def salvar(self, especie: Especie) -> bool:
        sql = "INSERT INTO ESPECIE (nome) VALUES (%s)"
        val = (especie.get_nome(),)
        return self.banco.execute_query(sql, val)

    def atualizar(self, especie: Especie) -> bool:
        sql = "UPDATE ESPECIE SET nome = %s WHERE id_especie = %s"
        val = (especie.get_nome(), especie.get_id_especie())
        return self.banco.execute_query(sql, val)

    def excluir(self, id: int) -> bool:
        sql = "DELETE FROM ESPECIE WHERE id_especie = %s"
        return self.banco.execute_query(sql, (id,))

    def listar_todos(self) -> List[Especie]:
        sql = "SELECT * FROM ESPECIE"
        lista_tuplas = self.banco.execute_select(sql)
        return self.tupleToObj(lista_tuplas)

    def recuperarById(self, id: int) -> Especie | None:
        sql = "SELECT * FROM ESPECIE WHERE id_especie = %s"
        lista = self.tupleToObj(self.banco.execute_select(sql, (id,)))
        return lista[0] if lista else None

    def pesquisarID(self, termo: str) -> List[int]:
        sql = "SELECT id_especie FROM ESPECIE WHERE nome LIKE %s"
        mascara = f"%{termo}%"

        lista_tuplas = self.banco.execute_select(sql, mascara)
        lista_id = []

        for linha in lista_tuplas:
            row: Any = linha
            id_produto = int(row[0])
            lista_id.append(id_produto)

        return lista_id

    def tupleToObj(self, lista_tuplas) -> List[Especie]:
        lista = []
        if not lista_tuplas:
            return []
        for row in lista_tuplas:
            especie = Especie(int(row[0]), str(row[1]))
            lista.append(especie)
        return lista
