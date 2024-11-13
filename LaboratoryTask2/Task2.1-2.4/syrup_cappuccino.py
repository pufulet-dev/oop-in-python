from cappuccino import Cappuccino
from enums import SyrupType
from enums import Intensity

class SyrupCappuccino(Cappuccino):
    def __init__(self, intensity: Intensity, ml_of_milk: int, syrup: SyrupType, name: str = "SyrupCappuccino"):
        super().__init__(intensity, ml_of_milk, name)
        self._syrup = syrup  

    def printDetails(self):
        super().printDetails()
        print(f"Syrup: {self._syrup}")

    def makeSyrupCappuccino(self):
        print("------------------------------")
        print(f"Making {self._name}")
        self.printDetails()
        print("------------------------------")
        return self