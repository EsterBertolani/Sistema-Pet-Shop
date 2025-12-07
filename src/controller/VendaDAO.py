from src.conexion.mysql_queries import MySQLQueries
from src.controller.interfaceDAO import interfaceDAO
from src.model.Venda import Venda
from src.model.ItemVenda import ItemVenda
from src.model.Pessoa import Pessoa
from src.model.Produto import Produto
from typing import List, Any
from datetime import datetime


class VendaDAO(interfaceDAO):
    def __init__(self):
        self.banco = MySQLQueries()

    # ================ SALVAR ================

    def salvar(self, venda: Venda) -> bool:
        sql_venda = """
        INSERT INTO VENDA (data_venda, valor_total, id_pessoa)
        VALUES (%s, %s, %s)
        """
        val_venda = (
            venda.get_data(),
            venda.get_valor_total(),
            venda.get_comprador().get_id_pessoa()
        )

        id_venda_gerado = self.banco.execute_insert(sql_venda, val_venda)

        if not id_venda_gerado:
            return False

        sql_item = """
        INSERT INTO ITEM_VENDA (id_venda, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
        """

        for item in venda.get_itens():
            val_item = (
                id_venda_gerado,
                item.get_produto().get_id_produto(),
                item.get_qtd(),
                item.get_preco_unit()
            )
            self.banco.execute_query(sql_item, val_item)

            # produtoDAO.baixar_estoque()

        return True

    # ================ ATUALIZAR ================

    def atualizar(self, venda: Venda) -> bool:
        sql = "UPDATE VENDA SET valor_total = %s WHERE id_venda = %s"
        val = (venda.get_valor_total(), venda.get_id_venda())
        return self.banco.execute_query(sql, val)

    # ================ EXCLUIR ================

    def excluir(self, id: int) -> bool:
        # O banco deve ter CASCADE, se não precisa apagar os itens antes
        sql = "DELETE FROM VENDA WHERE id_venda = %s"
        return self.banco.execute_query(sql, (id,))

    # ================ LISTAR ================

    def listar_todos(self) -> List[Venda]:
        sql = """
        SELECT V.id_venda, V.data_venda, V.valor_total, P.id_pessoa, P.nome, P.cpf, P.telefone, P.email 
        FROM VENDA V
        INNER JOIN PESSOA P ON V.id_pessoa = P.id_pessoa
        ORDER BY V.data_venda DESC
        """
        lista_tuplas = self.banco.execute_select(sql)
        return self.tupleToObj(lista_tuplas)

    # ================ RECUPERAR ================
    
    def recuperarById(self, id: int) -> Venda | None:
        sql = """
        SELECT V.id_venda, V.data_venda, V.valor_total, P.id_pessoa, P.nome, P.cpf, P.telefone, P.email 
        FROM VENDA V
        INNER JOIN PESSOA P ON V.id_pessoa = P.id_pessoa
        WHERE V.id_venda = %s
        """
        lista = self.tupleToObj(self.banco.execute_select(sql, (id,)))
        return lista[0] if lista else None

    # ================ MÉTODOS AUXILIARES ================

    def _carregar_itens(self, venda: Venda):
        """
        Busca os itens dessa venda específica no banco e popula a lista da venda.
        """
        sql = """
        SELECT I.id_item, I.quantidade, I.preco_unitario, 
               P.id_produto, P.nome, P.descricao, P.preco, P.estoque
        FROM ITEM_VENDA I
        INNER JOIN PRODUTO P ON I.id_produto = P.id_produto
        WHERE I.id_venda = %s
        """
        resultados = self.banco.execute_select(sql, (venda.get_id_venda(),))

        for row in resultados:
            row: Any
            prod = Produto(int(row[3]), str(row[4]), str(
                row[5]), float(row[6]), int(row[7]))

            item = ItemVenda(int(row[0]), prod, int(row[1]), venda)

            venda.get_itens().append(item)

    def tupleToObj(self, lista_tuplas) -> List[Venda]:
        lista_vendas = []
        if not lista_tuplas:
            return []

        for row in lista_tuplas:
            row: Any

            comprador = Pessoa(int(row[3]), str(row[4]), str(
                row[5]), str(row[6]), str(row[7]))

            data_venda = row[1]
            if isinstance(data_venda, str):
                data_venda = datetime.strptime(data_venda, '%Y-%m-%d %H:%M:%S')

            venda = Venda(
                id_venda=int(row[0]),
                comprador=comprador,
                data_venda=data_venda,
                valor_total=float(row[2])
            )

            self._carregar_itens(venda)

            lista_vendas.append(venda)

        return lista_vendas
