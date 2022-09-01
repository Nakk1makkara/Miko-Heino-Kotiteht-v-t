#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

summa= 0
arpa = int(input("Kuinka monta noppaa haluat heittää? : "))

for luku in range(arpa) :
    noppa = random.randint(1, 6)
    summa = summa + noppa

print(f"Noppien silmälukujen summa on {summa}.")



