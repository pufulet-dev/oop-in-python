from cappuccino import Cappuccino
from americano import Americano
from pumpkin_spice_latte import PumpkinSpiceLatte
from syrup_cappuccino import SyrupCappuccino
from enums import Intensity, SyrupType

if __name__ == "__main__":
    cappuccino = Cappuccino(Intensity.NORMAL, 50)
    americano = Americano(Intensity.LIGHT, 660)
    pumpkin_spice_latte = PumpkinSpiceLatte(Intensity.STRONG, 100, 75)
    syrup_cappuccino = SyrupCappuccino(Intensity.NORMAL, 150, SyrupType.CARAMEL)

    print("Coffee Details:")
    cappuccino.printDetails()
    print()
    americano.printDetails()  
    print()
    pumpkin_spice_latte.printDetails()
    print()
    syrup_cappuccino.printDetails()
    print()

    print("Making Coffee:")
    cappuccino.makeCappuccino()
    print()
    pumpkin_spice_latte.makePumpkinSpiceLatte()