from src.utils.validador import Validador
from src.model.Especie import Especie


class Animal:
    def __init__(self, id_animal: int, especie: Especie, nome: str, idade: int, sexo: str, raca: str, cor: str, porte: str, castrado: bool, vacinado: bool, adotado=False) -> None:
        self.id_animal = id_animal
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.raca = raca
        self.cor = cor
        self.porte = porte
        self.castrado = castrado
        self.vacinado = vacinado
        self.adotado = adotado

    # GETTERS & SETTERS

    def get_id_animal(self) -> int:
        return self.id_animal

    def get_especie(self) -> Especie:
        return self.especie

    def get_nome(self) -> str:
        return self.nome

    def get_sexo(self) -> str:
        return self.sexo

    def get_raca(self) -> str:
        return self.raca

    def get_cor(self) -> str:
        return self.cor

    def get_porte(self) -> str:
        return self.porte

    def isCastrado(self) -> bool:
        return self.castrado

    def isVacinado(self) -> bool:
        return self.vacinado

    def set_nome(self, nome: str):
        self.nome = nome

    def set_sexo(self, sexo: str):
        self.sexo = sexo

    def set_raca(self, raca: str):
        self.raca = raca

    def set_cor(self, cor: str):
        self.cor = cor

    def set_porte(self, porte: str):
        self.porte = porte

    def set_castrado(self, castrado: bool):
        self.castrado = castrado

    def set_vacinado(self, vacinado: bool):
        self.vacinado = vacinado

    # OUTROS MÉTODOS

    def disponivel(self):
        return not self.adotado

    def adotar(self):
        self.adotado = True

    def __str__(self) -> str:
        larg = 60
        rodape = f"ID: {self.id_animal}".rjust(larg)

        return f"""
        ------------------------------------------------------------
        🐾 {self.nome.upper()} - {str(self.especie).upper()}
        ------------------------------------------------------------
        {'DISPONÍVEL' if self.disponivel() else 'ADOTADO'}

        Idade: {self.idade} anos | Sexo: {self.sexo.upper()}
        Raça: {self.raca} | Cor: {self.cor} | Porte: {self.porte}
        Castrado: {'Sim' if self.castrado else 'Não'} | Vacinado: {'Sim' if self.vacinado else 'Não'}
        
        {rodape}
        ------------------------------------------------------------
        """

