#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
# onko se alkuluku. Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

kokonaisluku = float(input("anna luku niin kerron onko se alkuluku. : "))

numero_lista = [9, 8, 7, 6, 5, 4, 3, 2]
alkuluku = False

if kokonaisluku / kokonaisluku == 1 and kokonaisluku / 1 == kokonaisluku:
    alkuluku = True

for numero in numero_lista:
   if kokonaisluku % numero == 0:
       alkuluku = False


if alkuluku == True:
    print(f"numero {kokonaisluku} on alkuluku")
else:
    print(f"numero {kokonaisluku} ei ole alkuluku")

