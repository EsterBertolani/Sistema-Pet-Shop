from src.utils.validador import Validador


class Especie:

    def __init__(self, id_especie: int, nome: str) -> None:
        self.id_especie = id_especie
        self.nome = nome

    def get_id_especie(self) -> int:
        return self.id_especie

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"
