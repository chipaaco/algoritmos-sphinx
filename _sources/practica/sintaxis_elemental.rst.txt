Cheatsheet de Sintaxis de Pseudocódigo
=======================================

Declaración de Variables y Constantes
-------------------------------------
.. code-block:: text

    nombre_variable: tipo_de_dato
    // Ejemplo:
    edad: entero
    nombre: alfanumerico

Constantes:
    // No se modifica durante la ejecución

Tipos de Datos
--------------
* entero
* real
* alfanumerico
* logico

Operadores
----------
Asignación:
    :=
Aritméticos:
    +  -  *  /  MOD  DIV
Relacionales:
    =  <>  >  >=  <  <=
Lógicos:
    AND  OR  NOT

Estructuras de Control
----------------------
Secuencial:
    // Una instrucción tras otra

Condicional Simple:
.. code-block:: text

    SI <condición> ENTONCES
        <acciones>
    FIN_SI

Condicional Doble:
.. code-block:: text

    SI <condición> ENTONCES
        <acciones_si_verdadero>
    SINO
        <acciones_si_falso>
    FIN_SI

Condicional Múltiple:
.. code-block:: text

    SEGÚN <variable> HACER
        <valor1>: <acciones>
        <valor2>: <acciones>
        ...
    FIN_SEGUN

Bucle PRE-TEST (MIENTRAS):
.. code-block:: text

    MIENTRAS <condición> HACER
        <acciones>
    FIN_MIENTRAS

Bucle POST-TEST (REPETIR):
.. code-block:: text

    REPETIR
        <acciones>
    HASTA QUE <condición>

Bucle POR CONTADOR (PARA):
.. code-block:: text

    PARA <var> := <inicio> HASTA <fin> [INCREMENTO <paso>] HACER
        <acciones>
    FIN_PARA

Subacciones
-----------
Función:
.. code-block:: text

    FUNCION <nombre>(<parámetros>): <tipo>
    AMBIENTE
        <declaraciones>
    PROCESO
        <acciones>
        <nombre> := <valor>
    FIN_FUNCION

Procedimiento:
.. code-block:: text

    PROCEDIMIENTO <nombre>(<parámetros>)
    PROCESO
        <acciones>
    FIN_PROCEDIMIENTO

Registros
---------
Definición:
.. code-block:: text

    <NOMBRE> = Registro
        <campo1>: <tipo>;
        <campo2>: <tipo>;
    Fin Registro

Uso:
.. code-block:: text

    variable: <NOMBRE>
    variable.campo := valor

Archivos y Secuencias
---------------------
Operaciones básicas:
.. code-block:: text

    ARR(secuencia)         // Abrir para lectura
    AVZ(secuencia, var)    // Avanzar y leer
    CREAR(secuencia)       // Crear para escritura
    ESC(secuencia, var)    // Escribir elemento
    CERRAR(secuencia)      // Cerrar

Prueba de Escritorio
--------------------
.. list-table::
   :widths: 20 20 20
   :header-rows: 1

   * - Estado
     - a
     - b
   * - E0
     - ?
     - ?
   * - E1 (a := 2)
     - 2
     - ?
   * - E2 (b := 3)
     - 2
     - 3

Notas
-----
- Los nombres de variables y subacciones deben ser representativos.
- La indentación es solo para claridad visual.
- Consultar los apuntes para detalles y ejemplos completos.
