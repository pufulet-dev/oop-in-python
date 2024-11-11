from coffee import Coffee
from enums import Intensity

class Americano(Coffee):
    def __init__(self, intensity: Intensity, ml_of_water: int):
        super().__init__(intensity, name="Americano")
        self._ml_of_water = ml_of_water 

    def printDetails(self):
        print(f"Coffee Type: {self._name}")
        print(f"Intensity: {self._coffee_intensity.value}")
        print(f"Americano water: {self._ml_of_water} ml")

    def make_coffee(self):
        print("Making Americano")
        print(f"Intensity set to {self._coffee_intensity.value}")
        print(f"Adding {self._ml_of_water} mls of water")