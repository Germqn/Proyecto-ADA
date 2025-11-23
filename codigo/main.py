from typing import List
from matriz_coo import MatrizCOO
from matriz_csr import MatrizCSR
from matriz_csc import MatrizCSC

def verificar_csc_pdf():
    """
    Prueba específica para el Integrante 3 (CSC) usando el ejemplo del PDF.
    """
    print("\n" + "="*50)
    print("   VERIFICACIÓN ENTREGABLE: MATRIZ CSC (Integrante 3)")
    print("="*50)
    
    # 1. Reconstruimos la matriz del PDF manualmente
    filas, cols = 8, 7
    matriz_completa = [[0] * cols for _ in range(filas)]
    
    # Valores del PDF
    matriz_completa[4][0] = 5; matriz_completa[5][0] = 1; matriz_completa[6][0] = 4
    matriz_completa[0][1] = 2; matriz_completa[1][1] = 8; matriz_completa[5][1] = 2
    matriz_completa[1][2] = 9; matriz_completa[7][2] = 7
    matriz_completa[2][3] = 3
    matriz_completa[1][5] = 1; matriz_completa[4][5] = 6; matriz_completa[7][5] = 11
    matriz_completa[0][6] = 4

    # 2. Crear CSC
    print("1. Creando matriz desde matriz completa (Punto 1b)...")
    csc = MatrizCSC.crear_desde_matriz(matriz_completa)
    
    # 3. Validar
    valores_esp = [5, 1, 4, 2, 8, 2, 9, 7, 3, 1, 6, 11, 4]
    filas_esp =   [4, 5, 6, 0, 1, 5, 1, 7, 2, 1, 4, 7, 0]
    ccols_esp =   [0, 3, 6, 8, 9, 9, 12, 13]
    
    print(f"   -> Valores coinciden: {'✅' if csc.valores == valores_esp else '❌'}")
    print(f"   -> Filas coinciden:   {'✅' if csc.filas == filas_esp else '❌'}")
    print(f"   -> CCols coinciden:   {'✅' if csc.ccolumnas == ccols_esp else '❌'}")

    # 4. Operaciones Extra
    print("\n2. Verificando Operaciones (Puntos 2, 3, 4)...")
    
    # Obtener elemento
    val = csc.obtener_elemento(4, 0)
    print(f"   -> Obtener (4,0): {val} (Esperado 5) {'✅' if val==5 else '❌'}")
    
    # Transpuesta
    print("   -> Calculando Transpuesta...")
    mt = csc.transpuesta()
    val_t = mt.obtener_elemento(0, 4) # Debe ser el 5 de antes
    print(f"   -> Transpuesta (0,4): {val_t} (Esperado 5) {'✅' if val_t==5 else '❌'}")
    
    # Suma
    print("   -> Calculando Suma (Matriz + Matriz)...")
    msuma = csc.sumar(csc)
    val_s = msuma.obtener_elemento(4, 0)
    print(f"   -> Suma (4,0): {val_s} (Esperado 10) {'✅' if val_s==10 else '❌'}")

def main():
    print("INICIANDO PRUEBAS DEL PROYECTO DE MATRICES DISPERSAS")
    
    # --- PRUEBAS INTEGRANTE 1 (COO) ---
    # print("\n--- Pendiente: Implementación COO ---")
    # m_coo = MatrizCOO(5, 5)
    
    # --- PRUEBAS INTEGRANTE 2 (CSR) ---
    # print("\n--- Pendiente: Implementación CSR ---")
    # m_csr = MatrizCSR(5, 5)
    
    # --- PRUEBAS INTEGRANTE 3 (CSC) ---
    verificar_csc_pdf()

if __name__ == "__main__":
    main()
