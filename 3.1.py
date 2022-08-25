# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

Kuha = float(input("Anna kuhan pituus senttimetreinä : "))

if Kuha>=37:
    print("Kuha on täysimittainen.")
else:
    print("Laske kuha takaisin järveen se on alamittainen. ")