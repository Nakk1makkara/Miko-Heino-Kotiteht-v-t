#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, name):
        self.julkaisun_nimi = name

class Lehti(Julkaisu):
    def __init__(self, toimittaja, name):
        self.headjournalist = toimittaja
        super().__init__(name)

    def tulosta_tiedot(self):
        print(self.julkaisun_nimi, self.headjournalist)

class Kirja(Julkaisu):
    def __init__(self, kirjailija, sivumäärä, name):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
        super().__init__(name)

    def tulosta_tiedot(self):
        print(self.julkaisun_nimi, self.sivumäärä, self.kirjailija)

AkuAnkka = Lehti("AkiHyyppä", "aku_ankka")

hytti6 = Kirja("Rosa Liksom", 200, "Hytti6")


AkuAnkka.tulosta_tiedot()

hytti6.tulosta_tiedot()
