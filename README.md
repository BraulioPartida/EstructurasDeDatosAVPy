Este repositorio contiene dos tipos de estructuras de datos implementadas en Python:

-BloomFilter: Una estructura de datos de espacio eficiente que se utiliza para comprobar si un elemento está presente en un conjunto.

-Tries: Una estructura de datos jerárquica que se utiliza para almacenar datos asociados a una cadena.

BloomFilter

El BloomFilter es una estructura de datos de espacio eficiente que se utiliza para comprobar si un elemento está presente en un conjunto. Funciona almacenando un conjunto de bits, donde cada bit representa si un elemento está presente en el conjunto o no.

Para comprobar si un elemento está presente en el conjunto, se calcula un hash del elemento y se comprueba si el bit correspondiente al hash está establecido. Si el bit está establecido, entonces el elemento es probable que esté presente en el conjunto. Sin embargo, existe una pequeña probabilidad de que el bit esté establecido incluso si el elemento no está presente en el conjunto.

Tries

Los Tries son una estructura de datos jerárquica que se utiliza para almacenar datos asociados a una cadena. Funcionan almacenando los datos en un árbol, donde cada nodo del árbol representa una letra de la cadena.

Para acceder a los datos asociados a una cadena, se sigue el camino desde la raíz del árbol hasta el nodo que representa la última letra de la cadena.# EstructurasDeDatosAVPy
