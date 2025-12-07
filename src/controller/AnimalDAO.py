from src.conexion.mysql_queries import MySQLQueries
from src.controller.interfaceDAO import interfaceDAO
from src.model.Animal import Animal
from src.model.Especie import Especie
from typing import List, Any


class AnimalDAO(interfaceDAO):
    def __init__(self):
        self.banco = MySQLQueries()
        self.sql_base_join = """
        SELECT A.*, E.nome as nome_especie 
        FROM ANIMAL A
        INNER JOIN ESPECIE E ON A.id_especie = E.id_especie
        """

    # ================ SALVAR ================

    def salvar(self, animal: Animal) -> bool:
        try:
            id_esp = int(animal.get_especie().get_nome())
        except:
            id_esp = 1

        sql = """
        INSERT INTO ANIMAL (id_especie, nome, idade, sexo, raca, cor, porte, castrado, vacinado, adotado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            id_esp,
            animal.get_nome(),
            animal.idade,
            animal.sexo,
            animal.raca,
            animal.cor,
            animal.porte,
            animal.castrado,
            animal.vacinado,
            animal.adotado
        )
        return self.banco.execute_query(sql, values)

    # ================ ATUALIZAR ================

    def atualizar(self, animal: Animal) -> bool:
        try:
            id_esp = int(animal.get_especie().get_nome())
        except:
            id_esp = 1

        sql = """
        UPDATE ANIMAL 
        SET id_especie=%s, nome=%s, idade=%s, sexo=%s, raca=%s, cor=%s, porte=%s, castrado=%s, vacinado=%s, adotado=%s
        WHERE id_animal=%s
        """
        values = (
            id_esp,
            animal.get_nome(),
            animal.idade,
            animal.sexo,
            animal.raca,
            animal.cor,
            animal.porte,
            animal.castrado,
            animal.vacinado,
            animal.adotado,
            animal.get_id_animal()
        )
        return self.banco.execute_query(sql, values)

    # ================ EXCLUIR ================

    def excluir(self, id: int) -> bool:
        sql = "DELETE FROM ANIMAL WHERE id_animal = %s"
        values = (id,)
        return self.banco.execute_query(sql, values)

    # ================ LISTAR ================

    def listar_todos(self) -> List[Animal]:
        # Usa o SQL com JOIN definido no __init__
        return self.tupleToObj(self.banco.execute_select(self.sql_base_join))

    # ================ RECUPERAR ================

    def recuperarById(self, id: int) -> Animal | None:
        sql = f"{self.sql_base_join} WHERE A.id_animal = %s"
        values = (id,)
        lista = self.tupleToObj(self.banco.execute_select(sql, values))
        return lista[0] if lista else None

    # ================ FILTROS ================

    def filtrarSTR(self, termo_busca: str) -> List[Animal]:
        sql = f"""
        {self.sql_base_join} 
        WHERE A.nome LIKE %s OR A.raca LIKE %s OR E.nome LIKE %s
        """
        mascara = f"%{termo_busca}%"
        values = (mascara, mascara, mascara)
        return self.tupleToObj(self.banco.execute_select(sql, values))

    def filtrarINT(self, termo_busca: int) -> List[Animal]:
        sql = f"{self.sql_base_join} WHERE A.idade = %s"
        values = (termo_busca,)
        return self.tupleToObj(self.banco.execute_select(sql, values))

    def pesquisarID(self, termo_busca: str) -> List[int]:
        sql = "SELECT id_animal FROM ANIMAL WHERE nome LIKE %s"
        mascara = f"%{termo_busca}%"

        lista_tuplas = self.banco.execute_select(sql, mascara)
        lista_id = []

        for linha in lista_tuplas:
            row: Any = linha
            id_produto = int(row[0])
            lista_id.append(id_produto)

        return lista_id

    # ================ AUXILIAR ================

    def tupleToObj(self, lista_tuplas) -> List[Animal]:
        lista_objetos = []
        if not lista_tuplas:
            return []

        for linha in lista_tuplas:
            row: Any = linha
            id_especie = int(row[1])
            nome_especie = str(row[11]) if len(row) > 11 else "Desconhecido"
            obj_especie = Especie(id_especie, nome_especie)

            animal = Animal(
                id_animal=int(row[0]),
                especie=obj_especie,
                nome=str(row[2]),
                idade=int(row[3]),
                sexo=str(row[4]),
                raca=str(row[5]),
                cor=str(row[6]),
                porte=str(row[7]),
                castrado=bool(row[8]),
                vacinado=bool(row[9]),
                adotado=bool(row[10])
            )
            lista_objetos.append(animal)
        return lista_objetos
