Introducción a la Algoritmia
============================

Esta sección cubre los conceptos iniciales sobre algoritmos.

Qué es un Algoritmo
-------------------
Un algoritmo es una secuencia finita de instrucciones, reglas o pasos que describen de
modo preciso las operaciones que una computadora debe realizar para ejecutar una
tarea determinada en un tiempo finito.

También se puede decir que es:

* Una fórmula para resolver un problema.
* Un conjunto de acciones o secuencia de operaciones que ejecutadas en un determinado orden resuelven un problema.

Ejemplo de un algoritmo simple (pseudocódigo general):

.. code-block:: text

    Algoritmo (Nombre_algoritmo)
        Declaracion_de_variables
    INICIO
        INSTRUCCIÓN 1
        INSTRUCCIÓN 2
        INSTRUCCIÓN 3
        ...
        INSTRUCCIÓN N
    FIN_INICIO
    Fin (Nombre_algoritmo)

Características de los Algoritmos
---------------------------------
* **Preciso**: Indicar el orden de realización de cada paso.
* **Definido**: Si se sigue un algoritmo dos veces, se debe obtener el mismo resultado cada vez.
* **Finito**: Debe terminar en algún momento; tener un número finito de pasos.
* **Correcto**: El resultado del algoritmo debe ser el resultado esperado.
* **Independiente**: Del lenguaje de programación y de la computadora que lo ejecuta.

Entrada, Proceso y Salida
-------------------------
La definición de un algoritmo debe describir tres partes:

* **Entrada**: Datos con los que se cuenta.
* **Proceso**: Operaciones para transformar la entrada en salida.
* **Salida**: Resultados esperados.

.. todo::

    Expandir con Proceso, Acción y Estado, Tipos de Datos (Numéricos, Alfanuméricos, Lógicos),
    Variables, Constantes, Operadores (Asignación, Aritméticos, Relacionales, Lógicos),
    Prioridad, Prueba de Escritorio.

Tipos de Datos
--------------

En Pseudocódigo vamos a utilizar los siguientes tipos de datos:

Numéricos
~~~~~~~~~
Aquellos que representan una cantidad o valor determinado.

*   **Enteros**: Números completos, sin componentes fraccionarios o decimales.
    Ejemplos: ``10``, ``5``, ``0``, ``-234``.

    *Un dato que represente la edad de una persona, debe ser siempre del tipo Entero.*

*   **Reales**: Subconjunto de los números reales, siempre tienen un punto decimal.
    Ejemplos: ``0.345``, ``12.4``, ``-231.005``.

    *Un dato que represente el peso de una persona, debe ser siempre del tipo Real.*

Alfanuméricos
~~~~~~~~~~~~~
Datos que representan información textual (palabras, frases, símbolos, etc.).
No representan valor alguno para efectos numéricos.
Ejemplos: ``el nombre de una persona``, ``alguna frase cualquiera``.

Lógicos (Booleanos)
~~~~~~~~~~~~~~~~~~~
Dato que solo puede tomar uno de dos valores: Falso y Verdadero.
Ejemplo: *cuando se quiere determinar si un número es primo o no.*

Estructuras de Datos Simples
----------------------------

Variables
~~~~~~~~~
Elementos de almacenamiento de datos. Representan una dirección de memoria donde se almacena un dato,
cuyo contenido **puede variar** en el desarrollo del algoritmo.
Formato de definición:

.. code-block:: text

    nombre_variable: tipo_de_dato

Constantes
~~~~~~~~~~
Representan una zona de memoria donde se almacena un dato, pero su contenido **no puede modificarse**
durante la ejecución del algoritmo.

Operadores y Operandos
----------------------
Un **operador** es el símbolo que determina el tipo de operación o relación que habrá de establecerse
entre los **operandos** para alcanzar un resultado.

Operadores de Asignación
~~~~~~~~~~~~~~~~~~~~~~~~
Se utiliza para asignar un valor a una variable. El signo es ``:=``.
La acción de asignar es destructiva.

.. code-block:: text

    Edad := 29
    precio := 25.45

Operadores Aritméticos
~~~~~~~~~~~~~~~~~~~~~~
Son operadores binarios que realizan operaciones aritméticas.

*   ``+`` : Suma
*   ``-`` : Resta
*   ``*`` : Multiplicación
*   ``/`` : División real
*   ``MOD`` : Resto de la División entera
*   ``DIV`` : Cociente de la División entera

Operadores Relacionales
~~~~~~~~~~~~~~~~~~~~~~~
Sirven para realizar comparaciones. Proporcionan resultados lógicos (Verdadero/Falso).

*   ``=`` : Igual a
*   ``<>`` : No igual a
*   ``>`` : Mayor que
*   ``>=`` : Mayor o igual que
*   ``<`` : Menor que
*   ``<=`` : Menor o igual que

Formato: ``expresión1 operador_de_relación expresión2``

Operadores Lógicos
~~~~~~~~~~~~~~~~~~
Permiten la combinación de condiciones para formar una sola expresión lógica.

*   ``AND`` (``Y``, ``Λ``): Conjunción.

    *   ``V Y V -> V``
    *   ``V Y F -> F``
    *   ``F Y V -> F``
    *   ``F Y F -> F``

*   ``OR`` (``O``, ``v``): Disyunción.

    *   ``V O V -> V``
    *   ``V O F -> V``
    *   ``F O V -> V``
    *   ``F O F -> F``

*   ``NOT`` (``NO``): Negación.

Prioridad de los Operadores (General)
-------------------------------------
1.  Paréntesis ``()``
2.  Signo (``+``, ``-`` unarios), Negación (``NO``)
3.  Potencia (``**``)
4.  Multiplicación (``*``), División (``/``, ``DIV``), Módulo (``MOD``)
5.  Suma (``+``), Resta (``-``)
6.  Concatenación (``+`` para cadenas, si aplica)
7.  Relacionales (``<``, ``<=``, ``>``, ``>=``, ``=``, ``<>``)
8.  Conjunción (``Y``)
9.  Disyunción (``O``)

Prueba de Escritorio
--------------------
Comprobación de un algoritmo para saber si está bien realizado. Consiste en tomar datos
específicos como entrada y seguir la secuencia indicada hasta obtener un resultado.
Se realiza en base a una tabla con las variables como encabezados.

Ejemplo de tabla de prueba de escritorio:

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - ESTADO
     - a
     - b
     - suma
   * - E\ :sub:`o` = E\ :sub:`inicial`
     - ¿?
     - ¿?
     - ¿?
   * - E\ :sub:`1` (a := 2)
     - 2
     - ¿?
     - ¿?
   * - E\ :sub:`2` (b := 3)
     - 2
     - 3
     - ¿?
   * - E\ :sub:`3` (suma := a + b)
     - 2
     - 3
     - 5
   * - E\ :sub:`4` (suma := suma + 1)
     - 2
     - 3
     - 6