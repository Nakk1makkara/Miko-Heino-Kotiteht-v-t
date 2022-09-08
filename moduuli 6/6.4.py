#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def laske(luvut):
    vastaus = 0
    for num in range(0,len(luvut)):
        vastaus = vastaus + luvut[num]
    return vastaus
lista=[1,2,3,4, 5]
yhteenlasku = laske(lista)
print ("vastaus on: ",yhteenlasku)