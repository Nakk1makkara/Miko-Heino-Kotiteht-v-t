#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
# (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

vuoden_ajat = ("talvi","talvi", "kevät", "kevät", "kevät", "kesä" , "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

numero = int(input("Anna kuukauden järjestysnumero (1-12): "))

vuodenaika = vuoden_ajat[numero-1]

print(vuodenaika)