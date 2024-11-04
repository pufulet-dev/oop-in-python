from coffee import Coffee
from enums import Intensity

class Cappuccino(Coffee):
    def __init__(self, intensity: Intensity, ml_of_milk: int):
        super().__init__(intensity, name="Cappuccino")
        self._ml_of_milk = ml_of_milk

    def printDetails(self):
        self.printCoffeeDetails()
        print(f"Cappuccino milk: {self._ml_of_milk} ml")