Subacciones (Funciones y Procedimientos)
========================================

La resolución de problemas complejos se facilita dividiéndolos en problemas más pequeños,
cuya resolución se realiza mediante subalgoritmos o subacciones.

Características
---------------
*   Son acciones que forman parte de una ACCIÓN PRINCIPAL.
*   Módulos escritos para ejecutar alguna tarea específica.
*   Se definen en el AMBIENTE y se invocan en el PROCESO.
*   Se escriben una vez, pero pueden ser referenciados múltiples veces.

Control de Ejecución
--------------------
Cuando el algoritmo principal realiza la solicitud a una subacción, se detiene hasta que
la subacción termina su tarea, y luego continúa.

Elementos de las Subacciones
----------------------------
*   **Nombre**: Único y representativo. No debe ser palabra reservada.
*   **Parámetros**: Variables y/o constantes para pasar datos entre el algoritmo principal y la subacción.

    *   **Parámetros formales (o ficticios)**: Los que aparecen en la definición de la subacción. *Solo pueden ser variables*.
    *   **Parámetros actuales (o argumentos)**: Los que se usan en la llamada a la subacción. *Pueden ser constantes, variables, expresiones*.

Funciones
---------
Una FUNCIÓN es un subalgoritmo que recibe argumentos (parámetros actuales) y **devuelve un único resultado**.

*   **Funciones Internas (o intrínsecas predefinidas)**: Incorporadas al sistema/lenguaje.
*   **Funciones Externas**: Definidas por el usuario.

Declaración de Funciones (Pseudocódigo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    Funcion <nombrefun>(<lista_de_parámetros_formales>): <Tipo_de_retorno>
        // Ambiente local de la función (variables locales si son necesarias)
        <declaraciones_locales>
    PROCESO // Acciones de la función
        <acciones>
        <nombrefun> := <valor_de_la_funcion> // Asignación del resultado
    Fin Funcion

*   `<nombrefun>`: Nombre de la función.
*   `<lista_de_parámetros_formales>`: Lista de parámetros formales. *No puede ser vacía*.
*   `<Tipo_de_retorno>`: Tipo del resultado que devuelve la función.

Ejemplo de Función:

.. code-block:: text

    FUNCION ES_PRIMO(A:entero):lógico
    AMBIENTE
        i: entero
    PROCESO
        ES_PRIMO := V // Habilito la función como bandera (asumo que es primo)
        PARA i:=2 HASTA (A-1) HACER // Podría optimizarse hasta raiz(A)
            SI A MOD i = 0 ENTONCES
                ES_PRIMO := F // Ya no es primo
                // Se podría agregar SALIR_PARA para optimizar
            FIN_SI
        FIN_PARA
        // Considerar caso A < 2, no es primo. El bucle PARA no se ejecuta.
        // Si A es 2 o 3, el bucle PARA no se ejecuta, ES_PRIMO queda en V (correcto).
    FIN_FUNCION

Procedimientos
--------------
Un PROCEDIMIENTO también es una subacción, diseñado con un fin específico, pero a diferencia
de las funciones, **no devuelve ningún valor directamente**, solo ejecuta acciones.

Declaración de Procedimientos (Pseudocódigo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    Procedimiento <nombreproc>(<lista_de_parámetros_formales>)
        // Ambiente local del procedimiento
        <declaraciones_locales>
    PROCESO // Acciones del procedimiento
        <acciones>
    Fin Procedimiento

Ejemplo de Procedimiento:

.. code-block:: text

    PROCEDIMIENTO Login(usu, pass, valid: alfanumerico) // Asumiendo que valid es la contraseña correcta
    PROCESO
        Si pass = valid entonces
            ESC('Acceso autorizado a ', usu)
        Sino
            Esc('Login inválido para ', usu)
        FinSi
    FIN_PROCEDIMIENTO

Ámbitos de Variables
--------------------
*   **Variables Locales**: Declaradas dentro de una subacción. Conocidas solo dentro de esa subacción.
    Los parámetros de una subacción también son variables locales.
*   **Variables Globales**: Declaradas en el algoritmo principal. Pueden ser utilizadas en el algoritmo
    principal y en todas las subacciones declaradas en él.

Paso de Parámetros
------------------
Proceso por el cual el algoritmo principal envía variables a una subacción.

Paso de Parámetros por Valor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Se pasa una **copia** del valor del parámetro actual al parámetro formal.
La subacción trabaja con esta copia. Cualquier modificación al parámetro dentro de la subacción
**no afecta** a la variable original en el algoritmo llamador.
Es el método predominante en los ejemplos de la cátedra.

.. figure:: _static/paso_por_valor.png
   :alt: Esquema de paso de parámetros por valor
   :align: center
   :width: 400px

   Esquema conceptual del paso de parámetros por valor.

*(Asegúrate de que `paso_por_valor.png` esté en `docs/source/_static/`. He cambiado `.. image::` por `.. figure::` para poder añadirle una leyenda, lo cual es buena práctica y Furo lo maneja bien).*