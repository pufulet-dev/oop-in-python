from coffee import Coffee
from enums import Intensity

class Americano(Coffee):
    def __init__(self, intensity_of_coffee: Intensity, ml_of_water: int):
        super().__init__(intensity_of_coffee, name="Americano")
        self.__ml_of_water = ml_of_water

    def __str__(self):
        return f"{super().__str__()}, Water={self.__ml_of_water}ml"