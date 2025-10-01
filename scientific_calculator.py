import math

# Operaciones básicas
def suma(a, b):
    """Retorna la suma de a y b"""
    return a + b

def resta(a, b):
    """Retorna la resta de a menos b"""
    return a - b

def multiplicacion(a, b):
    """Retorna el producto de a y b"""
    return a * b

def division(a, b):
    """Retorna la división de a entre b con validación"""
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

# Operaciones científicas
def potencia(a, b):
    """Retorna a elevado a la potencia b"""
    return a ** b

def raiz_cuadrada(a):
    """Retorna la raíz cuadrada de a"""
    if a < 0:
        return "Error: No se puede calcular raíz cuadrada de número negativo"
    return math.sqrt(a)

def raiz_n(a, n):
    """Retorna la raíz n-ésima de a"""
    if a < 0 and n % 2 == 0:
        return "Error: No se puede calcular raíz par de número negativo"
    return a ** (1/n)

def logaritmo(a, base=10):
    """Retorna el logaritmo de a en la base especificada (por defecto base 10)"""
    if a <= 0:
        return "Error: El logaritmo solo acepta números positivos"
    if base <= 0 or base == 1:
        return "Error: Base de logaritmo inválida"
    return math.log(a, base)

def logaritmo_natural(a):
    """Retorna el logaritmo natural (ln) de a"""
    if a <= 0:
        return "Error: El logaritmo solo acepta números positivos"
    return math.log(a)

def seno(a, grados=True):
    """Retorna el seno de a (por defecto en grados)"""
    angulo = math.radians(a) if grados else a
    return math.sin(angulo)

def coseno(a, grados=True):
    """Retorna el coseno de a (por defecto en grados)"""
    angulo = math.radians(a) if grados else a
    return math.cos(angulo)

def tangente(a, grados=True):
    """Retorna la tangente de a (por defecto en grados)"""
    angulo = math.radians(a) if grados else a
    return math.tan(angulo)

def arcoseno(a, grados=True):
    """Retorna el arcoseno de a"""
    if a < -1 or a > 1:
        return "Error: El valor debe estar entre -1 y 1"
    resultado = math.asin(a)
    return math.degrees(resultado) if grados else resultado

def arcocoseno(a, grados=True):
    """Retorna el arcocoseno de a"""
    if a < -1 or a > 1:
        return "Error: El valor debe estar entre -1 y 1"
    resultado = math.acos(a)
    return math.degrees(resultado) if grados else resultado

def arcotangente(a, grados=True):
    """Retorna la arcotangente de a"""
    resultado = math.atan(a)
    return math.degrees(resultado) if grados else resultado

def factorial(n):
    """Retorna el factorial de n"""
    if n < 0:
        return "Error: El factorial no está definido para números negativos"
    if not isinstance(n, int):
        return "Error: El factorial solo acepta números enteros"
    return math.factorial(n)

def modulo(a, b):
    """Retorna el módulo (resto) de a dividido por b"""
    if b == 0:
        return "Error: División por cero no permitida"
    return a % b

def valor_absoluto(a):
    """Retorna el valor absoluto de a"""
    return abs(a)

def redondeo(a, decimales=0):
    """Retorna a redondeado a n decimales"""
    return round(a, decimales)

def mostrar_menu():
    """Muestra el menú de operaciones disponibles"""
    print("\n" + "="*60)
    print("🧮 CALCULADORA CIENTÍFICA".center(60))
    print("="*60)
    print("\n📐 OPERACIONES BÁSICAS:")
    print("  1.  Suma")
    print("  2.  Resta")
    print("  3.  Multiplicación")
    print("  4.  División")
    print("  5.  Módulo (resto)")
    
    print("\n🔬 OPERACIONES AVANZADAS:")
    print("  6.  Potencia (a^b)")
    print("  7.  Raíz cuadrada")
    print("  8.  Raíz n-ésima")
    print("  9.  Logaritmo (base 10)")
    print("  10. Logaritmo natural (ln)")
    print("  11. Logaritmo (base personalizada)")
    
    print("\n📊 FUNCIONES TRIGONOMÉTRICAS:")
    print("  12. Seno")
    print("  13. Coseno")
    print("  14. Tangente")
    print("  15. Arcoseno")
    print("  16. Arcocoseno")
    print("  17. Arcotangente")
    
    print("\n🎯 OTRAS FUNCIONES:")
    print("  18. Factorial")
    print("  19. Valor absoluto")
    print("  20. Redondeo")
    
    print("\n💾 CONSTANTES:")
    print("  21. Mostrar π (pi)")
    print("  22. Mostrar e (número de Euler)")
    
    print("\n  0.  Salir")
    print("="*60)

