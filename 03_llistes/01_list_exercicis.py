print('\nExercici 1:')
missatge = ['C', 'o', 'd', 'i', ' ', 's', 'e', 'c', 'r', 'e', 't']
secret = missatge[5:]
print(secret)
print('\nExercici 2:')
nombres = [10, 20, 30, 40, 50]
nombres[0], nombres[-1] = (nombres[-1], nombres[0])
print(nombres)
print('\nExercici 3:')
pa_de_dalt = ['pa de dalt']
ingredients = ['pernil', 'formatge', 'tomàquet']
pa_de_sota = ['pa de sota']
entrepa = pa_de_dalt + ingredients + pa_de_sota
print(entrepa)
print('\nExercici 4:')
llista = [1, 2, 3]
llista_duplicada = llista + llista
print(llista_duplicada)
print('\nExercici 5:')
llista = [10, 20, 30, 40, 50]
centre = len(llista) // 2
print(llista[centre])
print('\nExercici 6:')
llista = [1, 2, 3, 4, 5, 6]
meitat = len(llista) // 2
llista_invertida = llista[:meitat][::-1] + llista[meitat:]
print(llista_invertida)
