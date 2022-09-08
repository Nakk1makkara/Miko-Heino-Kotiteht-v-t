#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
# joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def galloonamuunnos(gal):

    litra = gal * 3.78541178
    return litra

galloonat = float(input("anna galloonat : "))
litrat = galloonamuunnos(galloonat)
while galloonat >= 0 :
    litrat = galloonamuunnos(galloonat)
    print(f"Sinulla on {litrat:.2f} litraa")
    galloonat = float(input("anna galloonat : "))
else :
    print("ohjelma loppu")
