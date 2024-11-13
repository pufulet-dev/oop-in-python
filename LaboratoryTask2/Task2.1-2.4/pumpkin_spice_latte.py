from coffee import Coffee
from enums import Intensity
from cappuccino import Cappuccino

class PumpkinSpiceLatte(Cappuccino):
    def __init__(self, intensity: Intensity, ml_of_milk: int, mg_of_pumpkin_spice: int, name: str = "PumpkinSpiceLatte"):
        super().__init__(intensity, ml_of_milk, name)
        self._mg_of_pumpkin_spice = mg_of_pumpkin_spice

    def printDetails(self):
        super().printDetails()
        print(f"Pumpkin Spice: {self._mg_of_pumpkin_spice} mg")

    def makePumpkinSpiceLatte(self):
        print("------------------------------")
        print(f"Making {self._name}")
        self.printDetails()
        print("------------------------------")
        return self