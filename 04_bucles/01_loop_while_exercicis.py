print("Exercici 1")
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1

print("Exercici 2")
numero = 2
suma = 0
while numero <= 20:
    suma += numero
    numero += 2
print("Suma de parells:", suma)

print("Exercici 3")
numero = int(input("Nombre enter no negatiu: "))
if numero < 0:
    print("El factorial només està definit aquí per a enters no negatius.")
else:
    resultat = 1
    factor = 1
    while factor <= numero:
        resultat *= factor
        factor += 1
    print("Factorial:", resultat)

print("Exercici 4")
contrasenya = input("Contrasenya de prova (8 caràcters o més): ")
while len(contrasenya) < 8:
    contrasenya = input("Massa curta. Torna-ho a provar: ")
print("Contrasenya vàlida")

print("Exercici 5")
numero = int(input("Nombre per a la taula: "))
factor = 1
while factor <= 10:
    print(f"{numero} x {factor} = {numero * factor}")
    factor += 1

print("Exercici 6")
limit = int(input("Mostra els primers fins a: "))
numero = 2
while numero <= limit:
    divisor = 2
    primer = True
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            primer = False
            break
        divisor += 1
    if primer:
        print(numero)
    numero += 1

print("Exercici 7")
total = 0
numero = int(input("Enter (0 per acabar): "))
while numero != 0:
    total += numero
    numero = int(input("Enter (0 per acabar): "))
print("Suma total:", total)

print("Exercici 8")
numero = int(input("Enter positiu: "))
if numero < 0:
    print("Cal un enter no negatiu.")
else:
    xifres = 1 if numero == 0 else 0
    while numero > 0:
        numero //= 10
        xifres += 1
    print("Nombre de xifres:", xifres)

print("Exercici 9")
termes = int(input("Quants termes de Fibonacci vols veure? "))
anterior = 0
actual = 1
comptador = 0
while comptador < termes:
    print(anterior)
    anterior, actual = actual, anterior + actual
    comptador += 1

print("Exercici 10")
secret = 7
intent = int(input("Endevina el nombre secret: "))
while intent != secret:
    if intent < secret:
        print("El nombre secret és més gran.")
    else:
        print("El nombre secret és més petit.")
    intent = int(input("Torna-ho a provar: "))
print("Correcte!")
