import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from refuelable import ElectricStation, GasStation

def test_electric_station():
    electric_station = ElectricStation()
    electric_station.refuel("Car3")
    assert electric_station.electric_cars_served == 1

def test_gas_station():
    gas_station = GasStation()
    gas_station.refuel("Car4")
    assert gas_station.gas_cars_served == 1

# python -m pytest test_refuelable.py