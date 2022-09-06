#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
# argumentiksi reverse=True.

lista = []

numero = input('Anna numeroita ja paina lopuksi "enter" : ' )
lista.append(numero)
while numero != "" :
    if numero == "":
        break
    numero = input(' : ')
    lista.append(numero)

lista.sort()
print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])