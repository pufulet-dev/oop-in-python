from enum import Enum

class Intensity(Enum):
    LIGHT = "LIGHT"
    NORMAL = "NORMAL"
    STRONG = "STRONG"

class SyrupType(Enum):
    MACADAMIA = "MACADAMIA"
    VANILLA = "VANILLA"
    COCONUT = "COCONUT"
    CARAMEL = "CARAMEL"
    CHOCOLATE = "CHOCOLATE"
    POPCORN = "POPCORN"