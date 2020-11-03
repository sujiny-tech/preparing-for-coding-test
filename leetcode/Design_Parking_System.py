class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_space=[big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking_space[carType-1]==0:
            return False
        else:
            self.parking_space[carType-1]-=1
            return True


system = ParkingSystem(1,1,0) #big, medium, small
param1=system.addCar(1)
param2=system.addCar(2)
param3=system.addCar(3)
param4=system.addCar(1)
