from src.conexion.mysql_queries import MySQLQueries
from src.controller.interfaceDAO import interfaceDAO
from src.model.Pessoa import Pessoa
from typing import List, Any


class PessoaDAO(interfaceDAO):
    def __init__(self):
        self.banco = MySQLQueries()

    # ================ SALVAR ================
    def salvar(self, pessoa: Pessoa) -> bool:
        sql = """
        INSERT INTO PESSOA (nome, cpf, telefone, email) 
        VALUES (%s, %s, %s, %s);
        """
        values = (
            pessoa.get_nome(),
            pessoa.get_cpf(),
            pessoa.get_telefone(),
            pessoa.get_email()
        )
        return self.banco.execute_query(sql, values)

    # ================ ATUALIZAR ================
    def atualizar(self, pessoa: Pessoa) -> bool:
        sql = """
        UPDATE PESSOA 
        SET nome = %s, cpf = %s, telefone = %s, email = %s 
        WHERE id_pessoa = %s
        """
        values = (
            pessoa.get_nome(),
            pessoa.get_cpf(),
            pessoa.get_telefone(),
            pessoa.get_email(),
            pessoa.get_id_pessoa()
        )
        return self.banco.execute_query(sql, values)

    # ================ EXCLUIR ================
    def excluir(self, id: int) -> bool:
        sql = "DELETE FROM PESSOA WHERE id_pessoa = %s;"
        values = (id,)
        return self.banco.execute_query(sql, values)

    # ================ LISTAR ================
    def listar_todos(self) -> List[Pessoa]:
        sql = "SELECT * FROM PESSOA"
        lista_tuplas = self.banco.execute_select(sql)
        return self.tupleToObj(lista_tuplas)

    # ================ RECUPERAR POR ID ================
    def recuperarById(self, id: int) -> Pessoa | None:
        sql = "SELECT * FROM PESSOA WHERE id_pessoa = %s"
        values = (id,)
        lista_tuplas = self.banco.execute_select(sql, values)

        if not lista_tuplas:
            return None

        objetos = self.tupleToObj(lista_tuplas)
        return objetos[0]

    # ================ FILTRAR (Texto) ================
    def filtrar(self, termo_busca: str) -> List[Pessoa]:
        """Filtra por Nome, Email ou CPF"""
        sql = """
        SELECT * FROM PESSOA 
        WHERE nome LIKE %s OR email LIKE %s OR cpf LIKE %s
        """
        mascara = f"%{termo_busca}%"
        values = (mascara, mascara, mascara)

        lista_tuplas = self.banco.execute_select(sql, values)
        return self.tupleToObj(lista_tuplas)

    def pesquisarID(self, termo_busca: str) -> List[int]:
        sql = "SELECT id_pessoa FROM PESSOA WHERE nome LIKE %s"
        mascara = f"%{termo_busca}%"
        values = (mascara,)

        lista_tuplas = self.banco.execute_select(sql, values)
        lista_id = []

        for linha in lista_tuplas:
            row: Any = linha
            id_produto = int(row[0])
            lista_id.append(id_produto)

        return lista_id

    # ================ AUXILIAR ================
    def tupleToObj(self, lista_tuplas) -> List[Pessoa]:
        lista_objetos = []
        if not lista_tuplas:
            return []

        for row in lista_tuplas:
            pessoa = Pessoa(
                id_pessoa=int(row[0]),
                nome=str(row[1]),
                cpf=str(row[2]),
                telefone=str(row[3]),
                email=str(row[4])
            )
            lista_objetos.append(pessoa)
        return lista_objetos
