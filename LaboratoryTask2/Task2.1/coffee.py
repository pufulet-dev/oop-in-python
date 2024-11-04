from enums import Intensity

class Coffee:
    def __init__(self, coffee_intensity: Intensity, name: str = "Coffee"):
        self.__coffee_intensity = coffee_intensity
        self.__name = name

    def __str__(self):
        return f"{self.__name}: Intensity={self.__coffee_intensity.value}"