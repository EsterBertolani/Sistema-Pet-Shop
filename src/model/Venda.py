from datetime import datetime
from src.model.Pessoa import Pessoa
from src.model.Produto import Produto
from src.model.ItemVenda import ItemVenda
from typing import List


class Venda:

    def __init__(self, id_venda: int, comprador: Pessoa, data_venda: datetime | None = None, valor_total: float = 0.0, itens: List[ItemVenda] | None = None) -> None:
        self.id_venda = id_venda
        self.comprador = comprador
        self.data_venda = data_venda if data_venda else datetime.now()
        self.valor_total = valor_total
        self.itens = itens if itens else []

    # GETTERS & SETTERS
    def get_id_venda(self) -> int:
        return self.id_venda

    def get_data(self) -> datetime:
        return self.data_venda

    def get_valor_total(self) -> float:
        return self.valor_total

    def get_comprador(self) -> Pessoa:
        return self.comprador

    def get_itens(self) -> List[ItemVenda]:
        return self.itens

    def adicionar_item(self, produto: Produto, qtd: int):
        id_item_temp = len(self.itens) + 1
        novo_item = ItemVenda(id_item_temp, produto, qtd, self)
        self.itens.append(novo_item)
        self.valor_total += novo_item.get_subtotal()

    # NOTINHA FISCAL
    def __str__(self) -> str:
        data_formatada = self.data_venda.strftime('%d/%m/%Y às %H:%M')

        texto = f"""
        ==================================================
                        COMPROVANTE DE VENDA
        ==================================================
        ID: {self.id_venda}  |  Data: {data_formatada}
        Comprador: {self.comprador.get_nome()}
        CPF: {self.comprador.get_cpf()}
        --------------------------------------------------
        ITENS COMPRADOS:
        """
        for item in self.itens:
            texto += f"\n        {item}"

        texto += f"""
        
        --------------------------------------------------
        TOTAL A PAGAR: R$ {self.valor_total:.2f}
        ==================================================
        """
        return texto
