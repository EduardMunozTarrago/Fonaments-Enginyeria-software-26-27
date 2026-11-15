from pathlib import Path
from tempfile import TemporaryDirectory

def desar_missatge(ruta, missatge):
    with open(ruta, 'w', encoding='utf-8') as fitxer:
        fitxer.write(missatge)

def llegir_missatge(ruta):
    with open(ruta, 'r', encoding='utf-8') as fitxer:
        return fitxer.read()

def comptar_lectures(ruta):
    comptador = 0
    with open(ruta, 'r', encoding='utf-8') as fitxer:
        for linia in fitxer:
            if linia.strip():
                comptador += 1
    return comptador

def llegir_valides(ruta):
    lectures = []
    with open(ruta, 'r', encoding='utf-8') as fitxer:
        for linia in fitxer:
            text = linia.strip()
            if text:
                try:
                    lectures.append(float(text))
                except ValueError:
                    continue
    return lectures

def afegir_esdeveniment(ruta, missatge):
    with open(ruta, 'a', encoding='utf-8') as fitxer:
        fitxer.write(missatge + '\n')

def main():
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / 'prova.txt'
        desar_missatge(ruta, 'Sensor de tensió actiu\n')
        print(repr(llegir_missatge(ruta)))
        desar_missatge(ruta, '')
        print(repr(llegir_missatge(ruta)))
        desar_missatge(ruta, '20.0\n\n21.5\n   \n')
        print(comptar_lectures(ruta))
        desar_missatge(ruta, '')
        print(comptar_lectures(ruta))
        try:
            comptar_lectures(Path(carpeta) / 'absent.txt')
        except FileNotFoundError:
            print("S'ha propagat FileNotFoundError")
        desar_missatge(ruta, '20.0\nerror\n\n22.0\n')
        print(llegir_valides(ruta))
        desar_missatge(ruta, 'error\n\n')
        print(llegir_valides(ruta))
        registre = Path(carpeta) / 'esdeveniments.txt'
        afegir_esdeveniment(registre, 'Inici')
        afegir_esdeveniment(registre, 'Aturada')
        print(repr(llegir_missatge(registre)))
        afegir_esdeveniment(registre, 'Inici')
        print(repr(llegir_missatge(registre)))
if __name__ == '__main__':
    main()
