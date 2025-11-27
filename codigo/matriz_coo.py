from typing import List
from sparse_matrix import SparseMatrix

class MatrizCOO(SparseMatrix):
    """
    Implementación del Formato Coordenado (COO).
    Almacena solo los elementos no cero con sus coordenadas.
    """
    
    def __init__(self, n_filas: int, m_columnas: int):
        super().__init__(n_filas, m_columnas)
        # Vectores para almacenar los datos
        self.valores: List[int] = []    # Almacena los valores no cero
        self.filas: List[int] = []      # Almacena los índices de fila
        self.columnas: List[int] = []   # Almacena los índices de columna

    def obtener_elemento(self, i: int, j: int) -> int:
        """
        Busca un elemento en la posición (i, j).
        Si no existe en nuestros vectores, retorna 0.
        
        Explicación detallada:
        1. Verificamos si hay elementos almacenados
        2. Recorremos todos los elementos buscando coincidencia en fila y columna
        3. Si encontramos, retornamos el valor
        4. Si no encontramos, retornamos 0 (porque en matrices dispersas, lo que no está almacenado es 0)
        """
        if len(self.filas) == 0:
            return 0

        # Buscamos en todos los elementos almacenados
        for k in range(len(self.filas)):
            if self.filas[k] == i and self.columnas[k] == j:
                return self.valores[k]
        return 0

    def obtener_fila(self, i: int) -> List[int]:
        """ 
        Obtiene TODA la fila i, incluyendo ceros.
        
        Explicación detallada:
        1. Verificamos que la fila sea válida
        2. Creamos una fila llena de ceros (por defecto todo es cero)
        3. Buscamos todos los elementos que están en la fila i
        4. Colocamos esos valores en sus columnas correspondientes
        """
        if i < 0 or i >= self.n:
            return []
        
        # Creamos una fila de ceros
        fila_completa = [0] * self.m
        
        # Buscamos elementos en esta fila
        for k in range(len(self.filas)):
            if self.filas[k] == i:
                columna = self.columnas[k]
                if columna < self.m:  # Verificamos que la columna sea válida
                    fila_completa[columna] = self.valores[k]
        
        return fila_completa

    def obtener_columna(self, j: int) -> List[int]:
        """
        Obtiene TODA la columna j, incluyendo ceros.
        
        Explicación detallada:
        1. Verificamos que la columna sea válida
        2. Creamos una columna llena de ceros
        3. Buscamos todos los elementos que están en la columna j
        4. Colocamos esos valores en sus filas correspondientes
        """
        if j < 0 or j >= self.m:
            return []
        
        # Creamos una columna de ceros
        columna_completa = [0] * self.n
        
        # Buscamos elementos en esta columna
        for k in range(len(self.columnas)):
            if self.columnas[k] == j:
                fila = self.filas[k]
                if fila < self.n:  # Verificamos que la fila sea válida
                    columna_completa[fila] = self.valores[k]
        
        return columna_completa

    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        """
        Modifica o inserta un elemento en la posición (i, j).
        
        Explicación detallada:
        1. Verificamos si la posición ya existe
        2. Si existe, actualizamos el valor
        3. Si no existe, agregamos nuevo elemento
        4. Si el elemento es 0, podríamos eliminarlo (pero en esta implementación no lo hacemos)
        """
        # Verificamos índices
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            raise ValueError(f"Posición ({i}, {j}) fuera de rango")
        
        # Buscamos si ya existe esta posición
        for k in range(len(self.filas)):
            if self.filas[k] == i and self.columnas[k] == j:
                if elemento == 0:
                    # Eliminamos el elemento si lo estamos poniendo en 0
                    self.valores.pop(k)
                    self.filas.pop(k)
                    self.columnas.pop(k)
                else:
                    # Actualizamos el valor
                    self.valores[k] = elemento
                return
        
        # Si no existe y el elemento no es cero, lo agregamos
        if elemento != 0:
            self.valores.append(elemento)
            self.filas.append(i)
            self.columnas.append(j)

    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':
        """
        Suma dos matrices dispersas.
        
        Explicación detallada:
        1. Verificamos que las dimensiones coincidan
        2. Creamos nueva matriz resultado
        3. Recorremos todos los elementos de AMBAS matrices
        4. Sumamos elemento por elemento
        5. Usamos un diccionario temporal para evitar duplicados
        """
        if self.n != otra_matriz.n or self.m != otra_matriz.m:
            raise ValueError("Las matrices no tienen las mismas dimensiones")
        
        # Creamos nueva matriz para el resultado
        resultado = MatrizCOO(self.n, self.m)
        
        # Usamos un diccionario para acumular las sumas
        suma_dict = {}
        
        # Sumamos elementos de esta matriz
        for k in range(len(self.filas)):
            i, j = self.filas[k], self.columnas[k]
            clave = (i, j)
            suma_dict[clave] = self.valores[k]
        
        # Sumamos elementos de la otra matriz
        for i in range(otra_matriz.n):
            for j in range(otra_matriz.m):
                valor_otra = otra_matriz.obtener_elemento(i, j)
                if valor_otra != 0:
                    clave = (i, j)
                    if clave in suma_dict:
                        suma_dict[clave] += valor_otra
                    else:
                        suma_dict[clave] = valor_otra
        
        # Agregamos los resultados a la nueva matriz
        for (i, j), valor in suma_dict.items():
            if valor != 0:  # Solo agregamos si no es cero
                resultado.modificar_posicion(i, j, valor)
        
        return resultado

    def transpuesta(self) -> 'SparseMatrix':
        """
        Calcula la transpuesta de la matriz.
        
        Explicación detallada:
        La transpuesta intercambia filas por columnas.
        En COO, esto significa intercambiar los vectores de filas y columnas.
        """
        # Creamos nueva matriz con dimensiones intercambiadas
        transpuesta = MatrizCOO(self.m, self.n)
        
        # Copiamos los datos intercambiando filas y columnas
        transpuesta.valores = self.valores.copy()
        transpuesta.filas = self.columnas.copy()    # Las columnas originales son las filas de la transpuesta
        transpuesta.columnas = self.filas.copy()    # Las filas originales son las columnas de la transpuesta
        
        return transpuesta

    @classmethod
    def crear_desde_matriz(cls, matriz_completa: List[List[int]]) -> 'SparseMatrix':
        """
        Crea una matriz COO a partir de una matriz completa.
        
        Explicación detallada:
        1. Obtenemos dimensiones de la matriz original
        2. Creamos instancia de MatrizCOO
        3. Recorremos TODA la matriz buscando elementos no cero
        4. Para cada elemento no cero, lo agregamos a los vectores
        """
        if not matriz_completa or not matriz_completa[0]:
            raise ValueError("La matriz no puede estar vacía")
        
        n = len(matriz_completa)
        m = len(matriz_completa[0])
        
        # Creamos la instancia
        matriz_coo = cls(n, m)
        
        # Recorremos la matriz completa
        for i in range(n):
            for j in range(m):
                valor = matriz_completa[i][j]
                if valor != 0:
                    # Agregamos el elemento no cero
                    matriz_coo.valores.append(valor)
                    matriz_coo.filas.append(i)
                    matriz_coo.columnas.append(j)
        
        return matriz_coo

    def __repr__(self):
        """Representación legible de la matriz COO"""
        elementos = []
        for i, j, v in zip(self.filas, self.columnas, self.valores):
            elementos.append(f"({i},{j}):{v}")
        return f"MatrizCOO({self.n}x{self.m}) - Elementos: {', '.join(elementos)}"