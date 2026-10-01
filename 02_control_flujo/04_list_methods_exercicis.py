numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.insert(2, 10)
numeros[0] = 0
print("Ejercicio 1:", numeros)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
lista_a.remove(1)
eliminado = lista_a.pop(3)
lista_b.clear()
print("Ejercicio 2: elemento eliminado:", eliminado)
print("lista_a:", lista_a)
print("lista_b:", lista_b)

lista_del = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista_del[2:5]
print("Ejercicio 3:", lista_del)

lista_ordenada = [5, 2, 8, 1, 9, 4, 2]
lista_ordenada.sort()
veces_dos = lista_ordenada.count(2)
contiene_siete = 7 in lista_ordenada
print("Ejercicio 4:", lista_ordenada)
print("Veces que aparece el 2:", veces_dos)
print("¿Está el 7?:", contiene_siete)

original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print("Ejercicio 5:")
print("original:", original)
print("copia_1:", copia_1)
print("copia_2:", copia_2)
print("referencia:", referencia)

frutas = ["Manzana", "pera", "BANANA", "naranja"]
frutas.sort(key=str.lower)
print("Ejercicio 6:", frutas)
