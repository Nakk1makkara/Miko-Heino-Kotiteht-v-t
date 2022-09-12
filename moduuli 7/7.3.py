#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

def valitse():
    print("1 - syötä uusi")
    print("2 - haku")
    print("0 - lopetus")
    valinta= -1
    while valinta < 0 or > 2:
        return valinta
def lisääUusi(asemat):
    icao = input("Aseman ICAO-koodi : ")
    nimi = input("Aseman nimi       : ")
    asemat[icao] = nimi
def hae(asemat)
    icao = input("Aseman ICAO-koodi : ")
    if icao in asemat:
        print(asemat[icao])
    else:
        print("Tuntematon ICAO-koodi")


lentoasemat = {"Helsinki-Vantaa":"EFHK",
               "Edmonton International Airport":"CYEG",
               "Uumajan lentoasema":"ESNU"}
valinta = valitse()
while valinta != 0:
    if valinta == 1:
        lisääUusi(lentoasemat)
    elif valinta == 2:
        hae(lentoasemat)
    valinta = valitse()