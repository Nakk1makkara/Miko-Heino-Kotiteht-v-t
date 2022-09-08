import math
def PizzaArvo(halkaisijaCm, hinta):
    sade = float(halkaisijaCm / 2)
    pintaalaM = (math.pi * sade * sade) / 1000
    arvo = hinta / pintaalaM
    return arvo

pizzat = []

for x in range (2):
    print(f"Anna pizza {x}, tiedot ")
    hinta = float(input("Syötä pizzan hinta : "))
    halkaisija = float(input("Syötä pizzan halkaisija :"))
    pizzat.append(PizzaArvo(halkaisija, hinta))

arvokkaimmanID = 0
for x in range (2):
    if pizzat[arvokkaimmanID] > pizzat[x]:
        arvokkaimmanID = x

print(f"Paras Hinta-kokosuhde on pizzalla {arvokkaimmanID}. ")