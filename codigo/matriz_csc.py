from typing import List
from sparse_matrix import SparseMatrix

class MatrizCSC(SparseMatrix):
    
    def __init__(self, n_filas: int, m_columnas: int):
        super().__init__(n_filas, m_columnas)
        self.valores: List[int] = []
        self.filas: List[int] = []
        # ccolumnas siempre tiene tamaño m + 1. Inicialmente apunta todo a 0.
        self.ccolumnas: List[int] = [0] * (m_columnas + 1)

    def obtener_elemento(self, i: int, j: int) -> int:
        if len(self.valores) == 0:
            return 0
        
        for k in range(self.ccolumnas[j], self.ccolumnas[j+1]):
            if self.filas[k] == i:
                return self.valores[k]
        return 0

    def obtener_fila(self, i: int) -> List[int]:
        if len(self.valores) == 0:
            return [0] * self.m
        #Crear una fila llena de ceros
        fila_resultado = [0] * self.m
        
        #Recorremos todas las columnas para encontrar los elementos de la fila i
        for j in range(self.m):
            # Se busca en la columna j actual
            for k in range(self.ccolumnas[j], self.ccolumnas[j+1]):
                # Si el elemento es de la fila i, se agrega a la fila resultado
                if self.filas[k] == i:
                    fila_resultado[j] = self.valores[k]
                    break
        return fila_resultado

    def obtener_columna(self, j: int) -> List[int]:
        if len(self.valores) == 0:
            return [0] * self.n
        
        columna_resultado = [0] * self.n
        
        for k in range(self.ccolumnas[j], self.ccolumnas[j+1]):
            columna_resultado[self.filas[k]] = self.valores[k]
        return columna_resultado

    def modificar_posicion(self, i: int, j: int, elemento: int) -> None:
        # 1. Buscar si ya existe el valor en esa posición
        rango_inicio = self.ccolumnas[j]
        rango_fin = self.ccolumnas[j+1]
        
        for k in range(rango_inicio, rango_fin):
            if self.filas[k] == i:
                # Caso 1: Ya existe.
                if elemento != 0:
                    self.valores[k] = elemento
                else:
                    self.valores.pop(k)
                    self.filas.pop(k)
                    # Restamos 1 a los punteros siguientes porque quitamos un elemento
                    for col in range(j + 1, self.m + 1):
                        self.ccolumnas[col] -= 1
                return

        # 2. Caso 2: No existe. Si es 0, no hacemos nada.
        if elemento == 0:
            return

        # 3. Insertar nuevo valor
        # Buscamos la posición correcta dentro de la columna para mantener las filas ordenadas
        pos_insertar = rango_inicio
        while pos_insertar < rango_fin and self.filas[pos_insertar] < i:
            pos_insertar += 1
        
        self.valores.insert(pos_insertar, elemento)
        self.filas.insert(pos_insertar, i)
        
        # 4. Se actualizan los punteros de todas las columnas siguientes
        # Como se ingreso un dato nuevo, las siguientes columnas se desplazan a la derecha
        for col in range(j + 1, self.m + 1):
            self.ccolumnas[col] += 1

    def sumar(self, otra_matriz: 'SparseMatrix') -> 'SparseMatrix':

        # 1. Se crea una nueva matriz la cual será el resultado de la suma
        nueva = MatrizCSC(self.n, self.m)
        
        # Listas temporales para construir la nueva matriz
        nuevos_valores = []
        nuevas_filas = []
        nuevos_ccolumnas = [0] # Empieza en 0
        
        # 2. Se recorre COLUMNA por COLUMNA (j desde 0 hasta m)
        for j in range(self.m):
            # Se obtienen los rangos de la columna j para 'self'
            p1 = self.ccolumnas[j]
            fin1 = self.ccolumnas[j+1]  
            
            # Se obtienen los rangos de la columna j para 'otra_matriz'
            p2 = otra_matriz.ccolumnas[j]
            fin2 = otra_matriz.ccolumnas[j+1]
            
            # 3. While para mezclar (Merge)
            while p1 < fin1 and p2 < fin2:
                fila1 = self.filas[p1]
                fila2 = otra_matriz.filas[p2]
                
                if fila1 < fila2:
                    # Se agregan a los vectores nuevos
                    nuevos_valores.append(self.valores[p1])
                    nuevas_filas.append(fila1)
                    p1 += 1
                elif fila2 < fila1:
                    # Se agregan a los vectores nuevos
                    nuevos_valores.append(otra_matriz.valores[p2])
                    nuevas_filas.append(fila2)
                    p2 += 1
                else:
                    # Empate (Sumar)
                    suma = self.valores[p1] + otra_matriz.valores[p2]
                    if suma != 0:
                        # Se agregan a los vectores nuevos
                        nuevos_valores.append(suma)
                        nuevas_filas.append(fila1)
                    p1 += 1
                    p2 += 1
            
            # 4. Vaciar los que sobraron (si p1 o p2 no llegaron al final)
            while p1 < fin1:
                fila1 = self.filas[p1]
                nuevos_valores.append(self.valores[p1])
                nuevas_filas.append(fila1)
                p1 += 1
            
            while p2 < fin2:
                fila2 = otra_matriz.filas[p2]
                nuevos_valores.append(otra_matriz.valores[p2])
                nuevas_filas.append(fila2)
                p2 += 1
            
            # 5. Actualizar puntero de columna
            nuevos_ccolumnas.append(len(nuevos_valores))
            
        # 6. Asignar las listas construidas a la matriz 'nueva'
        nueva.valores = nuevos_valores
        nueva.filas = nuevas_filas
        nueva.ccolumnas = nuevos_ccolumnas
        
        return nueva

    def transpuesta(self) -> 'SparseMatrix':
        # La transpuesta de una matriz NxM es una matriz MxN
        nueva = MatrizCSC(self.m, self.n)
        
        # 1. Contar cuántos elementos hay en cada fila de la original
        # (Porque las filas de la original serán las COLUMNAS de la nueva)
        conteo_por_fila = [0] * self.n
        for fila in self.filas:
            conteo_por_fila[fila] += 1
            
        # 2. Construir el vector ccolumnas de la nueva matriz (Acumulado)
        nueva.ccolumnas = [0] * (self.n + 1)
        for i in range(self.n):
            nueva.ccolumnas[i+1] = nueva.ccolumnas[i] + conteo_por_fila[i]
            
        # 3. Rellenar valores y filas
        # Necesitamos un puntero auxiliar para saber dónde escribir en cada columna nueva
        posicion_actual = list(nueva.ccolumnas) 
        
        nueva.valores = [0] * len(self.valores)
        nueva.filas = [0] * len(self.filas)
        
        # Recorremos la matriz original columna por columna (j)
        for j in range(self.m):
            # Para cada valor en la columna j
            for k in range(self.ccolumnas[j], self.ccolumnas[j+1]):
                fila_original = self.filas[k]
                valor = self.valores[k]
                
                # En la transpuesta:
                # - La columna destino es 'fila_original'
                # - La fila destino es 'j' (la columna original)
                dest_idx = posicion_actual[fila_original]
                
                nueva.valores[dest_idx] = valor
                nueva.filas[dest_idx] = j # Aquí se guarda la columna original como fila
                
                posicion_actual[fila_original] += 1
                
        return nueva


    @classmethod
    def crear_desde_matriz(cls, matriz_completa: List[List[int]]) -> 'SparseMatrix':
        # 1. Se obtiene las dimensiones de la matriz
        n = len(matriz_completa)
        if n == 0:
            return cls(0, 0)
        m = len(matriz_completa[0])
        
        # 2. Se crea una instancia vacía
        nueva_matriz = cls(n, m)
        
        # 3. Se recorre la matriz POR COLUMNAS (j primero, luego i)
        # llenamos columna por columna
        for j in range(m):
            for i in range(n):
                valor = matriz_completa[i][j]
                
                if valor != 0:
                    # Como vamos en orden, solo hacemos append (muy rápido)
                    nueva_matriz.valores.append(valor)
                    nueva_matriz.filas.append(i)
            
            # Al terminar una columna, actualizamos el puntero de la siguiente
            # El siguiente ccolumna empieza donde termina el actual
            nueva_matriz.ccolumnas[j+1] = len(nueva_matriz.valores)
            
        return nueva_matriz
