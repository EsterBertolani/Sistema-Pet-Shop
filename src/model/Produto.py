class Produto:

    def __init__(self, id_produto: int, nome: str, descricao: str, preco: float, estoque: int) -> None:
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    # GETTERS & SETTERS
    def get_id_produto(self) -> int:
        return self.id_produto

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_descricao(self) -> str:
        return self.descricao

    def set_descricao(self, descricao: str):
        self.descricao = descricao

    def get_preco(self) -> float:
        return self.preco

    def set_preco(self, preco: float):
        self.preco = preco

    def get_estoque(self) -> int:
        return self.estoque

    def set_estoque(self, estoque: int):
        self.estoque = estoque


    # OUTROS MÉTODOS

    def baixarEstoque(self, qtd: int) -> int:
        if (qtd <= self.estoque):
            self.estoque -= qtd
            return self.estoque
        else:
            return -1
        
    def __str__(self) -> str:
        larg = 50
        rodape = f"Estoque: {self.estoque} | ID: {self.id_produto}".rjust(larg)
        
        return f"""
        📦 {self.nome.upper()}
        --------------------------------------------------
        {self.descricao}
        
        PREÇO: R$ {self.preco:.2f}
        
        {rodape}
        --------------------------------------------------
        """
