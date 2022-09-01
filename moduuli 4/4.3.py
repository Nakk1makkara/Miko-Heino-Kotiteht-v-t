#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = float(input("anna luku : "))

suurin = -1000000000000000000000000000000000000000000000000000000000000000
pienin = 10000000000000000000000000000000000000000000000000000000000000000

while luku != 1000 :
    if luku < suurin or luku < pienin:
        pienin = 0 + luku

    elif luku > suurin :
        suurin = 0 + luku

    luku = float(input("anna luku : "))


print(f"pienin luku on {pienin}")
print(f"suurin luku on {suurin}")
