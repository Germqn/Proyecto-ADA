from typing import List
from sparse_matrix import SparseMatrix

class MatrizCSC(SparseMatrix):
    """
    Implementación del Formato Comprimido por Columna (CSC).
    Responsable: Integrante 3 - German Mejia
    """
    
    def __init__(self, n_filas: int, m_columnas: int):
        super().__init__(n_filas, m_columnas)
        self.valores: List[int] = []
        self.filas: List[int] = []
        # ccolumnas siempre tiene tamaño m + 1. Inicialmente apunta todo a 0.
        self.ccolumnas: List[int] = [0] * (m_columnas + 1)

    def obtener_elemento(self, i: int, j: int) -> int:
        # TODO: Usar ccolumnas[j] y ccolumnas[j+1] para delimitar la búsqueda en self.filas
        return 0

    def obtener_fila(self, i: int) -> List[int]:
        # TODO: Iterar sobre toda la estructura para encontrar elementos de la fila i.
        return []

    def obtener_columna(self, j: int) -> List[int]:
        # TODO: Reconstruir la columna usando el rango definido por ccolumnas.
        return []

    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        # TODO: Insertar valor y actualizar ccolumnas.
        pass

    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':
        # TODO: Implementar suma.
        return MatrizCSC(self.n, self.m)

    def transpuesta(self) -> 'SparseMatrix':
        # TODO: Implementar transpuesta.
        return MatrizCSC(self.m, self.n)

    @classmethod
    def crear_desde_matriz(cls, matriz_completa: List[List[int]]) -> 'SparseMatrix':
        # TODO: Implementar la creación desde una matriz completa (Punto 1b)
        return cls(len(matriz_completa), len(matriz_completa[0]))
