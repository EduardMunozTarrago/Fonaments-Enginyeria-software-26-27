print("Exercici 1: instal·lació de xarxa")
tecnic = input("Nom del tècnic: ")
xarxa = input("Nom de la xarxa: ")
print(f"El tècnic {tecnic} està instal·lant la xarxa {xarxa}.")

print("\nExercici 2: transmissió per fibra")
longitud_km = float(input("Longitud de l'enllaç (km): "))
velocitat_gbps = float(input("Velocitat de transmissió (Gbps): "))
if longitud_km < 0 or velocitat_gbps <= 0:
    print("Dades no vàlides: longitud >= 0 i velocitat > 0.")
else:

    temps_segons = 8 / velocitat_gbps
    print(f"Enllaç de {longitud_km:g} km a {velocitat_gbps:g} Gbps.")
    print(f"Temps per transmetre 1 GB: {temps_segons:g} segons.")

print("\nExercici 3: pressupost d'instal·lació")
hores = float(input("Hores de feina: "))
preu_hora = float(input("Preu per hora (EUR): "))
preu_material = float(input("Preu del material (EUR): "))
if hores < 0 or preu_hora < 0 or preu_material < 0:
    print("Dades no vàlides: les hores i els preus no poden ser negatius.")
else:
    cost_total = hores * preu_hora + preu_material
    print(f"Cost total de la instal·lació: {cost_total:.2f} EUR")
