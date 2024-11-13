from cappuccino import Cappuccino
from pumpkin_spice_latte import PumpkinSpiceLatte
from americano import Americano
from syrup_cappuccino import SyrupCappuccino

class Barista:
    def makeCoffee(self, orders):
        coffee_list = []
        for order in orders:
            match order['type']:
                case 1:
                    americano = Americano(order['intensity'], order['ml_of_water'], "Americano")
                    americano.makeAmericano()
                    coffee_list.append(americano)
                case 2:
                    cappuccino = Cappuccino(order['intensity'], order['ml_of_milk'], "Cappuccino")
                    cappuccino.makeCappuccino()
                    coffee_list.append(cappuccino)
                case 3:
                    pumpkin_spice_latte = PumpkinSpiceLatte(order['intensity'], order['ml_of_milk'], order['mg_of_pumpkin_spice'], "PumpkinSpiceLatte")
                    pumpkin_spice_latte.makePumpkinSpiceLatte()
                    coffee_list.append(pumpkin_spice_latte)
                case 4:
                    syrup_cappuccino = SyrupCappuccino(order['intensity'], order['ml_of_milk'], order['syrup'], "SyrupCappuccino")
                    syrup_cappuccino.makeSyrupCappuccino()
                    coffee_list.append(syrup_cappuccino)
        
        return coffee_list