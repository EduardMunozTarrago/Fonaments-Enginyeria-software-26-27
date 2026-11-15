print("Exercici 1")
for numero in range(1, 11):
    print(numero)

print("Exercici 2")
for numero in range(1, 21, 2):
    print(numero)

print("Exercici 3")
for numero in range(5, 51, 5):
    print(numero)

print("Exercici 4")
for numero in range(10, 0, -1):
    print(numero)

print("Exercici 5")
total = 0
for numero in range(1, 101):
    total += numero
print(total)

print("Exercici 6")
nombre = int(input("Introdueix un nombre: "))
for factor in range(1, 11):
    print(f"{nombre} x {factor} = {nombre * factor}")
