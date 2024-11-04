from cappuccino import Cappuccino
from americano import Americano
from pumpkin_spice_latte import PumpkinSpiceLatte
from syrup_cappuccino import SyrupCappuccino
from enums import Intensity, SyrupType

if __name__ == "__main__":
    cappuccino = Cappuccino(Intensity.NORMAL, 200)
    americano = Americano(Intensity.LIGHT, 660)
    pumpkin_spice_latte = PumpkinSpiceLatte(Intensity.STRONG, 100, 75)
    syrup_cappuccino = SyrupCappuccino(Intensity.NORMAL, 150, SyrupType.CARAMEL)

    print(cappuccino)
    print(pumpkin_spice_latte)
    print(americano)
    print(syrup_cappuccino)