
import os

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

def verificar_coo():
    """
    Prueba específica del Integrante 1 (COO).
    """

    print("\n" + "="*50)
    print("   VERIFICACIÓN ENTREGABLE: MATRIZ COO (Integrante 1)")
    print("="*50)

    # Matriz completa de ejemplo
    matriz_completa = [
        [0, 0, 5, 0],
        [2, 0, 0, 0],
        [0, 3, 0, 7]
    ]

    print("Matriz completa original:")
    for fila in matriz_completa:
        print(fila)

    # Crear matriz COO desde matriz completa
    matriz_coo = MatrizCOO.crear_desde_matriz(matriz_completa)
    print(f"\nMatriz COO creada: {matriz_coo}")
    print(f"Valores: {matriz_coo.valores}")
    print(f"Filas: {matriz_coo.filas}")
    print(f"Columnas: {matriz_coo.columnas}")

    print("\n2. OPERACIÓN: OBTENER ELEMENTO")
    print("=" * 50)

    # Obtener elementos existentes
    print(f"Elemento (0,2): {matriz_coo.obtener_elemento(0, 2)}")  
    print(f"Elemento (1,0): {matriz_coo.obtener_elemento(1, 0)}")
    print(f"Elemento (2,1): {matriz_coo.obtener_elemento(2, 1)}")
    print(f"Elemento (2,3): {matriz_coo.obtener_elemento(2, 3)}")

    # Obtener elementos cero (no almacenados)
    print(f"Elemento (0,0): {matriz_coo.obtener_elemento(0, 0)}")
    print(f"Elemento (1,1): {matriz_coo.obtener_elemento(1, 1)}")

    print("\n3. OPERACIÓN: OBTENER FILA COMPLETA")
    print("=" * 50)

    # Obtener todas las filas
    for i in range(3):
        fila = matriz_coo.obtener_fila(i)
        print(f"Fila {i}: {fila}")

    print("\n4. OPERACIÓN: OBTENER COLUMNA COMPLETA")
    print("=" * 50)

    # Obtener todas las columnas
    for j in range(4):
        columna = matriz_coo.obtener_columna(j)
        print(f"Columna {j}: {columna}")

    print("\n5. OPERACIÓN: MODIFICAR POSICIÓN")
    print("=" * 50)

    print("Estado antes de modificar:")
    print(f"Elemento (1,1): {matriz_coo.obtener_elemento(1, 1)}")

    # Modificar posición existente con cero (debe eliminar)
    print("\nModificando (1,0) de 2 a 0 (eliminación):")
    matriz_coo.modificar_posicion(1, 0, 0)
    print(f"Elemento (1,0) después: {matriz_coo.obtener_elemento(1, 0)}")
    print(f"Matriz COO ahora: {matriz_coo}")

    # Modificar posición con valor no cero (nueva inserción)
    print("\nInsertando nuevo elemento (1,1) = 9:")
    matriz_coo.modificar_posicion(1, 1, 9)
    print(f"Elemento (1,1) después: {matriz_coo.obtener_elemento(1, 1)}")
    print(f"Matriz COO ahora: {matriz_coo}")

    # Actualizar elemento existente
    print("\nActualizando (2,1) de 3 a 10:")
    matriz_coo.modificar_posicion(2, 1, 10)
    print(f"Elemento (2,1) después: {matriz_coo.obtener_elemento(2, 1)}")
    print(f"Matriz COO ahora: {matriz_coo}")

    print("\n6. OPERACIÓN: SUMA DE MATRICES")
    print("=" * 50)

    # Crear segunda matriz para suma
    matriz_completa2 = [
        [1, 0, 0, 2],
        [0, 4, 0, 0],
        [0, 0, 6, 0]
    ]

    matriz_coo2 = MatrizCOO.crear_desde_matriz(matriz_completa2)
    print(f"Segunda matriz COO: {matriz_coo2}")

    # Realizar suma
    print("\nRealizando suma de matrices:")
    matriz_suma = matriz_coo.sumar(matriz_coo2)
    print(f"Resultado de la suma: {matriz_suma}")

    # Verificar resultado manualmente
    print("\nVerificación manual de la suma:")
    print("Matriz 1 reconstruida:")
    for i in range(3):
        print(matriz_coo.obtener_fila(i))
    print("Matriz 2 reconstruida:")
    for i in range(3):
        print(matriz_coo2.obtener_fila(i))
    print("Suma reconstruida:")
    for i in range(3):
        print(matriz_suma.obtener_fila(i))

    print("\n7. OPERACIÓN: MATRIZ TRANSPUESTA")
    print("=" * 50)

    # Calcular transpuesta
    print("Calculando transpuesta:")
    matriz_transpuesta = matriz_coo.transpuesta()
    print(f"Matriz original (3x4): {matriz_coo}")
    print(f"Matriz transpuesta (4x3): {matriz_transpuesta}")

    # Mostrar transpuesta completa
    print("\nMatriz transpuesta completa:")
    for i in range(4):  # Ahora tiene 4 filas
        fila = matriz_transpuesta.obtener_fila(i)
        print(f"Fila {i} (columna original {i}): {fila}")

    print("\n8. VERIFICACIÓN FINAL DEL ESTADO")
    print("=" * 50)

    print("Estado final de la matriz original COO:")
    print(f"Dimensiones: {matriz_coo.n} x {matriz_coo.m}")
    print(f"Valores almacenados: {matriz_coo.valores}")
    print(f"Posiciones filas: {matriz_coo.filas}")
    print(f"Posiciones columnas: {matriz_coo.columnas}")

    print("\nMatriz original reconstruida completamente:")
    for i in range(matriz_coo.n):
        fila_completa = matriz_coo.obtener_fila(i)
        print(f"Fila {i}: {fila_completa}")


