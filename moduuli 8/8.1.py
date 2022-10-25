import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='',
         autocommit=True
         )

sql = "SELECT ident, name, iso_region FROM airport"

kursori = yhteys.cursor()
kursori.execute(sql)

airport = input("Anna lentokentän ICAO-koodi :  ")

tulos = kursori.fetchall()
for rivi in tulos:
    if rivi[0] == airport:
        print(f"Lentokenttä on {rivi[1]}, {rivi[2]} ")

