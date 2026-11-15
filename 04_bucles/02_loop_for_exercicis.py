print("Exercici 1")
for numero in range(2, 21, 2):
    print(numero)

print("Exercici 2")
numeros = [10, 20, 30, 40, 50]
total = 0
for numero in numeros:
    total += numero
print("Mitjana:", total / len(numeros))

print("Exercici 3")
numeros = [15, 5, 25, 10, 20]
maxim = numeros[0]
for numero in numeros:
    if numero > maxim:
        maxim = numero
print("Màxim:", maxim)

print("Exercici 4")
paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
llargues = []
for paraula in paraules:
    if len(paraula) > 5:
        llargues.append(paraula)
print("Amb for:", llargues)
print("Amb comprensió:", [paraula for paraula in paraules if len(paraula) > 5])

print("Exercici 5")
paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra = input("Introdueix una lletra: ").strip().lower()
comptador = 0
if len(lletra) == 1:
    for paraula in paraules:
        if paraula.lower().startswith(lletra):
            comptador += 1
    print("Paraules trobades:", comptador)
else:
    print("Cal introduir una sola lletra.")

print("Exercici 6")
tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
total = 0
for tensio in tensions:
    total += tensio
print("Tensió mitjana:", total / len(tensions), "V")

print("Exercici 7")
for resistencia in [100, 220, 470, 1000]:
    print(f"{resistencia} ohms: {12 / resistencia:.6f} A")

print("Exercici 8")
comptador = 0
for nivell in [-92, -85, -78, -95, -81, -88]:
    if nivell > -80:
        comptador += 1
print("Mostres que superen el llindar:", comptador)

print("Exercici 9")
transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
rebuts = [1, 0, 0, 1, 0, 1, 1, 0]
errors = 0
for index in range(len(transmesos)):
    if transmesos[index] != rebuts[index]:
        errors += 1
print("Bits diferents:", errors)
print("Taxa d'error:", errors / len(transmesos))

print("Exercici 10")
for frequencia in [50, 100, 500, 1000]:
    print(f"{frequencia} Hz: {1 / frequencia:g} s")
