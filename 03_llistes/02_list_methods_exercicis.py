print('\nExercici 1:')
llista = [1, 2, 3, 4, 5]
llista.append(6)
llista.insert(2, 10)
llista[0] = 0
print(llista)
print('\nExercici 2:')
llista_a = [1, 2, 3]
llista_b = [4, 5, 6, 1, 2]
llista_a.extend(llista_b)
llista_a.remove(1)
element_eliminat = llista_a.pop(3)
print(f'Element eliminat: {element_eliminat}')
llista_b.clear()
print('Llista a:', llista_a)
print('Llista b:', llista_b)
print('\nExercici 3:')
llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del llista[2:5]
print(llista)
print('\nExercici 4:')
llista = [5, 2, 8, 1, 9, 4, 2]
llista.sort()
quantitat_dos = llista.count(2)
hi_ha_el_set = 7 in llista
print(f'Llista ordenada: {llista}')
print(f'Quantitat de 2: {quantitat_dos}')
print(f'Hi ha el 7?: {hi_ha_el_set}')
print('\nExercici 5:')
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original
referencia[0] = 10
print(f'Original: {original}')
print(f'Còpia 1 (slicing): {copia_1}')
print(f'Còpia 2 (copy()): {copia_2}')
print(f'Referència: {referencia}')
print('\nExercici 6:')
cadenes = ['Poma', 'pera', 'PLÀTAN', 'taronja']
cadenes.sort(key=str.lower)
print(cadenes)
