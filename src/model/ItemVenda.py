from src.model.Produto import Produto
from typing import Any


class ItemVenda:

    def __init__(self, id_item: int, produto: Produto, qtd: int, venda: Any = None) -> None:
        self.id_item = id_item
        self.produto = produto
        self.qtd = qtd
        self.preco_unit = produto.get_preco()
        self.subtotal = self.qtd * self.preco_unit
        self.venda = venda

    # GETTERS
    def get_id_item(self) -> int:
        return self.id_item

    def get_produto(self) -> Produto:
        return self.produto

    def get_qtd(self) -> int:
        return self.qtd

    def get_preco_unit(self) -> float:
        return self.preco_unit

    def get_subtotal(self) -> float:
        return self.subtotal

    def get_venda(self) -> Any:
        return self.venda

    def set_qtd(self, nova_qtd: int):
        self.qtd = nova_qtd
        self.subtotal = self.qtd * self.preco_unit

    def __str__(self) -> str:
        return f"{self.qtd}x {self.produto.get_nome()} (R$ {self.preco_unit:.2f}) = R$ {self.subtotal:.2f}"
