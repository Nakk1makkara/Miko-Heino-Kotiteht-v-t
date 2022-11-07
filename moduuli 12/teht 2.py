#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

def main():
    api_key = '8a492fb462363a9123392be795a4fa25'


    city = input("Enter a city name: ")

    city_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').json()

    lat = city_data['coord']['lat']
    lon = city_data['coord']['lon']

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url).json()
    print(response['weather'][0]['description'], str(response['main']['temp'] - 273.15) + '°C')

main()
