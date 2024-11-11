from barista import Barista
from enums import Intensity

if __name__ == "__main__":
    barista = Barista()

    barista.makeCappuccino(Intensity.NORMAL, 50)
    barista.makePumpkinSpiceLatte(Intensity.STRONG, 100, 50)
    barista.makeSyrupCappuccino(Intensity.NORMAL, 30, 12)
    barista.makeAmericano(Intensity.LIGHT, 100)