from typing import List
from sparse_matrix import SparseMatrix

class MatrizCSR(SparseMatrix):
    """
    Implementación del Formato Comprimido por Fila (CSR).
    Responsable: Integrante 2
    """
    
    def __init__(self, n_filas: int, m_columnas: int):
        super().__init__(n_filas, m_columnas)
        self.valores: List[int] = []
        self.columnas: List[int] = []
        # cfilas siempre tiene tamaño n + 1. Inicialmente apunta todo a 0.
        self.cfilas: List[int] = [0] * (n_filas + 1)

    def obtener_elemento(self, i: int, j: int) -> int:
        # TODO: Usar cfilas[i] y cfilas[i+1] para delimitar la búsqueda en self.columnas
        return 0

    def obtener_fila(self, i: int) -> List[int]:
        # TODO: Reconstruir la fila usando el rango definido por cfilas.
        return []

    def obtener_columna(self, j: int) -> List[int]:
        # TODO: Iterar sobre toda la estructura para encontrar elementos de la columna j.
        return []

    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        # TODO: Insertar valor y actualizar cfilas (esto es lo más complejo).
        pass

    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':
        # TODO: Implementar suma.
        return MatrizCSR(self.n, self.m)

    def transpuesta(self) -> 'SparseMatrix':
        # TODO: Implementar transpuesta.
        return MatrizCSR(self.m, self.n)
