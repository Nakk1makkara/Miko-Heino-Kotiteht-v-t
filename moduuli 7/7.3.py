#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

def choose():
    print("1 Anna uusi")
    print("2 hae")
    print("0 lopeta")
    choice = -1
    while choice < 0 or choice > 2:
        choice = int(input("Valitse: "))
    return choice


def add_new(airports):
    icao = input("Aseman ICAO koodi: ")
    name = input("Aseman nimi: ")
    airports[icao] = name


def search(airports):
    icao = input("Aseman ICAO koodi: ")
    if icao in airports:
        print(airports[icao])
    else:
        print("Tuntemanton koodi")


airport_list = {}
choice = choose()
while choice != 0:
    if choice == 1:
        add_new(airport_list)
    elif choice == 2:
        search(airport_list)
    choice = choose()