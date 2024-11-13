from coffee import Coffee
from enums import Intensity

class Americano(Coffee):
    def __init__(self, intensity: Intensity, ml_of_water: int, name: str = "Americano"):
        super().__init__(intensity, name)
        self._ml_of_water = ml_of_water 

    def printDetails(self):
        super().printDetails()
        print(f"Americano water: {self._ml_of_water} ml")

    def makeAmericano(self):
        print("------------------------------")
        print(f"Making {self._name}")
        self.printDetails()
        print("------------------------------")
        return self