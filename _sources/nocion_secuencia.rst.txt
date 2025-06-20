Noción de Secuencia
===================

Concepto
--------
Una **secuencia** es un conjunto de datos relacionados entre sí que cumplen ciertas características:
*   **Existencia del primer elemento**: El acceso a este permite el acceso posterior a los demás.
*   **Relación de sucesión**: Todo objeto, salvo el último, precede a un sucesor. Permite construir el acceso a todos los elementos.
*   **Finitud**: Puede ser conocida o no (por cantidad o marca de fin). Deben ser finitas y acotadas por una condición de fin.
*   **Existencia del último elemento**: Un indicador de fin de secuencia.

Su tamaño no es fijo y puede variar. Requiere asignación de almacenamiento en memoria dinámica.

Clasificación
-------------

Según su contenido
~~~~~~~~~~~~~~~~~~
*   De datos elementales (Ej: secuencia de caracteres, secuencia de números).
*   De registros.

Según su procesamiento
~~~~~~~~~~~~~~~~~~~~~~
*   **Definidas**: Se conoce el último elemento antes de iniciar el proceso.
    *   Utiliza estructura Manejada por Contador (PARA) o Post-Test (REPETIR).
*   **Indefinidas**: No se conoce el último elemento.
    *   **Puras**: Utiliza estructura Pre-Test (MIENTRAS). El fin se detecta al intentar leer más allá del último elemento.
    *   **Impuras**: Cuentan con una marca de fin explícita como un elemento más de la secuencia.

Uso en el Algoritmo
-------------------

Definición en el ambiente
~~~~~~~~~~~~~~~~~~~~~~~~~
Se define la estructura de datos (tipo de elemento de la secuencia) y la variable de tipo secuencia.

.. code-block:: text

    // Ejemplo: secuencia de caracteres
    // 'v' sería la variable para almacenar el caracter actual
    // 'sec' es la variable que representa la secuencia en sí
    sec: Secuencia de caracter
    v: caracter

    // Ejemplo: secuencia de números enteros
    // 'num' sería la variable para el entero actual
    // 'sec_enteros' es la variable secuencia
    sec_enteros: Secuencia de entero
    num: entero

Acciones en el procesamiento (Operadores de Secuencia)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*   `ARR(sec)`: **Abrir/Arreglar**. Permite iniciar el tratamiento de una secuencia *ya existente*.
    Posiciona un puntero conceptual al inicio de la secuencia `sec` para la lectura.

*   `AVZ(sec, v)`: **Avanzar**. Recupera el contenido del elemento actual de la secuencia `sec` en la variable `v`,
    y avanza el puntero conceptual al siguiente elemento.
    Indica fin de secuencia si no hay más elementos.

*   `CREAR(secNueva)`: **Crear**. Inicializa una nueva secuencia `secNueva` como vacía.
    Prepara la secuencia para escritura.

*   `ESC(sec, v)`: **Escribir**. Agrega el contenido de la variable `v` como un nuevo elemento al final
    de la secuencia `sec`. La secuencia debe haber sido abierta con `CREAR`.

*   `CERRAR(sec)`: (No listado explícitamente en los PDFs pero implícito en el manejo de archivos/secuencias)
    Finaliza el procesamiento de la secuencia `sec`, guardando cambios si es de salida.

Sub-Secuencias
--------------
Conjunto de elementos consecutivos, incluidos en la secuencia, considerados como un subconjunto
de acuerdo a la definición del problema.
Cumplen las mismas características que una secuencia.

Ejemplos:
*   **Palabra**: Subconjunto de elementos de una secuencia de caracteres que comienza con un carácter distinto de espacio
    y finaliza con un espacio o marca específica.
    `H O L A   M U N D O . FDS`  (FDS es fin de secuencia)
    Palabras: "HOLA", "MUNDO"

*   **Oración**: Subconjunto de elementos de una secuencia de caracteres que comienza con un carácter distinto de espacio
    y finaliza con un punto `.` o marca específica.
    `H O L A   M U N D O .   A D I O S . FDS`
    Oraciones: "H O L A   M U N D O .", "A D I O S ."

*   **DNI**: Subconjunto de 8 elementos consecutivos de una secuencia de caracteres, donde cada carácter es un dígito.
    `N-O-M-B-R-E- -1-2-3-4-5-6-7-8-FDS`
    DNI: "12345678"

Relación entre Sub-Secuencias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*   **Enlazadas**: Identificadas una a continuación de la otra. El inicio de una sub-secuencia indica el fin de la anterior (salvo inicio/fin de secuencia general).
    Ej: `Nombre1-DNI1-Nombre2-DNI2-...`

*   **Jerárquicas**: Identificadas por pertenencia o inclusión. Una sub-secuencia está contenida dentro de otra.
    Ej: Una `ORACION` está formada por `PALABRAS`.
    El inicio y fin de una sub-secuencia de mayor jerarquía determina el inicio y fin de otras sub-secuencias incluidas.

    .. code-block:: text

        SECUENCIA PRINCIPAL
            |
            +-- ORACION 1
            |   |
            |   +-- PALABRA 1.1
            |   +-- PALABRA 1.2
            |
            +-- ORACION 2
                |
                +-- PALABRA 2.1