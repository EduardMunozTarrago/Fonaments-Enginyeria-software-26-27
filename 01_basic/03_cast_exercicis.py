paquets = int(input("Quants paquets ha rebut l'encaminador? "))
total = paquets + 1200
print(f"Total de paquets: {total}")

velocitat_mbps = float(input("Velocitat de la connexió en Mbps: "))
velocitat_mbs = velocitat_mbps / 8
print(f"Velocitat equivalent: {velocitat_mbs:g} MB/s")
