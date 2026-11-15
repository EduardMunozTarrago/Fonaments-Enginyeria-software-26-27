def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}!")

def es_parell(numero):
    return numero % 2 == 0

def mitjana(numeros):
    if not numeros:
        return None
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)

def sumar_tot(*args):
    total = 0
    for numero in args:
        total += numero
    return total

def taula_multiplicar(numero, limit=10):
    for factor in range(1, limit + 1):
        print(f"{numero} x {factor} = {numero * factor}")

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

def factorial(numero):
    if numero < 0:
        raise ValueError("El nombre ha de ser no negatiu")
    resultat = 1
    comptador = 1
    while comptador <= numero:
        resultat *= comptador
        comptador += 1
    return resultat

def maxim(numeros):
    if not numeros:
        return None
    resultat = numeros[0]
    for numero in numeros[1:]:
        if numero > resultat:
            resultat = numero
    return resultat

def comptar_vocals(text):
    resultat = 0
    for lletra in text.lower():
        if lletra in "aeiouàèéíòóúïü":
            resultat += 1
    return resultat

def minim_i_maxim(numeros):
    if not numeros:
        return None, None
    minim = numeros[0]
    maxim_actual = numeros[0]
    for numero in numeros[1:]:
        if numero < minim:
            minim = numero
        if numero > maxim_actual:
            maxim_actual = numero
    return minim, maxim_actual

def es_palindrom(text):
    text = text.lower()
    return text == text[::-1]

if __name__ == "__main__":
    saludar_a("Anna")
    saludar_a("Anna", "Bon dia")
    print("Parell:", es_parell(4), es_parell(7))
    print("Mitjana:", mitjana([10, 20, 30, 40, 50]))
    print("Sumes:", sumar_tot(1, 2), sumar_tot(1, 2, 3, 4, 5), sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    taula_multiplicar(3)
    mostrar_perfil(nom="Anna", edat=19, grau="Enginyeria")
    print("Factorial:", factorial(5), "Màxim:", maxim([15, 5, 25, 10, 20]))
    print("Vocals:", comptar_vocals("Hola Món"))
    minim, maxim_valor = minim_i_maxim([15, 3, 42, 8, 23, 4])
    print("Mínim i màxim:", minim, maxim_valor)
    print("Palíndrom:", es_palindrom("Anna"), es_palindrom("Python"))
