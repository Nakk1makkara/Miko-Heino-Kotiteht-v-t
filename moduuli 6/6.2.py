#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def noppa():
    nop = tahkot
    nop = random.randint(1, tahkot)
    return nop

tahkot = int(input("Anna tahkojen määrä. : "))
silmäluku = noppa()
while silmäluku != tahkot :
    noppa()
    silmäluku = noppa()
    print(silmäluku)


