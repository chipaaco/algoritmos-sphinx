Estructuras de Control
======================

Las estructuras de control señalan el orden en que tienen que sucederse los pasos de un algoritmo.
Todo algoritmo estructurado puede ser escrito utilizando solamente tres tipos de estructura de control.

Estructura Secuencial
---------------------
Una acción (instrucción) sigue a otra en secuencia. La salida de una es la entrada de la siguiente.

.. code-block:: text

    ACCION Ejemplo1 ES
    AMBIENTE
        a, doble: entero
    PROCESO
        ESCRIBIR("Ingrese el número")
        LEER(a)
        doble := a * 2
        ESCRIBIR("Resultado ->", doble)
    FIN_ACCION

Estructura Condicional
----------------------
Se utilizan para tomar decisiones lógicas.

Condicional Alternativo Simple (SI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Si se verifica una condición, se ejecuta una serie de instrucciones.

.. code-block:: text

    SI <condición> ENTONCES
        <acciones_si_verdadero>
    FIN_SI

    // Ejemplo
    ACCION Ejemplo2 ES
    AMBIENTE
        a: entero
    PROCESO
        ESC("Ingrese el número")
        LEER(a)
        SI a > 0 ENTONCES
            ESCRIBIR("El nro. es positivo")
        FIN_SI
    FIN_ACCION

Condicional Alternativo Doble (SI-SINO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Si se verifica una condición, se ejecuta un bloque; si no, se ejecuta otro.

.. code-block:: text

    SI <condición> ENTONCES
        <acciones_si_verdadero>
    SINO
        <acciones_si_falso>
    FIN_SI

    // Ejemplo
    ACCION Ejemplo3 ES
    AMBIENTE
        A, B: ENTERO
    PROCESO
        ESC("Ingrese el primer número"), LEER(A)
        ESC("Ingrese el segundo número"), LEER(B)
        SI A > B ENTONCES
            ESC(A, "es mayor que ", B)
        SINO
            ESC(A, "NO es mayor que ", B)
        FIN_SI
    FIN_ACCION

Condicional Alternativo Múltiple (SEGÚN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Permite evaluar una variable que puede tomar múltiples valores y ejecutar diferentes acciones para cada uno.

.. code-block:: text

    SEGÚN <variable_o_expresion> HACER
        <valor1>: <acciones_para_valor1>
        <valor2>: <acciones_para_valor2>
        ...
        <otro_caso>: <acciones_por_defecto> // Opcional
    FIN_SEGUN

    // Ejemplo
    ACCION EJEMPLO4 ES
    AMBIENTE
        a, b, suma: entero
    PROCESO
        ESC("Ingrese el primer número"), LEER(a)
        ESC ("Ingrese el segundo número"),LEER(b)
        suma := a + b
        SEGÚN suma HACER
            =0 : ESC("El resultado es igual a 0")
            <0: ESC("El resultado es menor a 0")
            >0: ESC("El resultado es mayor a 0")
        FIN_SEGUN
    FIN_ACCION

Estructuras Repetitivas (Bucles)
--------------------------------
Repiten una secuencia de instrucciones un número determinado o indeterminado de veces.
Cada repetición se llama **iteración**.

Estructura PRE-TEST (MIENTRAS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
El cuerpo del bucle se repite **mientras** una condición sea verdadera.
La condición se evalúa **antes** de cada iteración. Puede ejecutarse 0 o más veces.

.. code-block:: text

    MIENTRAS <condición> HACER
        <acciones_del_bucle>
    FIN_MIENTRAS

    // Ejemplo: Suma de números entre 1 y N
    ACCION BUCLE1_MIENTRAS ES
    AMBIENTE
        n, suma, cont: entero
    PROCESO
        ESCRIBIR("Ingrese el numero"), LEER(n)
        suma := 0
        cont := 1
        MIENTRAS cont <= n HACER
            suma := suma + cont
            cont := cont + 1
        FIN_MIENTRAS
        ESCRIBIR("La suma es: ", suma)
    FIN_ACCION

Estructura POST-TEST (REPETIR)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
El cuerpo del bucle se ejecuta **al menos una vez**, y se repite **hasta que** una condición sea verdadera.
La condición se evalúa **después** de cada iteración.

.. code-block:: text

    REPETIR
        <acciones_del_bucle>
    HASTA QUE <condición>

    // Ejemplo: Suma de números entre 1 y N
    ACCION BUCLE1_REPETIR ES
    AMBIENTE
        n, suma, cont: entero
    PROCESO
        ESCRIBIR("Ingrese el numero"), LEER(n)
        suma := 0
        cont := 0 // o 1, ajustar lógica interna
        REPETIR
            cont := cont + 1 // Si cont inicia en 0
            suma := suma + cont
            // Si cont iniciara en 1, el orden podría ser suma, luego cont++
        HASTA QUE cont >= n // o suma >= n en el ejemplo original (que parece un error de lógica para sumar 1 a N)
                            // Para sumar de 1 a N, la condición de parada es sobre 'cont'
        ESCRIBIR("La suma es: ", suma)
    FIN_ACCION

Estructura Manejada por Contador (PARA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Es un ciclo definido, se conoce de antemano la cantidad de veces que se iterará.

.. code-block:: text

    PARA <variable_contador> := <valor_inicial> HASTA <valor_final> [INCREMENTO <paso>] HACER
        <acciones_del_bucle>
    FIN_PARA

    // Ejemplo: Suma de números entre 1 y N
    ACCION BUCLE3_PARA ES
    AMBIENTE
        n, suma, cont: entero
    PROCESO
        ESCRIBIR("Ingrese el numero"), LEER(n)
        suma := 0
        PARA cont := 1 HASTA n HACER  // Incremento por defecto es 1
            suma := suma + cont
        FIN_PARA
        ESCRIBIR("La suma es: ", suma)
    FIN_ACCION

Comparación entre Estructuras Repetitivas
-----------------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Característica
     - PRE-TEST (MIENTRAS)
     - POST-TEST (REPETIR)
     - MANEJADO X CONT (PARA)
   * - ¿Se conoce N° iteraciones?
     - NO
     - NO
     - SI
   * - Momento verificación condición
     - Antes de ejecutar cuerpo
     - Después de ejecutar cuerpo
     - Antes de ejecutar cuerpo
   * - ¿Puede no ejecutarse nunca?
     - SI (si condición es falsa al inicio)
     - NO (al menos una vez)
     - SI (si Vi > Vf y paso > 0)
   * - ¿Modificar valor condición en bucle?
     - SI (necesario para finalizar)
     - SI (necesario para finalizar)
     - NO (es automático)
   * - ¿Puede ser infinito?
     - SI
     - SI
     - NO (generalmente)
   * - Cuándo usar
     - N° iteraciones indeterminado, puede no ejecutarse
     - N° iteraciones indeterminado, debe ejecutarse al menos una vez
     - N° iteraciones conocido por adelantado