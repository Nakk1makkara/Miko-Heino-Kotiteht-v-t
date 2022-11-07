#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
# jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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

class Sahkoauto(Car):
    def __init__(self,LicensePlate, MaxSpeed, CurrentSpeed, Distance, akkukapasiteetti):

        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(LicensePlate, MaxSpeed,CurrentSpeed, Distance)

class Polttomoottori(Car):
    def __init__(self,LicensePlate, MaxSpeed, CurrentSpeed, Distance ,bensatankinkoko):
        self.bensatankinkoko = bensatankinkoko
        super().__init__(LicensePlate, MaxSpeed, CurrentSpeed, Distance)


Sahkoauto1 = Sahkoauto("ABC-15", 180, 100,0, 52.5)

polttoauto1 = Polttomoottori("ACD-123", 165, 60, 0, 32.3)


Sahkoauto1.travel(3)

polttoauto1.travel(3)

print(Sahkoauto1.Distance)

print(polttoauto1.Distance)