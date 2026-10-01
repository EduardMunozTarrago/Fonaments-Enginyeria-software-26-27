from math import pi

print("Exercici 1: imprimir missatges")
nom = input("El teu nom: ")
ciutat = input("La teva ciutat: ")
print(nom)
print(ciutat)

print("\nExercici 2: tipus de dades")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nExercici 3: conversió de tipus")
nombre_enter = int("12345")
nombre_decimal = float(nombre_enter)
enter_truncat = int(3.99)
print(nombre_enter, type(nombre_enter))
print(nombre_decimal, type(nombre_decimal))
print(enter_truncat)

print("\nExercici 4: variables")
edat = int(input("La teva edat (anys): "))
alcada = float(input("La teva alçada (metres): "))
print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alcada:g} metres.")

print("\nExercici 5: nombres")
print("PI:", pi)
pi_arrodonit = round(pi)
resultat = pi_arrodonit // 2
print("PI arrodonit:", pi_arrodonit)
print("Divisió entera entre 2:", resultat)

print("\nExercici 6: conversor de temperatura")
celsius = float(input("Temperatura en graus Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:g} graus Celsius equivalen a {fahrenheit:g} graus Fahrenheit.")

print("\nExercici 7: calculadora de propina")
compte = float(input("Total del compte (EUR): "))
percentatge = float(input("Percentatge de propina: "))
if compte < 0 or percentatge < 0:
    print("Dades no vàlides: el compte i el percentatge no poden ser negatius.")
else:
    propina = compte * percentatge / 100
    total = compte + propina
    print(f"Propina: {propina:.2f} EUR")
    print(f"Total final: {total:.2f} EUR")

print("\nExercici 8: validador de contrasenya simple")
contrasenya = input("Contrasenya de prova: ")
if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")
