#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
# että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Car:
    def __init__(self, LicensePlate, MaxSpeed, CurrentSpeed, Distance):
        self.LicensePlate = LicensePlate
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = CurrentSpeed
        self.Distance = Distance
    def accelerate(self, speed):
        if 0 < self.CurrentSpeed + speed:
            if self.CurrentSpeed > self.MaxSpeed :
                self.CurrentSpeed = self.MaxSpeed
            self.CurrentSpeed = self.CurrentSpeed + speed
        elif self.CurrentSpeed + speed <= 0 :
            self.CurrentSpeed = 0
        elif self.CurrentSpeed >= self.MaxSpeed:
            self.CurrentSpeed = self.MaxSpeed
    def PrintInfo (self):
        print(f"\nAuton rekisteritunnus :", self.LicensePlate)
        print(f"Huippunopeus:", self.MaxSpeed, "KM/H")
        print("Tämänhetkinen nopeus:", self.CurrentSpeed, "KM/H")
        print("Kuljettu matka :", self.Distance, "m")



car1 = Car("NIX-991", 240, 0, 0)

car1.PrintInfo()


car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(200)


car1.PrintInfo()


