from src.utils.validador import Validador


class Especie:

    def __init__(self, nome) -> None:
        if not Validador.isEmpty(nome):
            raise ValueError("O nome não pode ser vazio!")
        else:
            self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"
