from coffee import Coffee
from enums import Intensity

class Cappuccino(Coffee):
    def __init__(self, intensity: Intensity, ml_of_milk: int, name: str = "Cappuccino"):
        super().__init__(intensity, name)
        self._ml_of_milk = ml_of_milk  

    def printDetails(self):
        super().printDetails()
        print(f"Cappuccino milk: {self._ml_of_milk} ml")

    def makeCappuccino(self):
        print("------------------------------")
        print(f"Making {self._name}")
        self.printDetails()
        print("------------------------------")
        return self