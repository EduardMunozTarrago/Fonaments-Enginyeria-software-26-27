print(bool('False'))
x = 10
if x > 5:
    print('A')
elif x > 8:
    print('B')
else:
    print('C')
print(not (True and False) or False)
print(not (True and False) or False)
llista = [1, 2, 3, 4, 5, 6, 7, 8]
print(llista[1:6:2])
comptador = 0
while comptador < 10:
    comptador += 1
    if comptador % 2 == 0:
        continue
    print(comptador)
numeros = [10, 20, 30, 40]
numeros.pop(1)
numeros.insert(2, 50)
print(numeros[-2])
temperatura = 28
humitat = 75
if temperatura > 30 or humitat > 80:
    print('Alerta')
elif temperatura >= 25 and humitat >= 70:
    print('Precaució')
else:
    print('Normal')
valors = [2, 4, 6, 8, 10]
i = 0
while i < len(valors):
    if valors[i] > 5:
        valors.pop(i)
    else:
        i += 1
print(valors)
