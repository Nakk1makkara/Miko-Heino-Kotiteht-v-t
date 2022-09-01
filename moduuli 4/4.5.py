#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules)

käyttäjä = "python"
sala = "rules"
yritykset = 0

arvaus1 = str(input("Anna käyttäjätunnus : "))
arvaus2 = str(input("Anna salasana : "))
yritykset = yritykset + 1
while arvaus1 != käyttäjä and arvaus2 != sala :

    arvaus1 = str(input("Anna käyttäjätunnus : "))
    arvaus2 = str(input("Anna salasana : "))
    yritykset = yritykset + 1
    if yritykset == 5 :
        break



if yritykset == 5 :
    print("Pääsy evätty.")
else:
    print("Tervetuloa!")
