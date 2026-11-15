num_usuaris = int(input("Introdueix el nombre d'usuaris afectats: "))
if num_usuaris < 0:
    print('Dades incorrectes')
elif num_usuaris >= 50:
    print('Prioritat crítica')
elif num_usuaris >= 10:
    print('Prioritat alta')
else:
    print('Prioritat baixa')
