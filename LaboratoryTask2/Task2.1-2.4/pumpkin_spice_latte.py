from coffee import Coffee
from enums import Intensity

class PumpkinSpiceLatte(Cappuccino):
    def __init__(self, intensity_of_coffee: Intensity, ml_of_milk: int, mg_of_pumpkin_spice: int):
        super().__init__(intensity_of_coffee, name="PumpkinSpiceLatte")
        self.__ml_of_milk = ml_of_milk
        self.__mg_of_pumpkin_spice = mg_of_pumpkin_spice

    def printDetails(self):
        super().printDetails()
        print(f"Pumpkin Spice: {self.__mg_of_pumpkin_spice} mg")

    # TODO create class specific methods
    def make_pumpkin_spice_latte(self):
        print("Making Pumpkin Spice Latte")
        # TODO reuse base classes code
        print(f"Adding {self.__mg_of_pumpkin_spice} mgs of pumpkin spice")