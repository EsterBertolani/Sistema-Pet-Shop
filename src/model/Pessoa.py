from src.utils.validador import Validador


class Pessoa:
    def __init__(self, id_pessoa: int, nome: str, cpf: str, telefone: str, email: str) -> None:
        self.id_pessoa = id_pessoa
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    # GETTERS & SETTERS

    def get_id_pessoa(self) -> int:
        return self.id_pessoa

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def set_telefone(self, telefone: str):
        self.telefone = telefone

    def get_telefone(self) -> str:
        return self.telefone

    def set_email(self, email: str):
        self.email = email

    def get_email(self) -> str:
        return self.email

    # OUTROS MÉTODOS

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}\nTelefone: {self.telefone} | E-mail: {self.email}"
