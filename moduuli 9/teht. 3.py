#Laajenna ohjelmaa siten, että mukana on kulje-metodi,
# joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella
# vauhdilla annetussa tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

car1.accelerate(30)
car1.travel(1)
car1.accelerate(70)
car1.travel(1)
car1.accelerate(50)
car1.travel(1)

car1.PrintInfo()
