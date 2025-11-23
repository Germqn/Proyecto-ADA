from matriz_coo import MatrizCOO
from matriz_csr import MatrizCSR
from matriz_csc import MatrizCSC

def probar_matriz(nombre_clase, clase_matriz):
    print(f"--- Probando {nombre_clase} ---")
    # Crear una matriz de 5x5
    m = clase_matriz(5, 5)
    
    # Insertar algunos valores
    print("Insertando valores...")
    m.modificar_posicion(0, 0, 10)
    m.modificar_posicion(1, 1, 20)
    m.modificar_posicion(2, 2, 30)
    
    # Verificar valores
    print(f"Valor en (1,1) (Esperado 20): {m.obtener_elemento(1, 1)}")
    print(f"Valor en (0,1) (Esperado 0): {m.obtener_elemento(0, 1)}")
    
    print(f"Estado interno: {m}")
    print("\n")

if __name__ == "__main__":
    # Descomentar a medida que los integrantes terminen sus partes
    probar_matriz("COO", MatrizCOO)
    probar_matriz("CSR", MatrizCSR)
    probar_matriz("CSC", MatrizCSC)
