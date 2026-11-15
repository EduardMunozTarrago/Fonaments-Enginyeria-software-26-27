print('\nExercici 1:')
nombre_a = 8
nombre_b = 5
print(f'{nombre_a} > {nombre_b}: {nombre_a > nombre_b}')
print(f'{nombre_a} < {nombre_b}: {nombre_a < nombre_b}')
print(f'{nombre_a} == {nombre_b}: {nombre_a == nombre_b}')
print('\nExercici 2:')
paraula_a = 'Hola'
paraula_b = 'hola'
print(f'Les paraules són iguals: {paraula_a == paraula_b}')
print(f"paraula_a és igual a 'Hola': {paraula_a == 'Hola'}")
print('\nExercici 3:')
router_encès = True
connexio_activa = False
xarxa_disponible = router_encès and connexio_activa
print(f'Xarxa disponible: {xarxa_disponible}')
print('\nExercici 4:')
actualitzacio_disponible = False
alerta_critica = True
cal_avisar = actualitzacio_disponible or alerta_critica
print(f'Cal avisar: {cal_avisar}')
print('\nExercici 5:')
compte_actiu = True
contrasenya_correcta = True
codi_correcte = False
dispositiu_de_confiança = True
compte_bloquejat = False
accés_permes = compte_actiu and contrasenya_correcta and (codi_correcte or dispositiu_de_confiança) and (not compte_bloquejat)
print(f'Accés permès: {accés_permes}')
