import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='OMA SALASANA TÄNNE',
         autocommit=True
         )

#määritellään kysely

sql = "SELECT name, continent FROM country"


#suoritetaan kysely
kursori = yhteys.cursor()
kursori.execute(sql)

#haetaan ja käsitellään tulos
tulos = kursori.fetchall()
for rivi in tulos:
    print(f"{rivi[0]}, {rivi[1]}")
