#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = (input("anna luku : "))

suurin = pienin = int(luku)

while luku != "" :
    int(luku)
    lukuint = int(luku)
    if lukuint < pienin :
        pienin = lukuint
    if int(luku) > suurin :
    lukuint = int(luku)
    suurin = lukuint
    luku = (input("anna luku : "))
print(f"pienin luku on {pienin}")
print(f"suurin luku on {suurin}")
