from cappuccino import Cappuccino
from enums import SyrupType

class SyrupCappuccino(Cappuccino):
    def __init__(self, intensity_coffee, ml_of_milk, syrup):
        super().__init__(intensity_coffee, ml_of_milk)
        self.__syrup = syrup

    def printDetails(self):
        print(f"Coffee intensity: {self._coffee_intensity.value}")
        print(f"Syrup Cappuccino milk: {self._Cappuccino__ml_of_milk} ml") 
        print(f"Syrup: {self.__syrup.value}")

    def makeSyrupCappuccino(self):
        print("Making Syrup Cappuccino")
        print(f"Intensity set to {self._coffee_intensity.value}")
        print(f"Adding {self._Cappuccino__ml_of_milk} mls of milk")
        print(f"Adding syrup: {self.__syrup.value}")