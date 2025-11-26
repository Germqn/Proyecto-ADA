from typing import List
from matriz_coo import MatrizCOO
from matriz_csr import MatrizCSR
from matriz_csc import MatrizCSC


def verificar_csr():
    """
    Prueba específica del Integrante 2 (CSR).
    """
    print("\n" + "="*50)
    print("   VERIFICACIÓN ENTREGABLE: MATRIZ CSR (Integrante 2)")
    print("="*50)

    # Matriz pequeña de prueba
    matriz_completa = [
        [0, 2, 0, 0],
        [5, 0, 1, 0],
        [0, 0, 3, 0],
        [4, 0, 0, 7]
    ]

    print("\n1. Creando matriz CSR desde matriz completa...")
    csr = MatrizCSR.crear_desde_matriz(matriz_completa)

    print("   -> Valores:", csr.valores)
    print("   -> Columnas:", csr.columnas)
    print("   -> CFilas:", csr.cfilas)

    print("\n2. Probando obtener_elemento...")
    print("   -> (1,0):", csr.obtener_elemento(1, 0))
    print("   -> (0,1):", csr.obtener_elemento(0, 1))
    print("   -> (3,3):", csr.obtener_elemento(3, 3))

    print("\n3. Probando obtener_fila...")
    print("   -> Fila 1:", csr.obtener_fila(1))
    print("   -> Fila 3:", csr.obtener_fila(3))

    print("\n4. Probando modificar_posicion...")
    csr.modificar_posicion(0, 2, 6)
    print("   -> Fila 0 tras insertar 6 en (0,2):", csr.obtener_fila(0))

    csr.modificar_posicion(1, 0, 0)
    print("   -> Fila 1 tras eliminar (1,0):", csr.obtener_fila(1))

    print("\n5. Probando transpuesta...")
    t = csr.transpuesta()
    print("   -> Transpuesta (0,3):", t.obtener_elemento(0, 3))
    print("   -> Transpuesta (2,0):", t.obtener_elemento(2, 0))

    print("\n6. Probando suma (CSR + CSR)...")
    suma = csr.sumar(csr)
    print("   -> Fila 0 sumada:", suma.obtener_fila(0))
    print("   -> Fila 3 sumada:", suma.obtener_fila(3))


def verificar_csc():
    """
    Prueba específica del Integrante 3 (CSC).
    """
    print("\n" + "="*50)
    print("   VERIFICACIÓN ENTREGABLE: MATRIZ CSC (Integrante 3)")
    print("="*50)
    
    matriz_completa = [
        [0, 2, 0, 0, 0, 0, 4],  # Fila 0
        [0, 8, 9, 0, 0, 1, 0],  # Fila 1
        [0, 0, 0, 3, 0, 0, 0],  # Fila 2
        [0, 0, 0, 0, 0, 0, 0],  # Fila 3
        [5, 0, 0, 0, 0, 6, 0],  # Fila 4
        [1, 2, 0, 0, 0, 0, 0],  # Fila 5
        [4, 0, 0, 0, 0, 0, 0],  # Fila 6
        [0, 0, 7, 0, 0, 11, 0]  # Fila 7
    ]

    print("\n1. Creando matriz CSC desde matriz completa...")
    csc = MatrizCSC.crear_desde_matriz(matriz_completa)
    
    print("   -> Valores:", csc.valores)
    print("   -> Filas:", csc.filas)
    print("   -> CColumnas:", csc.ccolumnas)

    print("\n2. Probando obtener_elemento...")
    print("   -> (4,0):", csc.obtener_elemento(4, 0))
    print("   -> (0,1):", csc.obtener_elemento(0, 1))
    print("   -> (7,5):", csc.obtener_elemento(7, 5))

    print("\n3. Probando obtener_columna...")
    print("   -> Columna 1:", csc.obtener_columna(1))
    print("   -> Columna 5:", csc.obtener_columna(5))

    print("\n4. Probando modificar_posicion...")
    csc.modificar_posicion(4, 0, 99)
    print("   -> Columna 0 tras insertar 99 en (4,0):", csc.obtener_columna(0))
    
    csc.modificar_posicion(1, 1, 0)
    print("   -> Columna 1 tras eliminar (1,1):", csc.obtener_columna(1))

    print("\n5. Probando transpuesta...")
    t = csc.transpuesta()
    print("   -> Transpuesta (0,4):", t.obtener_elemento(0, 4))
    print("   -> Transpuesta (1,0):", t.obtener_elemento(1, 0))

    print("\n6. Probando suma (CSC + CSC)...")
    suma = csc.sumar(csc)
    print("   -> Columna 0 sumada:", suma.obtener_columna(0))
    print("   -> Columna 1 sumada:", suma.obtener_columna(1))


def main():
    print("INICIANDO PRUEBAS DEL PROYECTO DE MATRICES DISPERSAS")

    # PRUEBAS INTEGRANTE 2 (CSR)
    verificar_csr()

    # PRUEBAS INTEGRANTE 3 (CSC)
    verificar_csc()


if __name__ == "__main__":
    main()