def menuPruebas():
    os.system("cls")
    
    print("\n" + "="*50)
    print("   MENU PRINCIPAL")
    print("="*50)
    print("1. Verificar COO")
    print("2. Verificar CSR")
    print("3. Verificar CSC")
    print("4. Salir")
    print("\n" + "="*50)

    opcion = int(input("\nIngrese su opcion: "))

    if opcion == 1:
        verificar_coo()
    elif opcion == 2:
        verificar_csr()
    elif opcion == 3:
        verificar_csc()
    elif opcion == 4:
        print("\nGracias por usar el programa")
        exit()
    else:
        print("\nOpcion invalida")
        menuPruebas()

def menu():
    os.system("cls")
    print("\n" + "="*50)
    print("   MENU PRINCIPAL")
    print("="*50)
    print("1. Iniciar pruebas")
    print("2. Pruebas personalizadas")
    print("3. Salir")
    print("\n" + "="*50)

    opcion = int(input("\nIngrese su opcion: "))

    if opcion == 1:
        menuPruebas()
    elif opcion == 2:
        menuPersonalizado()
    elif opcion == 3:
        print("\nGracias por usar el programa")
        exit()
    else:
        print("\nOpcion invalida")
        menu()

def obtener_matriz_usuario():
    
    print("\n" + "="*30)
    print("   SELECCIÓN DE MATRIZ")
    print("="*30)
    print("1. Usar matriz predeterminada (del ejemplo)")
    print("2. Ingresar nueva matriz manualmente")
    
    try:
        opcion = int(input("\nIngrese su opción: "))
        
        if opcion == 1:
            # Matriz del ejemplo (8x7) utilizada para verificar la lógica de dispersión
            # Esta matriz contiene varios ceros para probar la eficiencia de las estructuras
            return [
                [0, 2, 0, 0, 0, 0, 4],
                [0, 8, 9, 0, 0, 1, 0],
                [0, 0, 0, 3, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [5, 0, 0, 0, 0, 6, 0],
                [1, 2, 0, 0, 0, 0, 0],
                [4, 0, 0, 0, 0, 0, 0],
                [0, 0, 7, 0, 0, 11, 0]
            ]
        elif opcion == 2:
            # Entrada manual de dimensiones
            filas = int(input("Ingrese número de filas: "))
            cols = int(input("Ingrese número de columnas: "))
            
            matriz = []
            print(f"\nIngrese los valores fila por fila ({cols} valores separados por espacio):")
            # Bucle para ingresar cada fila asegurando que tenga la longitud correcta
            for i in range(filas):
                while True:
                    try:
                        fila_str = input(f"Fila {i}: ").strip().split()
                        # Validación de longitud de la fila
                        if len(fila_str) != cols:
                            print(f"Error: Debe ingresar exactamente {cols} valores.")
                            continue
                        # Conversión de valores a enteros
                        fila = [int(x) for x in fila_str]
                        matriz.append(fila)
                        break
                    except ValueError:
                        print("Error: Ingrese solo números enteros.")
            return matriz
        else:
            print("Opción inválida. Usando matriz predeterminada.")
            return obtener_matriz_usuario() # Recursiva simple para reintentar
    except ValueError:
        print("Entrada inválida.")
        return obtener_matriz_usuario()

def seleccionar_tipo_matriz(matriz_completa):
    
    print("\n" + "="*30)
    print("   TIPO DE REPRESENTACIÓN")
    print("="*30)
    print("1. COO (Coordenado)")
    print("2. CSR (Compressed Sparse Row)")
    print("3. CSC (Compressed Sparse Column)")
    
    try:
        opcion = int(input("\nSeleccione el tipo de matriz: "))
        
        # Instancia la clase correspondiente según la selección
        if opcion == 1:
            return MatrizCOO.crear_desde_matriz(matriz_completa), "COO"
        elif opcion == 2:
            return MatrizCSR.crear_desde_matriz(matriz_completa), "CSR"
        elif opcion == 3:
            return MatrizCSC.crear_desde_matriz(matriz_completa), "CSC"
        else:
            print("Opción inválida.")
            return None, None
    except ValueError:
        print("Entrada inválida.")
        return None, None

def operaciones_matriz(matriz, nombre_tipo):

    while True:
        print("\n" + "="*50)
        print(f"   OPERACIONES CON MATRIZ {nombre_tipo}")
        print("="*50)
        print("1. Ver matriz completa (Representación interna y visual)")
        print("2. Obtener elemento (i, j)")
        print("3. Obtener fila completa")
        print("4. Obtener columna completa")
        print("5. Modificar/Insertar elemento")
        print("6. Calcular transpuesta")
        print("7. Sumar con otra matriz")
        print("8. Volver al menú principal")
        
        try:
            op = int(input("\nIngrese operación: "))
            
            if op == 1:
                # Muestra la estructura interna específica de cada formato
                print(f"\nMatriz {nombre_tipo} ({matriz.n}x{matriz.m}):")
                if nombre_tipo == "COO":
                    print(f"Valores: {matriz.valores}")
                    print(f"Filas: {matriz.filas}")
                    print(f"Cols: {matriz.columnas}")
                elif nombre_tipo == "CSR":
                    print(f"Valores: {matriz.valores}")
                    print(f"Columnas: {matriz.columnas}")
                    print(f"CFilas: {matriz.cfilas}")
                elif nombre_tipo == "CSC":
                    print(f"Valores: {matriz.valores}")
                    print(f"Filas: {matriz.filas}")
                    print(f"CColumnas: {matriz.ccolumnas}")
                    
                # Muestra la matriz reconstruida visualmente fila por fila
                print("\nReconstrucción visual:")
                for i in range(matriz.n):
                    print(matriz.obtener_fila(i))
                    
            elif op == 2:
                # Obtención de un elemento individual
                i = int(input("Fila (i): "))
                j = int(input("Columna (j): "))
                if 0 <= i < matriz.n and 0 <= j < matriz.m:
                    val = matriz.obtener_elemento(i, j)
                    print(f"Elemento ({i},{j}) = {val}")
                else:
                    print("Índices fuera de rango.")
                    
            elif op == 3:
                # Obtención de fila completa
                i = int(input("Fila (i): "))
                if 0 <= i < matriz.n:
                    print(f"Fila {i}: {matriz.obtener_fila(i)}")
                else:
                    print("Fila fuera de rango.")
                    
            elif op == 4:
                # Obtención de columna completa
                j = int(input("Columna (j): "))
                if 0 <= j < matriz.m:
                    print(f"Columna {j}: {matriz.obtener_columna(j)}")
                else:
                    print("Columna fuera de rango.")
                    
            elif op == 5:
                # Modificación o inserción de un valor
                i = int(input("Fila (i): "))
                j = int(input("Columna (j): "))
                val = int(input("Nuevo valor: "))
                try:
                    matriz.modificar_posicion(i, j, val)
                    print("Modificación exitosa.")
                except Exception as e:
                    print(f"Error al modificar: {e}")
                    
            elif op == 6:
                # Cálculo y visualización de la transpuesta
                t = matriz.transpuesta()
                print("\nMatriz Transpuesta calculada exitosamente.")
                print(f"Dimensiones: {t.n}x{t.m}")
                print("Primeras filas de la transpuesta:")
                for k in range(min(3, t.n)):
                    print(t.obtener_fila(k))
                    
            elif op == 7:
                # Suma de matrices
                print("\n--- Segunda Matriz para Suma ---")
                print("Nota: Debe ingresar una segunda matriz para sumarla a la actual.")
                m2_completa = obtener_matriz_usuario()
                
                # Crear la segunda matriz del MISMO tipo para asegurar compatibilidad
                if nombre_tipo == "COO":
                    m2 = MatrizCOO.crear_desde_matriz(m2_completa)
                elif nombre_tipo == "CSR":
                    m2 = MatrizCSR.crear_desde_matriz(m2_completa)
                elif nombre_tipo == "CSC":
                    m2 = MatrizCSC.crear_desde_matriz(m2_completa)
                
                try:
                    suma = matriz.sumar(m2)
                    print("\nSuma realizada exitosamente.")
                    print("Resultado (primeras filas):")
                    for k in range(min(3, suma.n)):
                        print(suma.obtener_fila(k))
                except Exception as e:
                    print(f"Error en la suma: {e}")
                    
            elif op == 8:
                break
            else:
                print("Opción no válida.")
                
        except ValueError:
            print("Entrada inválida. Por favor ingrese números.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

def menuPersonalizado():
    """
    Función principal del menú de pruebas personalizadas.
    Orquesta el flujo de:
    1. Obtener matriz (default o manual).
    2. Seleccionar tipo de representación (COO, CSR, CSC).
    3. Ejecutar operaciones sobre la matriz creada.
    """
    os.system("cls")
    print("\n" + "="*50)
    print("   PRUEBAS PERSONALIZADAS")
    print("="*50)
    
    # Paso 1: Obtener la matriz base
    matriz_completa = obtener_matriz_usuario()
    
    # Paso 2: Convertir a la representación deseada
    matriz_dispersa, nombre = seleccionar_tipo_matriz(matriz_completa)
    
    # Paso 3: Operar
    if matriz_dispersa:
        operaciones_matriz(matriz_dispersa, nombre)
    else:
        print("No se pudo crear la matriz o selección cancelada.")
    
    input("\nPresione Enter para volver al menú principal...")

def main():
    menu()


if __name__ == "__main__":
    main()
