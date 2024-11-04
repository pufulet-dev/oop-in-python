from coffee import Coffee
from enums import Intensity

class Cappuccino(Coffee):
    def __init__(self, intensity: Intensity, ml_of_milk: int):
        super().__init__(intensity, name="Cappuccino")
        self.__ml_of_milk = ml_of_milk

    def printDetails(self):
        print(f"Coffee intensity: {self._coffee_intensity.value}")
        print(f"Cappuccino milk: {self.__ml_of_milk} ml")

    def makeCappuccino(self):
        print("Making Cappuccino")
        print(f"Intensity set to {self._coffee_intensity.value}")
        print(f"Adding {self.__ml_of_milk} mls of milk")