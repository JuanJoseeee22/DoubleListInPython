#  DoubleListInPython

##  Descripción

Este proyecto implementa una **lista doblemente enlazada** en el lenguaje de programación Python, utilizando el paradigma de **Programación Orientada a Objetos (POO)**.

Una lista doblemente enlazada permite almacenar elementos de manera dinámica, donde cada nodo contiene una referencia al nodo siguiente y al nodo anterior, lo que permite recorrer la estructura en ambas direcciones.

---

## ¿Qué es una lista doblemente enlazada?

![Image](https://ccia.ugr.es/~jfv/ed1/tedi/cdrom/icons/lenlaz2.gif)

![Image](https://image.slidesharecdn.com/listasdoblementeenlazadas-160520020240/85/Listas-doblemente-enlazadas-2-320.jpg)


Es una estructura de datos compuesta por nodos, donde cada nodo tiene:

* Un dato
* Una referencia al siguiente nodo (`next`)
* Una referencia al nodo anterior (`prev`)

Esto permite:

* Recorrer la lista hacia adelante
* Recorrer la lista hacia atrás

---

##  Requisitos

Para ejecutar este proyecto necesitas:

* **Lenguaje:** Python
* **Versión recomendada:** Python 3.14.3 
* **Entorno:** Consola / terminal
* **Editor recomendado:** Visual Studio Code

### Librerías utilizadas:

* `typing` → Para manejo de tipos genéricos
* `unittest` → Para pruebas del sistema

(No se utilizan librerías externas)

---

##  Instalación

### 1. Instalar Python

1. Ir a la página oficial: https://www.python.org

2. Descargar Python

3. Durante la instalación, activar la opción:

   *  *Add Python to PATH*

4. Verificar instalación:

```bash
python --version
```

---

### 2. Instalar Visual Studio Code

1. Descargar desde: https://code.visualstudio.com
2. Instalar normalmente

---

### 3. Instalar extensión de Python en VS Code

1. Abrir VS Code
2. Ir a extensiones
3. Buscar: **Python**
4. Instalar la extensión oficial

---

##  Estructura del proyecto

```
DoubleListInPython/

│── model/
│   └── Node.py
    └── DoubleList.py
│── test/
│   └── TestDoubleList.py
│── README.md

```

---
##  Uso básico

Ejemplo de uso de la lista:

```python
from DoubleList import DoubleList

lista = DoubleList()

lista.add(10)
lista.add(20)
lista.add(30)

print(lista)
```

---
##  Ejecución de pruebas

El proyecto incluye pruebas unitarias usando `unittest`.

###  Opción 1: Desde Visual Studio Code

* Click derecho sobre la clase de prueba
* Seleccionar **Run Python**

---

###  Opción 2: Desde la terminal

#### Sin carpetas:

```bash
python -m TestDoubleList
```

#### Con carpetas:

```bash
python -m test.TestDoubleList
```

---

##  Resultado de ejecución

El sistema mostrará en consola:

* Número de pruebas ejecutadas
* Tiempo de ejecución
* Resultado final:

  *  **OK** → Todo funciona correctamente
  *  **FAIL** → Hay errores en las pruebas

---

##  Errores comunes

 **Python no reconocido como comando**

* Solución: verificar que Python esté en el PATH

 **Error al ejecutar pruebas**

* Verificar nombres de archivos
* Revisar estructura de carpetas

**VS Code no detecta Python**

* Seleccionar intérprete manualmente:

  * `Ctrl + Shift + P → Python: Select Interpreter`

---

##  Autor

* **Nombre:** Juan José Buitrago y Willian David Tocarruncho
* **Universidad:** UPTC (Universidad Pedagógica y Tecnológica de Colombia)
* **Programa:** Ingeniería de Sistemas

---

##  Notas finales

Este proyecto tiene como objetivo reforzar y conocer otro lenguaje de progrmación, como en este caso es Python, haciendo uso de estructuras de datos y el paradigma orientado a objetos, además de conocer las diferencias con el lenguaje usado normalmente (java), introduciendo el uso de pruebas unitarias para validar el correcto funcionamiento del sistema.
