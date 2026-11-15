from math import isfinite

class Sensor:

    def __init__(self, nom, unitat):
        self.nom = nom
        self.unitat = unitat
        self.lectures = []

    def registrar(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError('La lectura ha de ser un nombre.')
        if isinstance(valor, float) and (not isfinite(valor)):
            raise ValueError('La lectura ha de ser finita.')
        self.lectures.append(valor)

    def ultima_lectura(self):
        if not self.lectures:
            return None
        return self.lectures[-1]

    def mitjana(self):
        if not self.lectures:
            return None
        return sum(self.lectures) / len(self.lectures)

    def comptar_superiors(self, llindar):
        recompte = 0
        for lectura in self.lectures:
            if lectura > llindar:
                recompte += 1
        return recompte

def main():
    print('Exercici 1')
    temperatura = Sensor('T1', '°C')
    humitat = Sensor('H1', '%')
    print(temperatura.nom, temperatura.unitat, temperatura.lectures)
    print(humitat.nom, humitat.unitat, humitat.lectures)
    print('Exercici 2')
    temperatura.registrar(20.0)
    temperatura.registrar(24.0)
    humitat.registrar(55.0)
    print(temperatura.lectures)
    print(humitat.lectures)
    for valor_invalid in ['error', True, float('inf')]:
        try:
            temperatura.registrar(valor_invalid)
        except ValueError:
            print('Lectura rebutjada')
    print(temperatura.lectures)
    try:
        temperatura.registrar(float('nan'))
    except ValueError:
        print('Lectura rebutjada')
    print('Exercici 3')
    print(temperatura.ultima_lectura())
    print(temperatura.mitjana())
    tensio = Sensor('V1', 'V')
    print(tensio.ultima_lectura())
    print(tensio.mitjana())
    tensio.registrar(0)
    print(tensio.ultima_lectura())
    print(tensio.mitjana())
    print('Exercici 4')
    sensor = Sensor('T2', '°C')
    for lectura in [20.0, 24.0, 24.0, 30.0]:
        sensor.registrar(lectura)
    print(sensor.comptar_superiors(24.0))
    print(sensor.comptar_superiors(19.0))
    print(Sensor('T3', '°C').comptar_superiors(24.0))
    print(sensor.lectures)
if __name__ == '__main__':
    main()
