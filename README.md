# DoubleListInPython

1. La aplicación se desarrollo en el lenguaje de programación de Python, utilizando la estructura de datos lista doblemente enlazada mediante las clases genéricas. 

La estructura principal es la DoubleList, utilizando Nodos que contienen la referencia hacia su nodo siguiente y anterior. Así recorrer la lista en ambas direcciones. 

El paradigma utilizado es la Programación Orientada a Objetos (POO). 

2. Para la ejecución se requiere de:
Lenguaje: Python
Versión recomendada: Python 3.14.3 
Entorno de ejecución: Consola o terminal del sistema operativo. 
No se hace uso de librerías externas, se utilizan los módulos estándar de Python exactamente typing (para los tipos genéricos) y unittest (para la clase de prueba). 
Se utiliza el editor de código Visual Studio Code con su extension para el lenguaje Python. 

3. Para ejecutar la clase de prueba se puede de dos maneras.

- Presionando click derecho estando en la clase de prueba y dando en la opción de Run Python. Esta opción funciona cuando las clases no están separadas en carpetas. 

- Abriendo el terminal y colocando el archivo de pruebas con el siguiente comando
sin carpeta: python -m TestDoubleList 
con carpetas: python -m test.TestDoubleList
Esta opción funciona con carpetas y sin carpetas 

El sistema en cualquiera de los 2 casos ejecutara todos los métodos de prueba y se mostrara en consola según sea el caso. El número de pruebas ejecutadas, el tiempo de ejecución y el resultado (OK si todo esta bien y FAIL si hay errores).