# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = float(input("Anna kuhan pituus senttimetreinä : "))

täysmitta = 37

if kuha>=37:
    print("Kuha on täysimittainen.")
else:
    print("Laske kuha takaisin järveen se on alamittainen. ")
    print(f"Kuhan pitäisi olla {täysmitta-kuha} senttimetriä pidempi. ")