import json
from pathlib import Path
from tempfile import TemporaryDirectory

def desar_configuracio(ruta, configuracio):
    with open(ruta, 'w', encoding='utf-8') as fitxer:
        json.dump(configuracio, fitxer, ensure_ascii=False, indent=2)

def llegir_configuracio(ruta):
    with open(ruta, 'r', encoding='utf-8') as fitxer:
        return json.load(fitxer)

def mitjana_historic(ruta):
    lectures = llegir_configuracio(ruta)
    if not lectures:
        return None
    suma = 0
    for lectura in lectures:
        suma += lectura['valor']
    return suma / len(lectures)

def carregar_o_informar(ruta):
    try:
        return llegir_configuracio(ruta)
    except FileNotFoundError:
        print('Fitxer absent')
    except json.JSONDecodeError:
        print('JSON invàlid')
    return None

def afegir_lectura(ruta, lectura):
    try:
        lectures = llegir_configuracio(ruta)
    except FileNotFoundError:
        lectures = []
    lectures.append(lectura)
    desar_configuracio(ruta, lectures)

def main():
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / 'dades.json'
        configuracio = {'dispositiu': 'Estació UAB', 'actiu': True, 'periode_s': 5}
        desar_configuracio(ruta, configuracio)
        print(llegir_configuracio(ruta))
        desar_configuracio(ruta, {})
        print(llegir_configuracio(ruta))
        historic = [{'sensor': 'T1', 'valor': 20.0, 'unitat': '°C'}, {'sensor': 'T1', 'valor': 22.0, 'unitat': '°C'}]
        desar_configuracio(ruta, historic)
        print(mitjana_historic(ruta))
        desar_configuracio(ruta, [])
        print(mitjana_historic(ruta))
        print(carregar_o_informar(Path(carpeta) / 'absent.json'))
        with open(ruta, 'w', encoding='utf-8') as fitxer:
            fitxer.write('{"actiu":')
        print(carregar_o_informar(ruta))
        desar_configuracio(ruta, {'actiu': True})
        print(carregar_o_informar(ruta))
        desar_configuracio(ruta, None)
        print(carregar_o_informar(ruta))
        ruta_historic = Path(carpeta) / 'historic.json'
        primera = {'sensor': 'H1', 'valor': 45.0, 'unitat': '%'}
        segona = {'sensor': 'H1', 'valor': 46.0, 'unitat': '%'}
        afegir_lectura(ruta_historic, primera)
        afegir_lectura(ruta_historic, segona)
        print(llegir_configuracio(ruta_historic))
        afegir_lectura(ruta_historic, primera)
        print(len(llegir_configuracio(ruta_historic)))
        with open(ruta_historic, 'w', encoding='utf-8') as fitxer:
            fitxer.write('[')
        try:
            afegir_lectura(ruta_historic, primera)
        except json.JSONDecodeError:
            print("S'ha propagat JSONDecodeError")
if __name__ == '__main__':
    main()
