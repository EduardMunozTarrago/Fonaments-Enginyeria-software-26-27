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

class SistemaMonitoratge:

    def __init__(self):
        self.sensors = {}

    def afegir_sensor(self, sensor):
        if sensor.nom in self.sensors:
            raise ValueError('Ja existeix un sensor amb aquest nom.')
        self.sensors[sensor.nom] = sensor

    def registrar(self, nom, valor):
        if nom not in self.sensors:
            raise ValueError('El sensor no existeix.')
        self.sensors[nom].registrar(valor)

    def resum(self):
        files = []
        for sensor in self.sensors.values():
            files.append({'sensor': sensor.nom, 'unitat': sensor.unitat, 'valor': sensor.ultima_lectura()})
        return files

def main():
    sistema = SistemaMonitoratge()
    print(sistema.resum())
    sistema.afegir_sensor(Sensor('T1', '°C'))
    sistema.afegir_sensor(Sensor('H1', '%'))
    sistema.registrar('T1', 22.5)
    sistema.registrar('T1', 23.0)
    print(sistema.resum())
    try:
        sistema.afegir_sensor(Sensor('T1', '°C'))
    except ValueError as error:
        print(error)
    try:
        sistema.registrar('V1', 3.3)
    except ValueError as error:
        print(error)
if __name__ == '__main__':
    main()
