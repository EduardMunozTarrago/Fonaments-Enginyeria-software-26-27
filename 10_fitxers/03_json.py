import json
import math
from pathlib import Path
from tempfile import TemporaryDirectory

def desar_json(ruta, lectures):
    text = json.dumps(lectures, ensure_ascii=False, indent=2, allow_nan=False)
    with open(ruta, 'w', encoding='utf-8') as fitxer:
        fitxer.write(text)

def llegir_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as fitxer:
        lectures = json.load(fitxer)
    if not isinstance(lectures, list):
        raise ValueError('Cal una llista de lectures')
    for lectura in lectures:
        if not isinstance(lectura, dict):
            raise ValueError('Cada lectura ha de ser un diccionari')
        if len(lectura) != 3:
            raise ValueError('Cada lectura ha de tenir sensor, valor i unitat')
        for camp in ('sensor', 'valor', 'unitat'):
            if camp not in lectura:
                raise ValueError('Falta un camp de la lectura')
        if not isinstance(lectura['sensor'], str):
            raise ValueError('El nom del sensor ha de ser text')
        if not isinstance(lectura['unitat'], str):
            raise ValueError('La unitat ha de ser text')
        valor = lectura['valor']
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError('La mesura ha de ser numèrica')
        try:
            valor = float(valor)
        except OverflowError:
            raise ValueError('La mesura supera el rang numèric admès')
        if not math.isfinite(valor):
            raise ValueError('La mesura ha de ser finita')
        lectura['valor'] = valor
    return lectures

def main():
    lectures = [{'sensor': 'T1', 'valor': 21.5, 'unitat': '°C'}]
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / 'lectures.json'
        desar_json(ruta, lectures)
        print(llegir_json(ruta))
        desar_json(ruta, [])
        print(llegir_json(ruta))
        configuracio = Path(carpeta) / 'configuracio.json'
        with open(configuracio, 'w', encoding='utf-8') as fitxer:
            json.dump({'actiu': True, 'llindar': 25.0}, fitxer, indent=2)
        with open(configuracio, encoding='utf-8') as fitxer:
            print(json.load(fitxer))
        with open(ruta, 'w', encoding='utf-8') as fitxer:
            fitxer.write('{"sensor":')
        try:
            llegir_json(ruta)
        except json.JSONDecodeError:
            print('El fitxer conté JSON incomplet')
if __name__ == '__main__':
    main()
