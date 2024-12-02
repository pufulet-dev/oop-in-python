import sys
import os
import pytest
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dineable import PeopleDinner, RobotDinner
from refuelable import ElectricStation, GasStation
from queue_interface import NumberQueue
from car import Car
from services.semaphore import Semaphore
from services.car_station import CarStation

def test_semaphore():
    dining_service_people = PeopleDinner()
    dining_service_robots = RobotDinner()
    refueling_service_electric = ElectricStation()
    refueling_service_gas = GasStation()
    electric_queue = NumberQueue()
    gas_queue = NumberQueue()

    electric_station = CarStation(dining_service_people, refueling_service_electric, refueling_service_gas, electric_queue)
    gas_station = CarStation(dining_service_robots, refueling_service_electric, refueling_service_gas, gas_queue)

    sample_cars = [
        Car(1, "ELECTRIC", "PEOPLE", True, 20),
        Car(2, "GAS", "ROBOTS", False, 30),
        Car(3, "ELECTRIC", "ROBOTS", False, 25),
        Car(4, "GAS", "PEOPLE", True, 35),
    ]

    for car in sample_cars:
        if car.car_type == "ELECTRIC":
            electric_station.add_car(car)
        elif car.car_type == "GAS":
            gas_station.add_car(car)

    electric_station.serve_cars()
    gas_station.serve_cars()

    assert dining_service_people.people_served == 1
    assert dining_service_robots.robots_served == 1
    assert refueling_service_electric.electric_cars_served == 2
    assert refueling_service_gas.gas_cars_served == 2
    assert electric_station.total_electric_consumption == 45
    assert gas_station.total_gas_consumption == 65

# python -m pytest test_semaphore.py