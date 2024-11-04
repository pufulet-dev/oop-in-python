from cappuccino import Cappuccino
from enums import Intensity, SyrupType

class SyrupCappuccino(Cappuccino):
    def __init__(self, intensity_coffee: Intensity, ml_of_milk: int, syrup: SyrupType):
        super().__init__(intensity_coffee, ml_of_milk)
        self._syrup = syrup

    def printDetails(self):
        self.printCoffeeDetails()
        print(f"Syrup Cappuccino milk: {self._ml_of_milk} ml")
        print(f"Syrup: {self._syrup.value}")