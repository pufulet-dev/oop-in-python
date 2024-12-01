import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dineable import Dineable, PeopleDinner, RobotDinner
from refuelable import Refuelable, ElectricStation, GasStation
from queue_interface import Queue, NumberQueue
from car import Car
from services.car_station import CarStation

class Semaphore:
    def __init__(self, electric_station: CarStation, gas_station: CarStation):
        self.electric_station = electric_station
        self.gas_station = gas_station

    def guide_car(self, car: Car) -> None:
        if car.car_type == "ELECTRIC":
            self.electric_station.add_car(car)
        elif car.car_type == "GAS":
            self.gas_station.add_car(car)

    def serve_all(self) -> None:
        self.electric_station.serve_cars()
        self.gas_station.serve_cars()