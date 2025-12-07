from src.conexion.mysql_queries import MySQLQueries
from src.controller.interfaceDAO import interfaceDAO
from src.model.Produto import Produto
from typing import List, Any


class ProdutoDAO(interfaceDAO):
    def __init__(self):
        self.banco = MySQLQueries()

    # ================ SALVAR ================

    def salvar(self, produto: Produto) -> bool:
        sql = """
        INSERT INTO PRODUTO (nome, descricao, preco, estoque) 
        VALUES (%s, %s, %s, %s);
        """
        values = (
            produto.get_nome(),
            produto.get_descricao(),
            produto.get_preco(),
            produto.get_estoque()
        )

        return self.banco.execute_query(sql, values)

    # ================ ATUALIZAR ================

    def atualizar(self, produto: Produto) -> bool:
        sql = """
        UPDATE PRODUTO 
        SET nome = %s, descricao = %s, preco = %s, estoque = %s 
        WHERE id_produto = %s
        """
        values = (
            produto.get_nome(),
            produto.get_descricao(),
            produto.get_preco(),
            produto.get_estoque(),
            produto.get_id_produto()
        )

        return self.banco.execute_query(sql, values)

    # ================ EXCLUIR ================

    def excluir(self, id: int) -> bool:
        sql = """
        DELETE FROM PRODUTO WHERE id_produto = %s;
        """
        values = (id,)

        return self.banco.execute_query(sql, values)

    # ================ LISTAR ================

    def listarTodos(self) -> List[Produto]:
        """
        Retorna todos os produtos
        """
        sql = "SELECT * FROM PRODUTO"
        lista_tuplas = self.banco.execute_select(sql)
        return self.tupleToObj(lista_tuplas)

    # ==========================================

    def filtrarSTR(self, termo_busca: str) -> List[Produto]:
        """
        Filtra por nome ou descrição
        """
        sql = """
        SELECT * FROM PRODUTO 
        WHERE nome LIKE %s OR descricao LIKE %s
        """

        mascara = f"%{termo_busca}%"
        values = (mascara, mascara)

        lista_tuplas = self.banco.execute_select(sql, values)
        return self.tupleToObj(lista_tuplas)

    # ==========================================

    def filtrarINT(self, termo_busca: float | int) -> List[Produto]:
        """
        Filtra por preço ou estoque
        """
        sql = """
        SELECT * FROM PRODUTO 
        WHERE preco = %s OR estoque = %s
        """

        mascara = f"{termo_busca}%"
        values = (mascara, mascara)

        lista_tuplas = self.banco.execute_select(sql, values)
        return self.tupleToObj(lista_tuplas)

    # ==========================================

    def pesquisarID(self, termo_busca: str) -> List[int]:
        """
        Retorna apenas o ID do produto
        """
        sql = """
        SELECT id_produto FROM PRODUTO 
        WHERE nome LIKE %s OR descricao LIKE %s
        """
        mascara = f"%{termo_busca}%"
        values = (mascara, mascara)

        lista_tuplas = self.banco.execute_select(sql, values)

        lista_id = []

        for linha in lista_tuplas:
            row: Any = linha
            id_produto = int(row[0])
            lista_id.append(id_produto)

        return lista_id

        # return [int(linha[0]) for linha in lista_tuplas]

    # ==========================================

    def recuperarById(self, id: int) -> Produto | None:
        sql = "SELECT * FROM PRODUTO WHERE id_produto = %s"
        values = (id,)

        lista_tuplas = self.banco.execute_select(sql, values)

        if not lista_tuplas:
            return None

        lista_objetos = self.tupleToObj(lista_tuplas)

        return lista_objetos[0]

    # -------- método aux --------

    def tupleToObj(self, lista_tuplas) -> List[Produto]:
        lista_objetos = []

        if not lista_tuplas:
            return []

        for linha in lista_tuplas:
            row: Any = linha
            produto = Produto(
                id_produto=int(row[0]),
                nome=str(row[1]),
                descricao=str(row[2]),
                preco=float(row[3]),
                estoque=int(row[4])
            )
            lista_objetos.append(produto)

        return lista_objetos
