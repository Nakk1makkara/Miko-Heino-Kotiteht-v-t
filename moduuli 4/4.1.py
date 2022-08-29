#Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

kolmijakonen_luku = 0

while kolmijakonen_luku <= 1000:
    if kolmijakonen_luku % 3 == 0 :
        print(kolmijakonen_luku)
        kolmijakonen_luku = kolmijakonen_luku + 1
    else:
        kolmijakonen_luku = kolmijakonen_luku + 1