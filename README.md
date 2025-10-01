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



# 🧮 Calculadora Científica en Python

Una calculadora científica completa y elegante desarrollada en Python que funciona directamente en la terminal. Perfecta tanto para estudiantes, profesionales y entusiastas de las matemáticas.

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Funciones Disponibles](#-funciones-disponibles)
- [Ejemplos](#-ejemplos)
- [Estructura del Código](#-estructura-del-código)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Contacto](#-contacto)

## ✨ Características

### 📐 Operaciones Básicas
- ➕ **Suma**: Adición de dos números
- ➖ **Resta**: Sustracción de dos números
- ✖️ **Multiplicación**: Producto de dos números
- ➗ **División**: División con validación de división por cero
- 🔢 **Módulo**: Resto de división entre dos números

### 🔬 Operaciones Avanzadas
- 📈 **Potencia**: Eleva un número a cualquier potencia
- √ **Raíz Cuadrada**: Calcula raíces cuadradas
- ⁿ√ **Raíz n-ésima**: Calcula cualquier raíz (cúbica, cuarta, etc.)
- 📊 **Logaritmos**: Base 10, natural (ln) y base personalizada
- ❗ **Factorial**: Calcula el factorial de números enteros
- |x| **Valor Absoluto**: Obtiene el valor absoluto
- 🎯 **Redondeo**: Redondea a n decimales

### 📐 Funciones Trigonométricas
- 📏 **Seno, Coseno, Tangente**: Funciones trigonométricas directas
- 🔄 **Arcoseno, Arcocoseno, Arcotangente**: Funciones inversas
- 🌐 **Modo flexible**: Trabaja en grados o radianes

### 💎 Constantes Matemáticas
- π **Pi**: 3.14159265...
- e **Número de Euler**: 2.71828182...

### 🛡️ Características Adicionales
- ✅ **Validación robusta**: Manejo completo de errores
- 🎨 **Interfaz intuitiva**: Menú organizado por categorías
- 🔄 **Uso continuo**: Realiza múltiples operaciones sin reiniciar
- 📱 **Mensajes descriptivos**: Feedback claro en cada operación

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.6 o superior**
- Terminal o línea de comandos

Para verificar tu versión de Python:
```bash