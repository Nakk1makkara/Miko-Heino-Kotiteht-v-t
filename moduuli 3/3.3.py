# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
gender = input("Sukupuolesi (nainen/mies)? : ")

hemo = int(input("Hemoglobiini (g/l)? : "))

if gender == "nainen" :
    if hemo < 117 :
        print("Hemoglobiiniarvo on alhainen")
    elif hemo <= 175 :
        print("Hemoglobiiniarvo on viite-arvossa")
    else:
        print("Hemoglobiiniarvosi on korkea.")

elif gender == "mies" :
    if hemo < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemo <= 195:
        print("Hemoglobiiniarvo on viite-arvossa")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("syöte virheellinen.")