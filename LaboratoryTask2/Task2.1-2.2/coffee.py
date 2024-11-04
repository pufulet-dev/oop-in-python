from enums import Intensity

class Coffee:
    def __init__(self, coffee_intensity: Intensity, name: str = "Coffee"):
        self._coffee_intensity = coffee_intensity
        self._name = name

    def printCoffeeDetails(self):
        print(f"Coffee intensity: {self._coffee_intensity.value}")

    def __str__(self):
        return f"{self._name}: Intensity={self._coffee_intensity.value}"