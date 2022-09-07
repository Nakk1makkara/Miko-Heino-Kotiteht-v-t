#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random
def noppa():
    nop = random.randint(1, 6)
    return nop
silmäluku = noppa()
while silmäluku != 6 :
    noppa()
    silmäluku = noppa()
    print(silmäluku)