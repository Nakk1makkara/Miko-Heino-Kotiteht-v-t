#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class House:
    def __init__(self, FirstFloor, HighestFloor, Elevators):
        self.FirstFLoor = FirstFloor
        self.HighestFLoor = HighestFloor
        self.Elevators = Elevators
        self.ElevatorsList = []

    def CreateElevators(self):
        for i in range(self.Elevators):
            Elevator = Elevator(self.FirstFloor, self.HighestFloor, self.CurrentFloor)
            self.ElevatorsList.append(Elevator)

    def DriveElevator


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

DriveElevator(2, 3)