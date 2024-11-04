from coffee import Coffee
from enums import Intensity

class PumpkinSpiceLatte(Coffee):
    def __init__(self, intensity_of_coffee: Intensity, ml_of_milk: int, mg_of_pumpkin_spice: int):
        super().__init__(intensity_of_coffee, name="PumpkinSpiceLatte")
        self.__ml_of_milk = ml_of_milk
        self.__mg_of_pumpkin_spice = mg_of_pumpkin_spice

    def __str__(self):
        return f"{super().__str__()}, Milk={self.__ml_of_milk}ml, Pumpkin Spice={self.__mg_of_pumpkin_spice}mg"