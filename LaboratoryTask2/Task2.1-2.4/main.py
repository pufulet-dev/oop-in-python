from barista import Barista
from enums import Intensity

if __name__ == "__main__":
    barista = Barista()

    orders = [
        {'type': 1, 'intensity': 'NORMAL', 'ml_of_water': 150, 'name': 'Americano'},  # Americano
        {'type': 2, 'intensity': 'LIGHT', 'ml_of_milk': 100, 'name': 'Cappuccino'},   # Cappuccino
        {'type': 3, 'intensity': 'NORMAL', 'ml_of_milk': 120, 'mg_of_pumpkin_spice': 20, 'name': 'PumpkinSpiceLatte'},  # Pumpkin Spice Latte
        {'type': 4, 'intensity': 'STRONG', 'ml_of_milk': 100, 'syrup': 'VANILLA', 'name': 'SyrupCappuccino'},  # Syrup Cappuccino
    ]

    coffee_list = barista.makeCoffee(orders)