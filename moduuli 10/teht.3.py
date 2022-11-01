#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
class Elevator:
    def __init__(self, FirstFloor, HighestFloor, CurrentFloor):
        self.FirstFloor = FirstFloor
        self.HighestFloor = HighestFloor
        self.CurrentFloor = CurrentFloor
    def GoToFloor(self, SelectedFloor, ElevatorNumber):
        if SelectedFloor > self.CurrentFloor
            while SelectedFloor > self.CurrentFloor:
                House1.ElevatorsList[ElevatorNumber].Up()

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



class House:
    def __init__(self, FirstFloor, HighestFloor, Elevators):
        self.FirstFLoor = FirstFloor
        self.HighestFLoor = HighestFloor
        self.Elevators = Elevators
        self.ElevatorsList = []
        for i in range(Elevators):
            self.ElevatorsList.append(Elevator(FirstFloor, HighestFloor, 0))

    def DriveElevator(self, ElevatorNumber, DestinationFloor):
            self.ElevatorsList[ElevatorNumber].GoToFloor(DestinationFloor, ElevatorNumber)


House1 = House(1, 12, 3)
print(House1.ElevatorsList)
House1.DriveElevator(2, 3)