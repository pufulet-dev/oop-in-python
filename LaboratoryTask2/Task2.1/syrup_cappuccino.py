from cappuccino import Cappuccino
from enums import Intensity, SyrupType

class SyrupCappuccino(Cappuccino):
    def __init__(self, intensity_coffee: Intensity, ml_of_milk: int, syrup: SyrupType):
        super().__init__(intensity_coffee, ml_of_milk)
        self.__name = "SyrupCappuccino"  
        self.__syrup = syrup

    def __str__(self):
        return f"{super().__str__()}, Syrup={self.__syrup.value}"