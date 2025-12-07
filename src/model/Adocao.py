from datetime import datetime
from src.model.Animal import Animal
from src.model.Pessoa import Pessoa


class Adocao:
    def __init__(self, id_adocao: int, animal: Animal, adotante: Pessoa, data_adocao: datetime | None = None) -> None:
        self.id_adocao = id_adocao
        self.data_adocao = data_adocao if data_adocao else datetime.now()
        self.animal = animal
        self.adotante = adotante

    def get_id_adocao(self) -> int:
        return self.id_adocao

    def get_data(self) -> datetime:
        return self.data_adocao
    
    def get_animal_adotado(self) -> Animal:
        return self.animal
    
    def get_adotante(self) -> Pessoa:
        return self.adotante


    def __str__(self) -> str:
        # Formata a data para ficar bonita (Dia/Mês/Ano Hora:Minuto)
        data_format = self.data_adocao.strftime('%d/%m/%Y às %H:%M')
        
        texto = f"""
        ===================================================
                        COMPROVANTE DE ADOCÃO
        ===================================================
        ID: {self.id_adocao}
        Data: {data_format}
        Cliente: {self.adotante.get_nome()} | CPF: {self.adotante.get_cpf()}
        ---------------------------------------------------
        ANIMAL ADOTADO: 

        {self.animal}

        ---------------------------------------------------
        O amor verdadeiro tem 4 patas e um coração gigante!
        ===================================================
        """
        
        return texto