from abc import ABC, abstractmethod
from typing import List, Tuple, Union

class SparseMatrix(ABC):
    """
    Clase abstracta que define la interfaz común para todas las representaciones de matrices dispersas.
    Todos los integrantes deben respetar estos nombres de métodos.
    """
    
    def __init__(self, n_filas: int, m_columnas: int):
        self.n = n_filas  # Número de filas
        self.m = m_columnas  # Número de columnas

    @abstractmethod
    def obtener_elemento(self, i: int, j: int) -> int:
        """
        Retorna el valor en la posición (i, j).
        Si no está almacenado, debe retornar 0.
        """
        pass

    @abstractmethod
    def obtener_fila(self, i: int) -> List[int]:
        """
        Retorna una lista con todos los elementos de la fila i (incluyendo ceros).
        """
        pass

    @abstractmethod
    def obtener_columna(self, j: int) -> List[int]:
        """
        Retorna una lista con todos los elementos de la columna j (incluyendo ceros).
        """
        pass

    @abstractmethod
    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        """
        Asigna el valor 'elemento' a la posición (i, j).
        Debe manejar la inserción si no existe, o actualización si ya existe.
        """
        pass

    @abstractmethod
    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':
        """
        Retorna una NUEVA matriz con el resultado de la suma de self + otra_matriz.
        """
        pass

    @abstractmethod
    def transpuesta(self) -> 'SparseMatrix':
        """
        Retorna una NUEVA matriz que es la transpuesta de self.
        """
        pass

    @classmethod
    @abstractmethod
    def crear_desde_matriz(cls, matriz_completa: List[List[int]]) -> 'SparseMatrix':
        """
        Punto 1 del Proyecto: Función para generar representación.
        Recibe una matriz completa (lista de listas) y retorna la instancia de la matriz dispersa.
        """
        pass
    
    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.n}x{self.m})>"
