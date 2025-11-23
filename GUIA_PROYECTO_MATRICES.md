# Guía de Proyecto: Matrices Dispersas
## Análisis y Diseño de Algoritmos 1

Esta guía detalla la mejor manera de abordar el proyecto final, asegurando una arquitectura de software limpia, una división de trabajo equitativa y una implementación eficiente.

---

## 1. Arquitectura de Software Sugerida

Para cumplir con los requisitos de "mejor manera" (código limpio, mantenible y modular), se recomienda utilizar **Programación Orientada a Objetos (POO)**.

### Estructura de Clases
Deben crear una **Clase Base (Interfaz)** que defina las operaciones, y 3 subclases que implementen la lógica específica.

*   **`SparseMatrix` (Clase Abstracta / Interfaz)**
    *   Define los métodos abstractos: `obtener_elemento`, `obtener_fila`, `modificar_posicion`, `sumar`, `transpuesta`, etc.
    *   Esto asegura que los 3 integrantes programen con los mismos nombres de funciones.

*   **`MatrizCOO` (Hereda de SparseMatrix)**
    *   Atributos: `valores`, `filas`, `columnas`.
*   **`MatrizCSR` (Hereda de SparseMatrix)**
    *   Atributos: `valores`, `columnas`, `cfilas`.
*   **`MatrizCSC` (Hereda de SparseMatrix)**
    *   Atributos: `valores`, `filas`, `ccolumnas`.

---

## 2. División del Trabajo (3 Integrantes)

Esta división asegura que cada integrante sea dueño de una parte lógica completa, minimizando los conflictos de código (merge conflicts).

### 👤 Integrante 1: Líder de Arquitectura & Formato Coordenado (COO)
Este formato es el más intuitivo, por lo que este integrante tendrá tiempo extra para coordinar la estructura base.

*   **Responsabilidades de Código:**
    *   Crear la **Clase Abstracta** y definir los nombres exactos de los métodos (el "contrato").
    *   Implementar la clase **`MatrizCOO`** completa.
    *   Implementar la función principal `main` o script de pruebas que verifique que todo funciona.
*   **Responsabilidades del Informe:**
    *   Redactar la **Introducción**.
    *   Explicar el **Formato Coordenado**.
    *   Unificar el PDF final.

### 👤 Integrante 2: Especialista en Filas (Formato CSR)
Este formato es el estándar industrial más común. Requiere entender bien la compresión por filas.

*   **Responsabilidades de Código:**
    *   Implementar la clase **`MatrizCSR`** completa.
    *   Prestar especial atención a la lógica del vector `cfilas` (punteros de fila).
    *   Optimizar la búsqueda binaria para `obtener_elemento` (ya que las columnas en CSR suelen estar ordenadas).
*   **Responsabilidades del Informe:**
    *   Explicar el **Formato CSR** con diagramas.
    *   Realizar el **Análisis de Complejidad** de las operaciones en CSR.

### 👤 Integrante 3: Especialista en Columnas (Formato CSC)
Este formato es simétrico al CSR pero por columnas. Es crucial para operaciones matemáticas específicas.

*   **Responsabilidades de Código:**
    *   Implementar la clase **`MatrizCSC`** completa.
    *   Implementar la lógica del vector `ccolumnas`.
    *   Implementar la **Transpuesta** de forma eficiente (Nota: La transpuesta de una CSR es estructuralmente una CSC y viceversa, este integrante puede liderar esa lógica).
*   **Responsabilidades del Informe:**
    *   Explicar el **Formato CSC**.
    *   Redactar las **Conclusiones** y la **Comparativa Final** (cuál formato es mejor para qué cosa).

---

## 3. Explicación Técnica y Estrategias

### A. Formato Coordenado (COO)
*   **Estrategia:** Es una lista simple de tuplas `(fila, col, valor)`.
*   **Reto:** Las operaciones de búsqueda (`obtener_elemento`) son lentas ($O(N)$ donde N es el número de elementos no nulos) si no se ordenan.
*   **Tip:** Mantener los vectores ordenados por fila y luego por columna facilita todo.

### B. Formato Comprimido por Fila (CSR)
*   **Estructura:**
    *   `valores`: [5, 8, 3, 6]
    *   `columnas`: [0, 1, 2, 1] (columnas de cada valor)
    *   `cfilas`: [0, 2, 3, 4] (índices donde *empieza* cada fila en los vectores anteriores).
*   **Lógica Clave (`obtener_fila(i)`):**
    *   El rango de datos para la fila `i` está entre `cfilas[i]` y `cfilas[i+1]`.
    *   Ejemplo: Para leer la fila 1, lees desde `valores[cfilas[1]]` hasta `valores[cfilas[2]]`.

### C. Formato Comprimido por Columna (CSC)
*   **Estructura:** Idéntica a CSR, pero invirtiendo el rol de filas y columnas.
*   **Lógica Clave:** El vector `ccolumnas` dice dónde empieza cada columna.
*   **Tip:** Es muy rápido para extraer columnas completas (`obtener_columna`), pero lento para filas.

### D. Operación "Modificar Posición" (El gran reto)
*   **Problema:** Insertar un nuevo valor en medio de los vectores requiere "empujar" todos los elementos siguientes (complejidad $O(N)$).
*   **Solución:** En implementaciones académicas, se acepta el costo $O(N)$. Simplemente usen funciones de inserción de arrays/listas. **No intenten hacerlo $O(1)$**, es imposible en estos formatos estáticos.

---

## 4. Estructura del Informe (Para el PDF)

1.  **Portada** (Nombres y Códigos).
2.  **Introducción:** Qué son matrices dispersas y por qué importan.
3.  **Metodología:**
    *   Explicación de la Clase Base.
    *   **COO:** Diagrama y explicación.
    *   **CSR:** Diagrama y explicación (¡Usen el ejemplo del enunciado!).
    *   **CSC:** Diagrama y explicación.
4.  **Análisis de Algoritmos (Punto 5 del proyecto):**
    *   Tabla comparativa de complejidades Big-O.
    *   *Ejemplo:* Obtener fila es $O(1)$ en CSR pero $O(N)$ en CSC.
5.  **Conclusiones:** ¿Cuándo usar cuál? (CSR para acceso por filas, CSC para columnas, COO para construcción inicial).

---

## 5. Siguientes Pasos

Para proceder con el código, necesito saber:
1.  **¿Qué lenguaje de programación prefieren?** (Python es recomendado por facilidad, C++ por rendimiento y tipado estricto).
2.  ¿Desean que genere la **plantilla de código** (esqueleto de las clases) ahora mismo?
