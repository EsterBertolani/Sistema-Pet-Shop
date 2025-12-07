from src.conexion.mysql_queries import MySQLQueries
from src.controller.interfaceDAO import interfaceDAO
from src.model.Adocao import Adocao
from src.model.Pessoa import Pessoa
from src.model.Animal import Animal
# Necessário para recriar o Animal completo
from src.model.Especie import Especie
from typing import List, Any
from datetime import datetime


class AdocaoDAO(interfaceDAO):
    def __init__(self):
        self.banco = MySQLQueries()

    def salvar(self, adocao: Adocao) -> bool:
        sql = """
        INSERT INTO ADOCAO (data, id_animal, id_pessoa)
        VALUES (%s, %s, %s)
        """
        val = (
            adocao.get_data(),
            adocao.get_animal_adotado().get_id_animal(),
            adocao.get_adotante().get_id_pessoa()
        )
        return self.banco.execute_query(sql, val)

    def atualizar(self, adocao: Adocao) -> Any:
        # Geralmente não se atualiza adoção (se errou, exclui e faz outra)
        pass

    def excluir(self, id: int) -> bool:
        sql = "DELETE FROM ADOCAO WHERE id_adocao = %s"
        return self.banco.execute_query(sql, (id,))

    def listar_todos(self) -> List[Adocao]:
        # JOIN triplo: Adocao -> Pessoa E Adocao -> Animal (que tem JOIN com Especie)
        # É uma query grande, mas necessária para ter o objeto completo
        sql = """
        SELECT 
            AD.id_adocao, AD.data, 
            P.id_pessoa, P.nome, P.cpf, P.telefone, P.email,
            A.id_animal, A.nome, A.idade, A.sexo, A.raca, A.cor, A.porte, A.castrado, A.vacinado, A.adotado,
            E.nome as nome_especie
        FROM ADOCAO AD
        INNER JOIN PESSOA P ON AD.id_pessoa = P.id_pessoa
        INNER JOIN ANIMAL A ON AD.id_animal = A.id_animal
        INNER JOIN ESPECIE E ON A.id_especie = E.id_especie
        """
        return self.tupleToObj(self.banco.execute_select(sql))

    def recuperar_por_id(self, id: int) -> Adocao | None:
        # Copiar a mesma query do listar_todos e adicionar WHERE
        sql = """
        SELECT 
            AD.id_adocao, AD.data, 
            P.id_pessoa, P.nome, P.cpf, P.telefone, P.email,
            A.id_animal, A.nome, A.idade, A.sexo, A.raca, A.cor, A.porte, A.castrado, A.vacinado, A.adotado,
            E.nome as nome_especie
        FROM ADOCAO AD
        INNER JOIN PESSOA P ON AD.id_pessoa = P.id_pessoa
        INNER JOIN ANIMAL A ON AD.id_animal = A.id_animal
        INNER JOIN ESPECIE E ON A.id_especie = E.id_especie
        WHERE AD.id_adocao = %s
        """
        lista = self.tupleToObj(self.banco.execute_select(sql, (id,)))
        return lista[0] if lista else None

    def tupleToObj(self, lista_tuplas) -> List[Adocao]:
        lista = []
        if not lista_tuplas:
            return []

        for row in lista_tuplas:
            # Mapeamento manual dos índices (trabalhoso mas necessário)
            # 0=id_adocao, 1=data
            # 2..6 = Pessoa
            # 7..16 = Animal
            # 17 = Nome Especie

            adotante = Pessoa(int(row[2]), str(row[3]), str(
                row[4]), str(row[5]), str(row[6]))

            obj_especie = Especie(str(row[17]))
            animal = Animal(
                id_animal=int(row[7]), especie=obj_especie, nome=str(row[8]),
                idade=int(row[9]), sexo=str(row[10]), raca=str(row[11]),
                cor=str(row[12]), porte=str(row[13]),
                castrado=bool(row[14]), vacinado=bool(row[15]), adotado=bool(row[16])
            )

            adocao = Adocao(
                id_adocao=int(row[0]),
                data_adocao=row[1],
                animal=animal,
                adotante=adotante
            )
            lista.append(adocao)
        return lista

    # Métodos obrigatórios vazios
    def filtrarSTR(self, t): return []
    def filtrarINT(self, t): return []
    def pesquisarID(self, t): return []
