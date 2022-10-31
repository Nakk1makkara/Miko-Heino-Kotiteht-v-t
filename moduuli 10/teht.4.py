#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:

#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.

#Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa aja tunti-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen,
# kun kilpailu on päättynyt.

import random
class Car:
    def __init__(self, LicensePlate, MaxSpeed, CurrentSpeed, Distance):
        self.LicensePlate = LicensePlate
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = CurrentSpeed
        self.Distance = Distance

    def travel(self, time):
        self.Distance = self.Distance + self.CurrentSpeed * time
    def accelerate(self, speed):

        self.CurrentSpeed = self.CurrentSpeed + speed
        if self.CurrentSpeed > self.MaxSpeed :
            self.CurrentSpeed = self.MaxSpeed
        elif self.CurrentSpeed + speed <= 0 :
            self.CurrentSpeed = 0
        elif self.CurrentSpeed >= self.MaxSpeed:
            self.CurrentSpeed = self.MaxSpeed
    def PrintInfo (self):
        print(f"\nAuton rekisteritunnus :", self.LicensePlate)
        print(f"Huippunopeus:", self.MaxSpeed, "KM/H")
        print("Tämänhetkinen nopeus:", self.CurrentSpeed, "KM/H")
        print("Kuljettu matka :", self.Distance, "KM")



car1 = Car("NIX-991", 240, 0, 0)

OtherCars = []

for i in range(10):
    car = Car("ABC-"+ str(i + 1), random.randint(100, 200), 0, 0)
    OtherCars.append(car)

race_over = False

for car in OtherCars:
    car.PrintInfo()

while race_over == False:
    for car in OtherCars:
        car.travel(1)
        car.accelerate(random.randint(-10, 15))

    for car in OtherCars:
        if car.Distance >= 1000:
            race_over = True


for car in OtherCars:
    if car.Distance >= 1000:
        print(f"\n\nVoittaja on {car.LicensePlate}", car.Distance, "KM")


