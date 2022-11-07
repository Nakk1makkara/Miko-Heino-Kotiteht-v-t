#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests

haku = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(haku).json()


print(vastaus["value"])

