from typing import List
from sparse_matrix import SparseMatrix

class MatrizCSR(SparseMatrix):

    def __init__(self, n_filas: int, m_columnas: int):
        super().__init__(n_filas, m_columnas)
        self.valores: List[int] = []
        self.columnas: List[int] = []
        self.cfilas: List[int] = [0] * (n_filas + 1)

    # -------------------------------------------------------------
    # Obtener un elemento (i, j)
    # -------------------------------------------------------------
    def obtener_elemento(self, i: int, j: int) -> int:
        inicio = self.cfilas[i]
        fin = self.cfilas[i + 1]

        for idx in range(inicio, fin):
            if self.columnas[idx] == j:
                return self.valores[idx]

        return 0

    # -------------------------------------------------------------
    # Obtener una fila completa como lista normal (con ceros)
    # -------------------------------------------------------------
    def obtener_fila(self, i: int) -> List[int]:
        fila = [0] * self.m
        inicio = self.cfilas[i]
        fin = self.cfilas[i + 1]

        for idx in range(inicio, fin):
            col = self.columnas[idx]
            fila[col] = self.valores[idx]

        return fila

    # -------------------------------------------------------------
    # Obtener una columna completa como lista normal (con ceros)
    # -------------------------------------------------------------
    def obtener_columna(self, j: int) -> List[int]:
        columna = [0] * self.n

        for i in range(self.n):
            inicio = self.cfilas[i]
            fin = self.cfilas[i + 1]

            for idx in range(inicio, fin):
                if self.columnas[idx] == j:
                    columna[i] = self.valores[idx]
                    break

        return columna

    # -------------------------------------------------------------
    # Modificar una posición (insertar, actualizar o eliminar)
    # -------------------------------------------------------------
    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        inicio = self.cfilas[i]
        fin = self.cfilas[i + 1]

        # Buscar si ya existe
        for idx in range(inicio, fin):
            if self.columnas[idx] == j:
                # Si es 0, eliminar el valor
                if elemento == 0:
                    self.valores.pop(idx)
                    self.columnas.pop(idx)

                    for k in range(i + 1, len(self.cfilas)):
                        self.cfilas[k] -= 1
                else:
                    self.valores[idx] = elemento
                return

        # Si no existía y es 0 → nada que insertar
        if elemento == 0:
            return

        # Insertar en la posición ordenada
        pos = inicio
        while pos < fin and self.columnas[pos] < j:
            pos += 1

        # Insertar valores
        self.valores.insert(pos, elemento)
        self.columnas.insert(pos, j)

        # Actualizar cfilas
        for k in range(i + 1, len(self.cfilas)):
            self.cfilas[k] += 1

    # -------------------------------------------------------------
    # Suma de matrices CSR
    # -------------------------------------------------------------
    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':
        if self.n != otra_matriz.n or self.m != otra_matriz.m:
            raise ValueError("Las matrices deben tener el mismo tamaño.")

        resultado = MatrizCSR(self.n, self.m)

        for i in range(self.n):
            fila_self = self.obtener_fila(i)
            fila_otro = otra_matriz.obtener_fila(i)

            for j in range(self.m):
                suma = fila_self[j] + fila_otro[j]
                if suma != 0:
                    resultado.modificar_posicion(i, j, suma)

        return resultado

    # -------------------------------------------------------------
    # Transpuesta (CSR → CSC pero devolvemos CSR para mantener compatibilidad)
    # -------------------------------------------------------------
    def transpuesta(self) -> 'SparseMatrix':
        matriz_t = MatrizCSR(self.m, self.n)

        for i in range(self.n):
            inicio = self.cfilas[i]
            fin = self.cfilas[i + 1]

            for idx in range(inicio, fin):
                val = self.valores[idx]
                col = self.columnas[idx]

                matriz_t.modificar_posicion(col, i, val)

        return matriz_t

    # -------------------------------------------------------------
    # Crear desde matriz completa
    # -------------------------------------------------------------
    @classmethod
    def crear_desde_matriz(cls, matriz_completa: List[List[int]]) -> 'SparseMatrix':
        n = len(matriz_completa)
        m = len(matriz_completa[0])
        matriz = cls(n, m)

        for i in range(n):
            for j in range(m):
                if matriz_completa[i][j] != 0:
                    matriz.modificar_posicion(i, j, matriz_completa[i][j])

        return matriz
