from math import isfinite

class Sensor:

    def __init__(self, nom, unitat):
        self.nom = nom
        self.unitat = unitat
        self._lectures = []

    def _validar(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError('La lectura ha de ser un nombre.')
        if isinstance(valor, float) and (not isfinite(valor)):
            raise ValueError('La lectura ha de ser finita.')

    def registrar(self, valor):
        self._validar(valor)
        self._lectures.append(valor)

    def ultima_lectura(self):
        if not self._lectures:
            return None
        return self._lectures[-1]

    def mitjana(self):
        if not self._lectures:
            return None
        return sum(self._lectures) / len(self._lectures)

    def obtenir_lectures(self):
        return self._lectures.copy()

class SensorTemperatura(Sensor):

    def __init__(self, nom):
        super().__init__(nom, '°C')

    def _validar(self, valor):
        super()._validar(valor)
        if not -40 <= valor <= 85:
            raise ValueError("La temperatura ha d'estar entre -40 i 85 °C.")

class SensorHumitat(Sensor):

    def __init__(self, nom):
        super().__init__(nom, '%')

    def _validar(self, valor):
        super()._validar(valor)
        if not 0 <= valor <= 100:
            raise ValueError("La humitat ha d'estar entre 0 i 100 %.")

class SensorTensio(Sensor):

    def __init__(self, nom):
        super().__init__(nom, 'V')

    def _validar(self, valor):
        super()._validar(valor)
        if not 0 <= valor <= 5:
            raise ValueError("La tensió ha d'estar entre 0 i 5 V.")

def mostrar_resums(sensors):
    for sensor in sensors:
        print(sensor.nom, sensor.ultima_lectura(), sensor.mitjana(), sensor.unitat)

def main():
    print('Exercici 1')
    temperatura = SensorTemperatura('T1')
    humitat = SensorHumitat('H1')
    print(temperatura.nom, temperatura.unitat, temperatura.obtenir_lectures())
    print(humitat.nom, humitat.unitat, humitat.obtenir_lectures())
    print('Exercici 2')
    for valor in [-40, 85]:
        temperatura.registrar(valor)
    for valor in [0, 100]:
        humitat.registrar(valor)
    print(temperatura.obtenir_lectures())
    print(humitat.obtenir_lectures())
    for sensor, valor in [(temperatura, -41), (temperatura, 86), (humitat, -1), (humitat, 101)]:
        try:
            sensor.registrar(valor)
        except ValueError:
            print('Lectura rebutjada')
    print(temperatura.obtenir_lectures())
    print(humitat.obtenir_lectures())
    buit = SensorTemperatura('T0')
    for valor in [True, '25', float('nan'), float('inf')]:
        try:
            buit.registrar(valor)
        except ValueError:
            print('Lectura rebutjada')
    print(buit.obtenir_lectures())
    print('Exercici 3')
    temperatura = SensorTemperatura('T1')
    humitat = SensorHumitat('H1')
    for valor in [20.0, 24.0]:
        temperatura.registrar(valor)
    for valor in [40.0, 60.0]:
        humitat.registrar(valor)
    sensors = [temperatura, humitat]
    mostrar_resums(sensors)
    copia = temperatura.obtenir_lectures()
    copia.append(999.0)
    print(temperatura.obtenir_lectures())
    print(buit.ultima_lectura())
    print(buit.mitjana())
    print('Exercici 4')
    tensio = SensorTensio('V1')
    tensio.registrar(0.0)
    tensio.registrar(5.0)
    try:
        tensio.registrar(6.0)
    except ValueError:
        print('Lectura rebutjada')
    sensors.append(tensio)
    mostrar_resums(sensors)
    print(tensio.obtenir_lectures())
if __name__ == '__main__':
    main()
