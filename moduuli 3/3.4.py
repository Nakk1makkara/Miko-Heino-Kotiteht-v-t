#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Syötä vuosiluku : "))



if vuosi % 4 == 0 and(vuosi % 400 == 0):
     print("Vuosi on karkausvuosi.")
elif vuosi % 4 == 0 :
    print("Vuosi on karkausvuosi.")
else:
    print("vuosi ei ole karkausvuosi.")
