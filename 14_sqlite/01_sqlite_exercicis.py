import sqlite3
from contextlib import closing
from pathlib import Path
from tempfile import TemporaryDirectory

def crear_historic(ruta):
    with closing(sqlite3.connect(ruta)) as connexio:
        connexio.execute('\n            CREATE TABLE IF NOT EXISTS lectures (\n                id INTEGER PRIMARY KEY,\n                sensor TEXT NOT NULL,\n                valor REAL NOT NULL,\n                unitat TEXT NOT NULL\n            )\n        ')
        connexio.commit()

def afegir_lectura(ruta, sensor, valor, unitat):
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute('INSERT INTO lectures (sensor, valor, unitat) VALUES (?, ?, ?)', (sensor, valor, unitat))
        connexio.commit()
        return cursor.lastrowid

def lectures_sensor(ruta, nom):
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute('SELECT valor, unitat FROM lectures WHERE sensor = ? ORDER BY id', (nom,))
        return cursor.fetchall()

def actualitzar_valor(ruta, identificador, valor):
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute('UPDATE lectures SET valor = ? WHERE id = ?', (valor, identificador))
        connexio.commit()
        return cursor.rowcount

def eliminar_lectura(ruta, identificador):
    with closing(sqlite3.connect(ruta)) as connexio:
        cursor = connexio.execute('DELETE FROM lectures WHERE id = ?', (identificador,))
        connexio.commit()
        return cursor.rowcount

def afegir_lot(ruta, lectures):
    with closing(sqlite3.connect(ruta)) as connexio:
        try:
            for sensor, valor, unitat in lectures:
                connexio.execute('INSERT INTO lectures (sensor, valor, unitat) VALUES (?, ?, ?)', (sensor, valor, unitat))
            connexio.commit()
        except sqlite3.Error:
            connexio.rollback()
            raise

def main():
    with TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / 'historic.sqlite'
        crear_historic(ruta)
        print(lectures_sensor(ruta, "Sensor d'entrada"))
        print(afegir_lectura(ruta, "Sensor d'entrada", 3.3, 'V'))
        print(afegir_lectura(ruta, 'T1', 21.5, '°C'))
        crear_historic(ruta)
        afegir_lectura(ruta, "Sensor d'entrada", 3.4, 'V')
        print(lectures_sensor(ruta, "Sensor d'entrada"))
        print(lectures_sensor(ruta, 'desconegut'))
        ruta_correccio = Path(carpeta) / 'correccio.sqlite'
        crear_historic(ruta_correccio)
        afegir_lectura(ruta_correccio, "Sensor d'entrada", 3.3, 'V')
        afegir_lectura(ruta_correccio, 'T1', 21.5, '°C')
        print(actualitzar_valor(ruta_correccio, 1, 3.5))
        print(eliminar_lectura(ruta_correccio, 2))
        print(actualitzar_valor(ruta_correccio, 999, 4.0))
        print(eliminar_lectura(ruta_correccio, 999))
        with closing(sqlite3.connect(ruta_correccio)) as connexio:
            print(connexio.execute('SELECT id, sensor, valor, unitat FROM lectures ORDER BY id').fetchall())
        ruta_lots = Path(carpeta) / 'lots.sqlite'
        crear_historic(ruta_lots)
        afegir_lot(ruta_lots, [("Sensor d'entrada", 3.3, 'V'), ('T1', 21.5, '°C')])
        afegir_lot(ruta_lots, [('H1', 45.0, '%'), ('H1', 46.0, '%')])
        afegir_lot(ruta_lots, [])
        try:
            afegir_lot(ruta_lots, [('H2', 50.0, '%'), (None, 51.0, '%')])
        except sqlite3.IntegrityError:
            print('Lot rebutjat')
        with closing(sqlite3.connect(ruta_lots)) as connexio:
            files = connexio.execute('SELECT id FROM lectures').fetchall()
            print(len(files))
        ruta_buida = Path(carpeta) / 'buida.sqlite'
        crear_historic(ruta_buida)
        try:
            afegir_lot(ruta_buida, [('H2', 50.0, '%'), (None, 51.0, '%')])
        except sqlite3.IntegrityError:
            print('Lot buit després del rebuig:')
            print(lectures_sensor(ruta_buida, 'H2'))
if __name__ == '__main__':
    main()
