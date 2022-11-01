#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class House:
    def __init__(self, FirstFloor, HighestFloor, Elevators):
        self.FirstFloor = FirstFloor
        self.HighestFloor = HighestFloor
        self.Elevators = Elevators
        self.ElevatorsList = []

    def CreateElevators(self):
        for i in range(self.Elevators):
            Elevator = Elevator(self.FirstFloor, self.HighestFloor, 0)
            self.ElevatorsList.append(Elevator)

    def DriveElevator(self, ElevatorNumber, DestinationFloor):
        ElevatorToDrive = self.ElevatorsList[ElevatorNumber]
        while DestinationFloor > Elevator.CurrentFloor:
            Elevator.CurrenFloor + 1
            print(f"Kerros", Elevator.CurrentFloor)
            if DestinationFloor > self.HighestFloor


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

House1 = House(1,12, 3)

