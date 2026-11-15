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

    def alarmes(self, unitat, llindar):
        noms = []
        for sensor in self.sensors.values():
            lectura = sensor.ultima_lectura()
            if sensor.unitat == unitat and lectura is not None:
                if lectura > llindar:
                    noms.append(sensor.nom)
        return noms

def main():
    print('Exercici 1')
    sistema = SistemaMonitoratge()
    print(len(sistema.sensors))
    sistema.afegir_sensor(Sensor('T1', '°C'))
    sistema.afegir_sensor(Sensor('H1', '%'))
    print(list(sistema.sensors))
    try:
        sistema.afegir_sensor(Sensor('T1', '°C'))
    except ValueError:
        print('Nom duplicat')
    print('Exercici 2')
    sistema.registrar('T1', 20.0)
    sistema.registrar('T1', 24.0)
    sistema.registrar('H1', 50.0)
    print(sistema.sensors['T1'].ultima_lectura())
    print(sistema.sensors['H1'].ultima_lectura())
    for nom, valor in [('V1', 3.3), ('T1', 'error')]:
        try:
            sistema.registrar(nom, valor)
        except ValueError:
            print('Registre rebutjat')
    print(sistema.sensors['T1'].ultima_lectura())
    print('Exercici 3')
    resum_sistema = SistemaMonitoratge()
    print(resum_sistema.resum())
    resum_sistema.afegir_sensor(Sensor('T1', '°C'))
    resum_sistema.afegir_sensor(Sensor('H1', '%'))
    resum_sistema.registrar('T1', 22.5)
    print(resum_sistema.resum())
    print('Exercici 4')
    alarmes_sistema = SistemaMonitoratge()
    for nom, unitat in [('T1', '°C'), ('T2', '°C'), ('H1', '%'), ('T3', '°C')]:
        alarmes_sistema.afegir_sensor(Sensor(nom, unitat))
    alarmes_sistema.registrar('T1', 28.0)
    alarmes_sistema.registrar('T2', 25.0)
    alarmes_sistema.registrar('H1', 70.0)
    print(alarmes_sistema.alarmes('°C', 25.0))
    print(alarmes_sistema.alarmes('V', 3.0))
    print(SistemaMonitoratge().alarmes('°C', 25.0))
if __name__ == '__main__':
    main()
