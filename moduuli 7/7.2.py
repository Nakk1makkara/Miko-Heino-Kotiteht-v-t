#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai
# Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()
nimi = (input("Anna nimi : "))
nimet.add(nimi)
while nimi != "" :
    if nimi in nimet :
        print(f"{nimi} on jo lisätty listaan! ")
    else :
        nimi = input("Anna nimi : ")
    nimet.add(nimi)


for i in nimet:
    print(i)