from enums import Intensity

class Coffee:
    def __init__(self, intensity: Intensity, name: str = "Coffee"):
        self._intensity = intensity
        self._name = name

    def printDetails(self):
        print(f"Coffee Type: {self._name}")
        print(f"Coffee Intensity: {self._intensity}")

    def makeCoffee(self):
        print("------------------------------")
        print(f"Making {self._name}")
        self.printDetails()
        print("------------------------------")
        return self