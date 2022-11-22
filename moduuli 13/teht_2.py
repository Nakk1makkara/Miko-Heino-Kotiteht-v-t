#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän
# nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.


from flask import Flask, request
import mysql.connector

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='',
        autocommit=True
        )

app = Flask(name)
app.config['JSON_SORT_KEYS'] = False
@app.route('/airport')

def Lentokenttä():
    args = request.args
    icao = (args.get("airport"))
    sql_name = "Select name from airport where ident = '" + icao + "'"
    sql_munici = "Select municipality from airport where ident = '" + icao + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql_name)
    sql_return_name = kursori.fetchone()

    kursori = yhteys.cursor()
    kursori.execute(sql_munici)
    sql_return_munici = kursori.fetchone()

    sql_print = {
        "ICAO": icao,
        "Name": sql_return_name[0],
        "Municipality": sql_return_munici[0]
    }

    return sql_print

if name == 'main':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)