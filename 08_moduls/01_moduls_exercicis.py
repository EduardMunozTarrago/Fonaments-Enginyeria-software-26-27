import math as matematiques
import conversions as conv
from sensors import mitjana

def informe_sensor(nom, lectures):
    return {'nom': nom, 'nombre': len(lectures), 'mitjana': mitjana(lectures)}

def main():
    print('Exercici 1')
    x = 3.0
    y = 4.0
    print(matematiques.sqrt(x * x + y * y))
    print(matematiques.sqrt(0.0 * 0.0 + 0.0 * 0.0))
    print('Exercici 2')
    temperatures = [-10.0, 0.0, 25.0]
    tensions_mv = [0, 3300, 5000]
    temperatures_k = []
    for temperatura in temperatures:
        temperatures_k.append(conv.celsius_a_kelvin(temperatura))
    tensions_v = []
    for tensio in tensions_mv:
        tensions_v.append(conv.milivolts_a_volts(tensio))
    print(temperatures_k)
    print(tensions_v)
    print('Exercici 3')
    dades = {'T1': [20.0, 22.0], 'T2': [18.0], 'T3': []}
    mitjanes = {}
    for identificador, lectures in dades.items():
        mitjanes[identificador] = mitjana(lectures)
    print(mitjanes)
    print('Exercici 4')
    print(informe_sensor('T1', [20.0, 22.0]))
    print(informe_sensor('T0', []))
if __name__ == '__main__':
    main()
