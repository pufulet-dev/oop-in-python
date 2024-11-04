from coffee import Coffee
from enums import Intensity

class PumpkinSpiceLatte(Coffee):
    def __init__(self, intensity_of_coffee: Intensity, ml_of_milk: int, mg_of_pumpkin_spice: int):
        super().__init__(intensity_of_coffee, name="PumpkinSpiceLatte")
        self._ml_of_milk = ml_of_milk 
        self._mg_of_pumpkin_spice = mg_of_pumpkin_spice  

    def printDetails(self):
        self.printCoffeeDetails()
        print(f"Pumpkin Spice Latte milk: {self._ml_of_milk} ml")
        print(f"Pumpkin Spice: {self._mg_of_pumpkin_spice} mg")