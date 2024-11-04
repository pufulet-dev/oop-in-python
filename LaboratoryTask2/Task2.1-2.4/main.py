from barista import Barista
from enums import Intensity

if __name__ == "__main__":
    barista = Barista()
    barista.makeCappuccino(Intensity.NORMAL, 50)
    print()
    barista.makePumpkinSpiceLatte(Intensity.STRONG, 100, 50)