from cappuccino import Cappuccino
from pumpkin_spice_latte import PumpkinSpiceLatte

class Barista:
    def makeCappuccino(self, intensity, ml_of_milk):
        cappuccino = Cappuccino(intensity, ml_of_milk)
        cappuccino.makeCappuccino()
        cappuccino.printDetails()

    def makePumpkinSpiceLatte(self, intensity, ml_of_milk, mg_of_pumpkin_spice):
        pumpkin_spice_latte = PumpkinSpiceLatte(intensity, ml_of_milk, mg_of_pumpkin_spice)
        pumpkin_spice_latte.makePumpkinSpiceLatte()
        pumpkin_spice_latte.printDetails()