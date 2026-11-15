total_consum = 0
connexions = 0
while total_consum < 100 and connexions < 10:
    consum = float(input('Introdueix el consum en GB: '))
    total_consum += consum
    connexions += 1
print('Consum total acumulat:', total_consum)
print('Connexions registrades:', connexions)
if connexions > 0:
    print('Consum mitjà per connexió:', total_consum / connexions)
