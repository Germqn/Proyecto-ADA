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


def verificar_csc_pdf():
    """
    Prueba específica para el Integrante 3 (CSC) usando el ejemplo del PDF.
    """
    print("\n" + "="*50)
    print("   VERIFICACIÓN ENTREGABLE: MATRIZ CSC (Integrante 3)")
    print("="*50)
    
    filas, cols = 8, 7
    matriz_completa = [[0] * cols for _ in range(filas)]
    
    matriz_completa[4][0] = 5; matriz_completa[5][0] = 1; matriz_completa[6][0] = 4
    matriz_completa[0][1] = 2; matriz_completa[1][1] = 8; matriz_completa[5][1] = 2
    matriz_completa[1][2] = 9; matriz_completa[7][2] = 7
    matriz_completa[2][3] = 3
    matriz_completa[1][5] = 1; matriz_completa[4][5] = 6; matriz_completa[7][5] = 11
    matriz_completa[0][6] = 4

    print("1. Creando matriz desde matriz completa (Punto 1b)...")
    csc = MatrizCSC.crear_desde_matriz(matriz_completa)
    
    valores_esp = [5, 1, 4, 2, 8, 2, 9, 7, 3, 1, 6, 11, 4]
    filas_esp =   [4, 5, 6, 0, 1, 5, 1, 7, 2, 1, 4, 7, 0]
    ccols_esp =   [0, 3, 6, 8, 9, 9, 12, 13]
    
    print(f"   -> Valores coinciden: {'✅' if csc.valores == valores_esp else '❌'}")
    print(f"   -> Filas coinciden:   {'✅' if csc.filas == filas_esp else '❌'}")
    print(f"   -> CCols coinciden:   {'✅' if csc.ccolumnas == ccols_esp else '❌'}")

    print("\n2. Verificando Operaciones (Puntos 2, 3, 4)...")
    
    val = csc.obtener_elemento(4, 0)
    print(f"   -> Obtener (4,0): {val} (Esperado 5) {'✅' if val==5 else '❌'}")
    
    print("   -> Calculando Transpuesta...")
    mt = csc.transpuesta()
    val_t = mt.obtener_elemento(0, 4)
    print(f"   -> Transpuesta (0,4): {val_t} (Esperado 5) {'✅' if val_t==5 else '❌'}")
    
    print("   -> Calculando Suma (Matriz + Matriz)...")
    msuma = csc.sumar(csc)
    val_s = msuma.obtener_elemento(4, 0)
    print(f"   -> Suma (4,0): {val_s} (Esperado 10) {'✅' if val_s==10 else '❌'}")


def main():
    print("INICIANDO PRUEBAS DEL PROYECTO DE MATRICES DISPERSAS")

    # PRUEBAS INTEGRANTE 2 (CSR)
    verificar_csr()

    # PRUEBAS INTEGRANTE 3 (CSC)
    verificar_csc_pdf()


if __name__ == "__main__":
    main()
