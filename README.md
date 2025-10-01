\# 🧮 Calculadora en Python


🌐 **[Ver versión web](https://pepegamboa.github.io/calculator/)**

Una calculadora simple y elegante desarrollada en Python...

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/PepeGamboa/calculator?style=social)](https://github.com/PepeGamboa/calculator/stargazers)

Una calculadora simple y elegante desarrollada en Python que funciona directamente en la terminal. Perfecta para principiantes que quieren aprender programación y conceptos básicos de Python.

Una calculadora simple y elegante desarrollada en Python que funciona directamente en la terminal. Perfecta para principiantes que quieren aprender programación y conceptos básicos de Python.



\## 📋 Tabla de Contenidos



\- \[Características](#-características)

\- \[Requisitos Previos](#-requisitos-previos)

\- \[Instalación](#-instalación)

\- \[Uso](#-uso)

\- \[Estructura del Código](#-estructura-del-código)

\- \[Ejemplos](#-ejemplos)

\- \[Contribuir](#-contribuir)

\- \[Licencia](#-licencia)

\- \[Contacto](#-contacto)



\## ✨ Características



\- ➕ \*\*Suma\*\*: Adición de dos números

\- ➖ \*\*Resta\*\*: Sustracción de dos números

\- ✖️ \*\*Multiplicación\*\*: Producto de dos números

\- ➗ \*\*División\*\*: División con validación de división por cero

\- 🎯 \*\*Interfaz Simple\*\*: Fácil de usar en la terminal

\- 🔄 \*\*Uso Continuo\*\*: Realiza múltiples operaciones sin reiniciar

\- 🛡️ \*\*Manejo de Errores\*\*: Validación de entradas y operaciones



\## 🔧 Requisitos Previos



Antes de comenzar, asegúrate de tener instalado:



\- Python 3.6 o superior

\- Terminal o línea de comandos



Para verificar tu versión de Python:



```bash

python --version

\# o

python3 --version

```



\## 📥 Instalación



\### Opción 1: Clonar el repositorio



```bash

\# Clona este repositorio

git clone https://github.com/PepeGamboa/calculator.git



\# Navega al directorio del proyecto

cd calculator

```



\### Opción 2: Descarga directa



Descarga el archivo `calculator.py` directamente desde este repositorio y guárdalo en tu computadora.



\## 🚀 Uso



Ejecuta la calculadora desde tu terminal:



```bash

python calculator.py

```



O si tienes Python 3:



```bash

python3 calculator.py

```



\### Instrucciones de uso:



1\. Ingresa el primer número cuando se te solicite

2\. Ingresa el segundo número

3\. Selecciona la operación que deseas realizar:

&nbsp;  - `1` para Suma

&nbsp;  - `2` para Resta

&nbsp;  - `3` para Multiplicación

&nbsp;  - `4` para División

4\. Ve el resultado en pantalla

5\. Decide si quieres realizar otra operación



\## 🏗️ Estructura del Código



El proyecto está organizado con funciones modulares para cada operación:



```python

def suma(a, b):

&nbsp;   """Retorna la suma de a y b"""

&nbsp;   return a + b



def resta(a, b):

&nbsp;   """Retorna la resta de a menos b"""

&nbsp;   return a - b



def multiplicacion(a, b):

&nbsp;   """Retorna el producto de a y b"""

&nbsp;   return a \* b



def division(a, b):

&nbsp;   """Retorna la división de a entre b con validación"""

&nbsp;   if b == 0:

&nbsp;       return "Error: División por cero no permitida"

&nbsp;   return a / b

```



\### Flujo del Programa:



```

Inicio

&nbsp; ↓

Solicitar números

&nbsp; ↓

Mostrar menú de operaciones

&nbsp; ↓

Ejecutar operación seleccionada

&nbsp; ↓

Mostrar resultado

&nbsp; ↓

¿Continuar? → Sí → (volver a Solicitar números)

&nbsp; ↓

&nbsp; No

&nbsp; ↓

Fin

```



\## 💡 Ejemplos



\### Ejemplo 1: Suma



```

Ingresa el primer número: 15

Ingresa el segundo número: 27



Selecciona una operación:

1\. Suma

2\. Resta

3\. Multiplicación

4\. División



Elige una opción (1-4): 1



Resultado: 15 + 27 = 42

```



\### Ejemplo 2: División



```

Ingresa el primer número: 100

Ingresa el segundo número: 4



Selecciona una operación:

1\. Suma

2\. Resta

3\. Multiplicación

4\. División



Elige una opción (1-4): 4



Resultado: 100 / 4 = 25.0

```



\### Ejemplo 3: División por cero



```

Ingresa el primer número: 10

Ingresa el segundo número: 0



Selecciona una operación:

1\. Suma

2\. Resta

3\. Multiplicación

4\. División



Elige una opción (1-4): 4



Resultado: Error: División por cero no permitida

```



\## 🎓 Conceptos de Programación Incluidos



Este proyecto es ideal para aprender:



\- \*\*Funciones\*\*: Modularización y reutilización de código

\- \*\*Condicionales\*\*: Estructuras if/elif/else

\- \*\*Bucles\*\*: Implementación de while para operaciones continuas

\- \*\*Entrada/Salida\*\*: Interacción con el usuario mediante input() y print()

\- \*\*Manejo de Errores\*\*: Validación de operaciones incorrectas

\- \*\*Tipos de Datos\*\*: Trabajo con números enteros y flotantes



\## 🤝 Contribuir



¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:



1\. Haz un Fork del proyecto

2\. Crea una rama para tu función (`git checkout -b feature/NuevaFuncion`)

3\. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva función'`)

4\. Sube los cambios a tu rama (`git push origin feature/NuevaFuncion`)

5\. Abre un Pull Request



\### Ideas para contribuir:



\- Agregar más operaciones (potencia, raíz cuadrada, módulo)

\- Implementar una interfaz gráfica (GUI)

\- Agregar historial de operaciones

\- Incluir operaciones con múltiples números

\- Mejorar el manejo de excepciones



\## 📝 Licencia



Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.



\## 👤 Contacto



\*\*Pepe Gamboa\*\*



\- GitHub: \[@PepeGamboa](https://github.com/PepeGamboa)

\- Repositorio: \[https://github.com/PepeGamboa/calculator](https://github.com/PepeGamboa/calculator)



---



⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub



📚 Perfecto para principiantes en Python | 🚀 Proyecto educativo



\*\*Hecho con ❤️ y Python\*\*

