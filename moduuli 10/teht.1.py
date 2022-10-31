#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
# että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:
    def __init__(self, FirstFloor, HighestFloor, CurrentFloor):
        self.FirstFloor = FirstFloor
        self.HighestFloor = HighestFloor
        self.CurrentFloor = CurrentFloor

    def Up(self, Floors):
        if self.CurrentFloor < self.HighestFloor:
            for i in range(Floors):
                if self.CurrentFloor == self.HighestFloor:
                    self.CurrentFloor = self.HighestFloor
                    print("Ylin kerros.")
                    return
                self.CurrentFloor = self.CurrentFloor + 1
                print(f"Kerros", self.CurrentFloor)


    def Down(self, Floors):
        for i in range(Floors):
            if self.CurrentFloor == self.FirstFloor :
                self.CurrentFloor = self.FirstFloor
                print("Alin kerros")
                return
            self.CurrentFloor = self.CurrentFloor - 1
            print(f"Kerros", self.CurrentFloor)






Elevator1 = Elevator(0, 8, 0)

Elevator1.Up(100)

Elevator1.Down(100)