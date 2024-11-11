from cappuccino import Cappuccino
from pumpkin_spice_latte import PumpkinSpiceLatte
from americano import Americano
from syrup_cappuccino import SyrupCappuccino

class Barista:
    def makeCoffee("list of orders"):
        # listCoffee
        # use match, based on the list create the coffee type
        # if 1 -> listCoffee.add(Americano())
        # if 2 -> listCOffee.add(Cappuccino())

        # use a for loop (coffee in listCoffee)
        # check the type of coffee
        # if Americano -> coffee.makeCoffee()
        # if PumpkinSpiceLatte -> coffee.makePumpkinSpiceLatte

    def makeCappuccino(self, intensity, ml_of_milk):
        cappuccino = Cappuccino(intensity, ml_of_milk)
        cappuccino.make_coffee()
        print()
        cappuccino.printDetails()
        print("-------------------")
        return cappuccino # TODO return the coffee

    def makePumpkinSpiceLatte(self, intensity, ml_of_milk, mg_of_pumpkin_spice):
        pumpkin_spice_latte = PumpkinSpiceLatte(intensity, ml_of_milk, mg_of_pumpkin_spice)
        pumpkin_spice_latte.make_coffee()
        print()
        pumpkin_spice_latte.printDetails()
        print("-------------------")

    def makeAmericano(self, intensity, ml_of_water):
        americano = Americano(intensity, ml_of_water)
        americano.make_coffee()
        print()
        americano.printDetails()
        print("-------------------")

    def makeSyrupCappuccino(self, intensity, ml_of_milk, syrup):
        syrup_cappuccino = SyrupCappuccino(intensity, ml_of_milk, syrup)
        syrup_cappuccino.make_coffee()
        print()
        syrup_cappuccino.printDetails()
        print("-------------------")