mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:10] + mensaje[10:]
print("Ejercicio 1:", secreto)

numeros = [10, 20, 30, 40, 50]
primero = numeros[0]
numeros[0] = numeros[-1]
numeros[-1] = primero
print("Ejercicio 2:", numeros)

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print("Ejercicio 3:", sandwich)

lista = [1, 2, 3]
duplicada = lista + lista
print("Ejercicio 4:", duplicada)

lista_centro = [10, 20, 30, 40, 50]
indice_centro = len(lista_centro) // 2
centro = lista_centro[indice_centro:indice_centro + 1]
print("Ejercicio 5: El centro es", centro[0])

lista_reversa = [1, 2, 3, 4, 5, 6]
mitad = len(lista_reversa) // 2
reversa_parcial = lista_reversa[:mitad][::-1] + lista_reversa[mitad:]
print("Ejercicio 6:", reversa_parcial)
