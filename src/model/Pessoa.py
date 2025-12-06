from src.utils.validador import Validador

class Pessoa:
    def __init__(self, id_pessoa, nome, cpf, telefone, email) -> None:
        self.id_pessoa = id_pessoa

        if not Validador.isEmpty(nome):
            raise ValueError("O nome não pode ser vazio!")
        else:
            self.nome = nome

        if Validador.validarCpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError(f"CPF inválido: {cpf}")
        
        if Validador.validarTel(telefone):
            self.telefone = telefone
        else:
            raise ValueError(f"Telefone inválido: {telefone}")

        if Validador.validarEmail(email):
            self.email = email
        else:
            raise ValueError(f"E-mail inválido: {email}")

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
