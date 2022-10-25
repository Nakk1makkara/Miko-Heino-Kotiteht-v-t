#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, LicensePlate, MaxSpeed, CurrentSpeed, Distance):
        self.LicensePlate = LicensePlate
        self.MaxSpeed = MaxSpeed
        self.CurrentSpeed = CurrentSpeed
        self.Distance = Distance





car1 = Car("NIX-991", 240, 0, 0)

print(f"Auto 1. \nrekisteritunnus:", car1.LicensePlate, "\nHuippunopeus :", car1.MaxSpeed, "KM/H")
