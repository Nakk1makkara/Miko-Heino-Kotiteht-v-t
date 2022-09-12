import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='partaveikko96',
         autocommit=True
         )

#määritellään kysely

sql = "SELECT iso_country FROM airport"


#suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

#haetaan ja käsitellään tulos
number = 0

airport = input("anna lentokentän maakoodi : ")

tulos = kursori.fetchall()
for rivi in tulos:
    if rivi[0] == airport:
        number += 1

print(f"Lentokenttien määrä on {number}")
