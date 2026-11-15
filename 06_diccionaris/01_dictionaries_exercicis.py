estudiant = {
    "nom": "Alex",
    "edat": 20,
    "assignatures": ["Programació", "Xarxes", "Matemàtiques"],
}
print("Exercici 1:", estudiant)

print("Exercici 2:", estudiant["assignatures"][1])
estudiant["edat"] = 21
print("Nova edat:", estudiant["edat"])

estudiant["grau"] = "Enginyeria"
del estudiant["edat"]
print("Exercici 3:", estudiant)

print("Exercici 4: nom:", "nom" in estudiant)
print("Exercici 4: email:", "email" in estudiant)

print("Exercici 5")
for clau, valor in estudiant.items():
    print(f"{clau}: {valor}")

paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
comptador = {}
for paraula in paraules:
    if paraula in comptador:
        comptador[paraula] += 1
    else:
        comptador[paraula] = 1
print("Exercici 6:", comptador)
