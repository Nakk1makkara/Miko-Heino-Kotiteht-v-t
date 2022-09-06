#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

lista = []
t = 0
kaupunki = input("Anna ensimmäinen kaupunki tai lopeta painamalla Enter: ")
t = t +1

while kaupunki!="" and t != 5:
    lista.append(kaupunki)
    kaupunki = input("Anna seuraava kaupunki tai lopeta painamalla Enter: ")
    t = t +1

for n in lista :
    print ({n})