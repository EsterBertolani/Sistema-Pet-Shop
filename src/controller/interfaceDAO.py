from abc import ABC, abstractmethod
from typing import List, Any


class interfaceDAO(ABC):

    @abstractmethod
    def salvar(self, objeto: Any) -> bool:
        pass

    @abstractmethod
    def atualizar(self, objeto: Any) -> bool:
        pass

    @abstractmethod
    def excluir(self, id: int) -> bool:
        pass

    @abstractmethod
    def listar_todos(self) -> List[Any]:
        pass

    @abstractmethod
    def recuperarByID(self, id: int) -> Any:
        pass

    @abstractmethod
    def tupleToObj(self, list) -> Any:
        pass
