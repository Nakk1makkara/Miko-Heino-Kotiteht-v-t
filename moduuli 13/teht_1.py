#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa:
# {"Number":31, "isPrime":true}.
from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):



    is_not_prime_number = False

    for i in range(2, luku):
        jakojäänne = luku % i
        if jakojäänne == 0:
            is_not_prime_number = True
            break

    if is_not_prime_number:
        response_dict = {"Number": str(luku), "isPrime": "False"}

    else:
        response_dict = {"Number": str(luku), "IsPrime": "True"}

    return Response(json.dumps(response_dict), status=200, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)




