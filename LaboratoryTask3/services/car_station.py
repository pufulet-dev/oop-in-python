import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dineable import Dineable, PeopleDinner, RobotDinner
from refuelable import Refuelable, ElectricStation, GasStation
from queue_interface import Queue, NumberQueue
from car import Car

class CarStation:
    def __init__(self, dining_service: PeopleDinner, electric_refueling_service: ElectricStation, gas_refueling_service: GasStation, queue: NumberQueue):
        self.dining_service = dining_service
        self.electric_refueling_service = electric_refueling_service
        self.gas_refueling_service = gas_refueling_service
        self.queue = queue
        self.total_electric_consumption = 0
        self.total_gas_consumption = 0

    def add_car(self, car: Car) -> None:
        self.queue.enqueue(car)

    def serve_cars(self) -> None:
        while not self.queue.is_empty():
            car = self.queue.dequeue()

            if car.is_dining:
                self.dining_service.serveDinner(car.car_id)

            if car.car_type == "ELECTRIC":
                self.electric_refueling_service.refuel(car.car_id)
                self.total_electric_consumption += car.consumption
            elif car.car_type == "GAS":
                self.gas_refueling_service.refuel(car.car_id)
                self.total_gas_consumption += car.consumption