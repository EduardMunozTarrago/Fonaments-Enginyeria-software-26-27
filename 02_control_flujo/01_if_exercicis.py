print("Ejercicio 1: el mayor de dos números")
primero = float(input("Primer número: "))
segundo = float(input("Segundo número: "))
if primero > segundo:
    print(f"El mayor es {primero:g}.")
elif segundo > primero:
    print(f"El mayor es {segundo:g}.")
else:
    print("Los dos números son iguales.")

print("\nEjercicio 2: calculadora simple")
numero_a = float(input("Primer número: "))
numero_b = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ").strip()
if operacion == "+":
    print(f"Resultado: {numero_a + numero_b:g}")
elif operacion == "-":
    print(f"Resultado: {numero_a - numero_b:g}")
elif operacion == "*":
    print(f"Resultado: {numero_a * numero_b:g}")
elif operacion == "/":
    if numero_b == 0:
        print("No se puede dividir entre cero.")
    else:
        print(f"Resultado: {numero_a / numero_b:g}")
else:
    print("Operación no válida. Usa +, -, * o /.")

print("\nEjercicio 3: año bisiesto")
anio = int(input("Año (entero positivo): "))
if anio <= 0:
    print("Año no válido: introduce un entero positivo.")
elif anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")

print("\nEjercicio 4: categorizar edades")
edad = int(input("Edad (años cumplidos): "))
if edad < 0:
    print("Edad no válida: no puede ser negativa.")
elif edad <= 2:
    print("Bebé")
elif edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")
