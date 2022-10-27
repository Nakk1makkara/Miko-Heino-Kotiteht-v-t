#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.

#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
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

