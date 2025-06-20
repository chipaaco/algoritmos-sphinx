Estructuras de Datos Complejas (Campo, Registro, Archivo)
=======================================================

Concepto de Campo
-----------------
Un **campo** es un conjunto de caracteres capaz de suministrar una determinada información referida a un
concepto. Es la entidad lógica más pequeña, un conjunto de bytes que conforman un dato.
Características:
*   **Nombre**: Identificador del campo.
*   **Tipo**: Tipo de caracteres que puede contener (alfabético, entero, etc.).
*   **Tamaño**: Cantidad de caracteres que puede contener.

Ejemplo de definición (conceptual):
`dni : N (8)` (Nombre: dni, Tipo: Numérico, Tamaño: 8)

Registro
--------
Un **registro** es un conjunto de campos que permanecen juntos y se tratan como una unidad.
Se define en el AMBIENTE para ser usado en el algoritmo.

Definición de un Tipo Registro:
.. code-block:: text

    PERSONA = Registro
        DNI: Entero;
        Nombre: AN(50); // Alfanumérico de 50 caracteres
        Domicilio: AN(70);
    Fin Registro

Uso de un Registro:
Primero, se declara una variable del tipo registro definido:
.. code-block:: text

    // En el AMBIENTE del algoritmo principal o subacción
    RegAlumno: PERSONA

Luego, se accede a sus campos usando el selector de campo (`.`):
.. code-block:: text

    RegAlumno.DNI := 12345678;
    LEER(NroDNI);
    RegAlumno.DNI := NroDNI;
    ESCRIBIR(RegAlumno.Nombre);

Archivos
--------
Un **archivo** es un conjunto de registros que, una vez almacenados (generalmente en memoria externa),
se pueden utilizar a través de distintas aplicaciones.

Características Generales de los Archivos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.  Almacenados en **memoria externa** (permanente). Proceso en memoria interna.
2.  **Independencia** de los datos respecto a los algoritmos que los usan.
3.  Unidad básica de entrada/salida es el **registro completo**.
4.  Gran capacidad de almacenamiento.

Consistencia y Congruencia de Archivos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*   **Consistencia**: Verifica la validez del dato almacenado con su definición en el ambiente (tipo, rango).
    Ej: `FECHA = Registro DD: 1..31; MM: 1..12; AAAA: Entero; Fin Registro;`
    `RegFecha = (02/12/2019)` es consistente.
    `RegFecha = (50/50/9999)` es inconsistente.

*   **Congruencia**: Verifica la validez de los datos entre sí.
    *   **Fina**: Validación entre datos en archivos distintos.
        Ej: DNI en archivo ALUMNOS validado con archivo PADRON.
    *   **Gruesa**: Validación entre datos en un mismo registro.
        Ej: `RegFecha = (31/02/2019)` es consistente (cada campo individualmente), pero no congruente (febrero no tiene 31 días).

Clasificación de Archivos por su Contenido
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  **De acuerdo a su utilidad**:
    *   **De Entrada**: Compuestos por datos almacenados en un dispositivo de entrada.
    *   **De Salida**: Contienen información que se visualiza desde la computadora.
    *   **Históricos (o Maestros)**: Datos que varían en el tiempo, con información actualizada.
    *   **De Movimiento (o Transacciones)**: Se usan con archivos constantes/maestros, poseen campos en común para actualizar.
    *   **Temporales (o Auxiliares)**: Se crean durante la ejecución de un programa y se borran al finalizar.

2.  **De acuerdo a sus datos almacenados**:
    *   **ASCII (o de Texto)**: Datos almacenados como texto simple. Permite intercambio y modificación manual.
    *   **Binarios**: Almacena información en un lenguaje que solo la computadora comprende (colores, sonidos, imágenes, órdenes). Menor peso que los ASCII.

Organización de Archivos
------------------------
Manera en que se encuentran almacenados los registros en el archivo. Depende de los **soportes**:
*   **Soportes Secuenciales**: Registros escritos uno a continuación del otro. Para acceder al registro N, se deben recorrer N-1 anteriores.
*   **Soportes Direccionables**: Información localizada por su dirección. Registros deben tener una **clave** única.

Tipos de Organización:
1.  **Secuencial**: Sucesión de registros almacenados consecutivamente (continuidad física). Para acceder a un registro `n`, se deben pasar por los `n-1` anteriores.
    Común en soportes secuenciales (cintas) y direccionables (discos).

2.  **Relativa (o Directa)**: El orden físico no necesariamente corresponde al lógico. Se accede por su posición (lugar relativo). Necesita soporte direccionable, campo clave y relación clave-dirección.
    Permite huecos o espacios libres intermedios.

    .. code-block:: text

        // Dir. memoria | Clave | Datos
        // 1            |       |
        // 2            | 2     | Registro 'A'
        // 3            |       |
        // 4            | 4     | Registro 'B'
        // 5            | 5     | Registro 'C'

3.  **Indexada (o Secuencial Indexada)**: Consta de un archivo de datos y un archivo índice.
    *   **Área de datos (o primaria)**: Registros en forma secuencial por clave, sin huecos.
    *   **Área de índices**: Tabla con niveles de índice que apuntan a bloques/registros en el área de datos.

        Ejemplo conceptual:
        Área de Índices:
        Clave | Dirección (en archivo de datos)
        15    | 010
        24    | 020
        36    | 030
        ...

        Área de Datos (en dirección 010):
        010 | 15 | Datos del registro 15
        011 | .. | Siguiente registro secuencial
        ...

Acceso de Archivos
------------------
Manera en que se recuperan (leen) los registros.
1.  **Acceso Secuencial**: Acceso según el orden de almacenamiento, uno tras otro.
2.  **Acceso Directo**: Acceso a un registro determinado sin consultar precedentes. Solo con soportes direccionables.
3.  **Acceso Mixto**: Acceso directo a un registro y posterior acceso secuencial a los siguientes.