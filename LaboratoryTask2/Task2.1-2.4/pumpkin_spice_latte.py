from coffee import Coffee
from enums import Intensity

class PumpkinSpiceLatte(Coffee):
    def __init__(self, intensity_of_coffee: Intensity, ml_of_milk: int, mg_of_pumpkin_spice: int):
        super().__init__(intensity_of_coffee, name="PumpkinSpiceLatte")
        self.__ml_of_milk = ml_of_milk
        self.__mg_of_pumpkin_spice = mg_of_pumpkin_spice

    def printDetails(self):
        super().printDetails()
        print(f"Pumpkin Spice Latte milk: {self.__ml_of_milk} ml")
        print(f"Pumpkin Spice: {self.__mg_of_pumpkin_spice} mg")

    def makePumpkinSpiceLatte(self):
        print("Making Pumpkin Spice Latte")
        print(f"Intensity set to {self._coffee_intensity.value}")
        print(f"Adding {self.__ml_of_milk} mls of milk")
        print(f"Adding {self.__mg_of_pumpkin_spice} mgs of pumpkin spice")