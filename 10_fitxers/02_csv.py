import csv
import math
from pathlib import Path
from tempfile import TemporaryDirectory
CAMPS = ['sensor', 'valor', 'unitat']

def desar_csv(ruta, lectures):
    with open(ruta, 'w', encoding='utf-8', newline='') as fitxer:
        escriptor = csv.DictWriter(fitxer, fieldnames=CAMPS)
        escriptor.writeheader()
        escriptor.writerows(lectures)

def llegir_csv(ruta):
    lectures = []
    with open(ruta, 'r', encoding='utf-8', newline='') as fitxer:
        lector = csv.DictReader(fitxer)
        if lector.fieldnames != CAMPS:
            raise ValueError('La capçalera ha de ser sensor,valor,unitat')
        for fila in lector:
            if None in fila:
                raise ValueError('La fila ha de tenir tres camps')
            for camp in CAMPS:
                if fila[camp] is None:
                    raise ValueError('La fila ha de tenir tres camps')
            valor = float(fila['valor'])
            if not math.isfinite(valor):
                raise ValueError('La mesura ha de ser finita')
            lectures.append({'sensor': fila['sensor'], 'valor': valor, 'unitat': fila['unitat']})
    return lectures

def main():
    lectures = [{'sensor': 'T1', 'valor': 21.5, 'unitat': '°C'}, {'sensor': 'Laboratori, nord', 'valor': 48.0, 'unitat': '%'}]
    with TemporaryDirectory() as carpeta:
        ruta_tensions = Path(carpeta) / 'tensions.csv'
        with open(ruta_tensions, 'w', encoding='utf-8', newline='') as fitxer:
            escriptor = csv.writer(fitxer)
            escriptor.writerow(['sensor', 'volts'])
            escriptor.writerow(['V1', 3.3])
        with open(ruta_tensions, encoding='utf-8', newline='') as fitxer:
            print(list(csv.reader(fitxer)))
        ruta = Path(carpeta) / 'lectures.csv'
        desar_csv(ruta, lectures)
        recuperades = llegir_csv(ruta)
        print(recuperades)
        print(type(recuperades[0]['valor']).__name__)
        desar_csv(ruta, [])
        print(llegir_csv(ruta))
if __name__ == '__main__':
    main()
