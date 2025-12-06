class Pessoa:
    def __init__(self, id_pessoa: int = None, nome: str = None, cpf: str = None, telefone: str = None, email: str = None) -> None:
        self.set_id_pessoa(id_pessoa)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_email(email)

    def set_id_pessoa(self, id_pessoa: int):
        self.id_pessoa = id_pessoa

    def get_id_pessoa(self) -> int:
        return self.id_pessoa

    def set_nome(self, nome: str):
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def set_cpf(self, cpf: str):
        self.cpf = cpf

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

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}\nTelefone: {self.telefone} | E-mail: {self.email}"
