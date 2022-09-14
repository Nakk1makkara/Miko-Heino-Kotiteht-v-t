import re
import mysql.connector
from geopy.distance import geodesic as etäisyys

#yhteyden avaus
yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='',
        autocommit=True
        )

#funktio str muutokseen
def muunna(nimi):
    uusinimi = ''.join(map(str, nimi))
    return uusinimi


#määritetään kysely
icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
sql1nimi = "SELECT name FROM airport WHERE ident = '" + icao1 + "'"
sql1 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao1 + "'"
sql2nimi = "SELECT name FROM airport WHERE ident = '" + icao2 + "'"
sql2 = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '" + icao2 + "'"

#suoritetaan kysely 1 NIMI
kursori = yhteys.cursor()
kursori.execute(sql1nimi)

#haetaan 1 NIMI
tulos1nimi = kursori.fetchall()
#muuntaa lentoaseman nimen str muotoon ja poistaa ylimääräiset merkit
nimi1 = muunna(tulos1nimi)
puhdasnimi1 = re.sub(r'[^a-zA-Z]',' ', nimi1)

#suoritetaan kysely 1 kordinaatit
kursori = yhteys.cursor()
kursori.execute(sql1)
#haetaan 1 kordinaatit
tulos1 = kursori.fetchall()


#suoritetaan kysely 2 NIMI
kursori = yhteys.cursor()
kursori.execute(sql2nimi)

#haetaan 2 NIMI
tulos2nimi = kursori.fetchall()
#muuntaa lentoaseman nimen str muotoon ja poistaa ylimääräiset merkit
nimi2 = muunna(tulos2nimi)
puhdasnimi2= re.sub(r'[^a-zA-Z]',' ', nimi2)

#suoritetaan kysely 2 kordinaatit
kursori = yhteys.cursor()
kursori.execute(sql2)
#haetaan 2 kordinaatit
tulos2 = kursori.fetchall()


#tulostaa vastauksen
print(puhdasnimi1,"ja",puhdasnimi2,"etäisyys on: ",round(etäisyys(tulos1,tulos2).km,2)," km")