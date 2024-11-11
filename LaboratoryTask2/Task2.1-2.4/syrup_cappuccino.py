from cappuccino import Cappuccino
from enums import SyrupType

class SyrupCappuccino(Cappuccino):
    def __init__(self, intensity, ml_of_milk, syrup: SyrupType):
        super().__init__(intensity, ml_of_milk)
        self._syrup = syrup  

    def printDetails(self):
        print(f"Coffee Type: Syrup Cappuccino")
        print(f"Intensity: {self._coffee_intensity.value}")
        print(f"Syrup Cappuccino milk: {self._ml_of_milk} ml")
        print(f"Syrup: {self._syrup} ml")

    def make_coffee(self):
        print("Making Syrup Cappuccino")
        print(f"Intensity set to {self._coffee_intensity.value}")
        print(f"Adding {self._ml_of_milk} mls of milk")
        print(f"Adding syrup: {self._syrup} ml")