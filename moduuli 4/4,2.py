#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.

tuuma = float(input('Anna "tuumat" niin muunnan ne senttimetreiksi : '))

while tuuma >= 0 :
    tuuma = tuuma / 0.39370079
    print(f"{tuuma:6.2f} senttimetriä")
    tuuma = float(input("Anna tuumat niin muunnan ne senttimetreiksi : "))

print("virheellinen numero aloita alusta....")