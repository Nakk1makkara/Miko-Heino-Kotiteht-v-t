#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = (input("anna luku : "))

suurin = pienin = int(luku)

while luku != "" :
    luku = input("anna luku : ")
    if luku == "":
        break
    lukuint = int(luku)
    if lukuint < pienin :
        pienin = lukuint
    if lukuint > suurin :
        suurin = lukuint

print(f"pienin luku on {pienin}")
print(f"suurin luku on {suurin}")
