import csv
from pathlib import Path
from tempfile import TemporaryDirectory
CAMPS = ['sensor', 'valor', 'unitat']

def desar_tensions(ruta, tensions):
    with open(ruta, 'w', encoding='utf-8', newline='') as fitxer:
        escriptor = csv.writer(fitxer)
        escriptor.writerow(['sensor', 'volts'])
        escriptor.writerows(tensions)

def sensors_en_alerta(ruta, llindar):
    noms = []
    with open(ruta, 'r', encoding='utf-8', newline='') as fitxer:
        for fila in csv.DictReader(fitxer):
            if float(fila['valor']) >= llindar:
                noms.append(fila['sensor'])
    return noms

def desar_lectures(ruta, lectures):
    with open(ruta, 'w', encoding='utf-8', newline='') as fitxer:
        escriptor = csv.DictWriter(fitxer, fieldnames=CAMPS)
        escriptor.writeheader()
        escriptor.writerows(lectures)

def recuperar_lectures(ruta):
    with open(ruta, 'r', encoding='utf-8', newline='') as fitxer:
        lectures = list(csv.DictReader(fitxer))
    for lectura in lectures:
        lectura['valor'] = float(lectura['valor'])
    return lectures

def llegir_amb_capcalera_validada(ruta):
    with open(ruta, 'r', encoding='utf-8', newline='') as fitxer:
        lector = csv.DictReader(fitxer)
        if lector.fieldnames != CAMPS:
            raise ValueError('Capçalera incorrecta')
        lectures = list(lector)
    for lectura in lectures:
        lectura['valor'] = float(lectura['valor'])
    return lectures

def main():
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / 'lectures.csv'
        desar_tensions(ruta, [('V1', 3.3), ('V2', 5.0)])
        with open(ruta, encoding='utf-8', newline='') as fitxer:
            print(list(csv.reader(fitxer)))
        desar_tensions(ruta, [])
        with open(ruta, encoding='utf-8', newline='') as fitxer:
            print(list(csv.reader(fitxer)))
        lectures = [{'sensor': 'T1', 'valor': 20.0, 'unitat': '°C'}, {'sensor': 'T2', 'valor': 25.0, 'unitat': '°C'}, {'sensor': 'T3', 'valor': 26.0, 'unitat': '°C'}]
        desar_lectures(ruta, lectures)
        print(sensors_en_alerta(ruta, 25.0))
        desar_lectures(ruta, [])
        print(sensors_en_alerta(ruta, 25.0))
        print(recuperar_lectures(ruta))
        amb_coma = [{'sensor': 'Sala, nord', 'valor': 19.5, 'unitat': '°C'}]
        desar_lectures(ruta, amb_coma)
        print(recuperar_lectures(ruta))
        print(llegir_amb_capcalera_validada(ruta))
        desar_lectures(ruta, [])
        print(llegir_amb_capcalera_validada(ruta))
        for contingut in ['nom,valor\nT1,20\n', '']:
            with open(ruta, 'w', encoding='utf-8') as fitxer:
                fitxer.write(contingut)
            try:
                llegir_amb_capcalera_validada(ruta)
            except ValueError as error:
                print(error)
if __name__ == '__main__':
    main()
