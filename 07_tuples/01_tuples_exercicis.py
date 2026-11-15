ciutats = ("Barcelona", "Madrid", "València", "Sevilla", "Bilbao")
print("Segona ciutat:", ciutats[1])
print("Penúltima ciutat:", ciutats[-2])

numeros = (1, 3, 5, 3, 7, 3, 9)
print("Nombre de vegades que apareix el 3:", numeros.count(3))

def ordenar_tupla(valors):
    return tuple(sorted(valors))

print("Tupla ordenada:", ordenar_tupla((9, 3, 7, 1, 5)))
