from coffee import Coffee
from enums import Intensity

class Cappuccino(Coffee):
    def __init__(self, intensity: Intensity, ml_of_milk: int):
        super().__init__(intensity, name="Cappuccino")
        self.__ml_of_milk = ml_of_milk

    def __str__(self):
        return f"{super().__str__()}, Milk={self.__ml_of_milk}ml"