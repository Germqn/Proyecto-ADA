from typing import List
from sparse_matrix import SparseMatrix

class MatrizCOO(SparseMatrix):
    """
    Implementación del Formato Coordenado (COO).
    Responsable: Integrante 1
    """
    
    def __init__(self, n_filas: int, m_columnas: int):
        super().__init__(n_filas, m_columnas)
        # Vectores para almacenar los datos
        self.valores: List[int] = []
        self.filas: List[int] = []
        self.columnas: List[int] = []

    def obtener_elemento(self, i: int, j: int) -> int:
        # TODO: Implementar búsqueda. 
        # Sugerencia: Iterar sobre self.filas y self.columnas para encontrar coincidencia.
        return 0

    def obtener_fila(self, i: int) -> List[int]:
        # TODO: Construir la fila completa.
        return []

    def obtener_columna(self, j: int) -> List[int]:
        # TODO: Construir la columna completa.
        return []

    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        # TODO: Insertar o actualizar el valor en los 3 vectores.
        pass

    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':
        # TODO: Implementar suma.
        return MatrizCOO(self.n, self.m)

    def transpuesta(self) -> 'SparseMatrix':
        # TODO: Implementar transpuesta.
        return MatrizCOO(self.m, self.n)

    @classmethod
    def crear_desde_matriz(cls, matriz_completa: List[List[int]]) -> 'SparseMatrix':
        # TODO: Implementar la creación desde una matriz completa (Punto 1a)
        # 1. Leer dimensiones (n, m)
        # 2. Crear instancia
        # 3. Recorrer matriz_completa y usar modificar_posicion para los no ceros.
        return cls(len(matriz_completa), len(matriz_completa[0]))