def calculadora():
    """Función principal de la calculadora"""
    print("\n¡Bienvenido a la Calculadora Científica! 🎓")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\n👉 Elige una opción (0-22): "))
            
            if opcion == 0:
                print("\n✨ ¡Gracias por usar la calculadora! Hasta pronto. 👋\n")
                break
            
            elif opcion == 21:
                print(f"\n🔢 π (pi) = {math.pi}")
                input("\nPresiona Enter para continuar...")
                continue
            
            elif opcion == 22:
                print(f"\n🔢 e (número de Euler) = {math.e}")
                input("\nPresiona Enter para continuar...")
                continue
            
            # Operaciones con dos números
            elif opcion in [1, 2, 3, 4, 5, 6, 8, 11]:
                a = float(input("\nIngresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                
                if opcion == 1:
                    resultado = suma(a, b)
                    print(f"\n✅ Resultado: {a} + {b} = {resultado}")
                elif opcion == 2:
                    resultado = resta(a, b)
                    print(f"\n✅ Resultado: {a} - {b} = {resultado}")
                elif opcion == 3:
                    resultado = multiplicacion(a, b)
                    print(f"\n✅ Resultado: {a} × {b} = {resultado}")
                elif opcion == 4:
                    resultado = division(a, b)
                    print(f"\n✅ Resultado: {a} ÷ {b} = {resultado}")
                elif opcion == 5:
                    resultado = modulo(a, b)
                    print(f"\n✅ Resultado: {a} mod {b} = {resultado}")
                elif opcion == 6:
                    resultado = potencia(a, b)
                    print(f"\n✅ Resultado: {a}^{b} = {resultado}")
                elif opcion == 8:
                    resultado = raiz_n(a, b)
                    print(f"\n✅ Resultado: raíz {b} de {a} = {resultado}")
                elif opcion == 11:
                    resultado = logaritmo(a, b)
                    print(f"\n✅ Resultado: log base {b} de {a} = {resultado}")
            
            # Operaciones con un número
            elif opcion in [7, 9, 10, 18, 19, 20]:
                a = float(input("\nIngresa el número: "))
                
                if opcion == 7:
                    resultado = raiz_cuadrada(a)
                    print(f"\n✅ Resultado: √{a} = {resultado}")
                elif opcion == 9:
                    resultado = logaritmo(a)
                    print(f"\n✅ Resultado: log₁₀({a}) = {resultado}")
                elif opcion == 10:
                    resultado = logaritmo_natural(a)
                    print(f"\n✅ Resultado: ln({a}) = {resultado}")
                elif opcion == 18:
                    if a != int(a):
                        print("\n❌ Error: El factorial solo acepta números enteros")
                    else:
                        resultado = factorial(int(a))
                        print(f"\n✅ Resultado: {int(a)}! = {resultado}")
                elif opcion == 19:
                    resultado = valor_absoluto(a)
                    print(f"\n✅ Resultado: |{a}| = {resultado}")
                elif opcion == 20:
                    decimales = int(input("¿A cuántos decimales deseas redondear?: "))
                    resultado = redondeo(a, decimales)
                    print(f"\n✅ Resultado: {a} redondeado a {decimales} decimales = {resultado}")
            
            # Funciones trigonométricas
            elif opcion in [12, 13, 14, 15, 16, 17]:
                a = float(input("\nIngresa el ángulo/valor: "))
                
                if opcion in [12, 13, 14]:
                    modo = input("¿Grados (g) o Radianes (r)? [g]: ").lower() or 'g'
                    grados = modo == 'g'
                else:
                    modo = input("¿Resultado en Grados (g) o Radianes (r)? [g]: ").lower() or 'g'
                    grados = modo == 'g'
                
                if opcion == 12:
                    resultado = seno(a, grados)
                    unidad = "°" if grados else "rad"
                    print(f"\n✅ Resultado: sen({a}{unidad}) = {resultado}")
                elif opcion == 13:
                    resultado = coseno(a, grados)
                    unidad = "°" if grados else "rad"
                    print(f"\n✅ Resultado: cos({a}{unidad}) = {resultado}")
                elif opcion == 14:
                    resultado = tangente(a, grados)
                    unidad = "°" if grados else "rad"
                    print(f"\n✅ Resultado: tan({a}{unidad}) = {resultado}")
                elif opcion == 15:
                    resultado = arcoseno(a, grados)
                    unidad = "°" if grados else "rad"
                    print(f"\n✅ Resultado: arcsen({a}) = {resultado}{unidad}")
                elif opcion == 16:
                    resultado = arcocoseno(a, grados)
                    unidad = "°" if grados else "rad"
                    print(f"\n✅ Resultado: arccos({a}) = {resultado}{unidad}")
                elif opcion == 17:
                    resultado = arcotangente(a, grados)
                    unidad = "°" if grados else "rad"
                    print(f"\n✅ Resultado: arctan({a}) = {resultado}{unidad}")
            
            else:
                print("\n❌ Opción no válida. Por favor, elige un número entre 0 y 22.")
            
            input("\nPresiona Enter para continuar...")
            
        except ValueError:
            print("\n❌ Error: Por favor, ingresa un valor numérico válido.")
            input("\nPresiona Enter para continuar...")
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    calculadora()