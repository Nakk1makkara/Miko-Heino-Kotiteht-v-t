#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen
# kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def poista(lista2):
    for n in lista:
        if n % 2 == 0:
            lista2.append(n)
    return lista2
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
print(lista)
print(poista(lista2))