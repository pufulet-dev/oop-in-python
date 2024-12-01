import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dineable import Dineable, PeopleDinner, RobotDinner
from refuelable import Refuelable, ElectricStation, GasStation
from queue_interface import Queue, NumberQueue
from car import Car
from services.car_station import CarStation

def test_carstation_full_processing():
    dining_service = PeopleDinner()
    electric_refueling_service = ElectricStation()
    gas_refueling_service = GasStation()
    car_queue = NumberQueue()

    car_station = CarStation(dining_service, electric_refueling_service, gas_refueling_service, car_queue)

    car_station.add_car(Car(1, "ELECTRIC", "PEOPLE", True, 20))
    car_station.add_car(Car(2, "GAS", "ROBOTS", False, 30))
    car_station.add_car(Car(3, "ELECTRIC", "ROBOTS", False, 25))
    car_station.add_car(Car(4, "GAS", "PEOPLE", True, 35))

    car_station.serve_cars()

    assert dining_service.people_served == 2
    assert electric_refueling_service.electric_cars_served == 2
    assert gas_refueling_service.gas_cars_served == 2
    assert car_station.total_electric_consumption == 45
    assert car_station.total_gas_consumption == 65

def test_empty_queue():
    dining_service = PeopleDinner()
    electric_refueling_service = ElectricStation()
    gas_refueling_service = GasStation()
    car_queue = NumberQueue()

    car_station = CarStation(dining_service, electric_refueling_service, gas_refueling_service, car_queue)

    car_station.serve_cars()

    assert dining_service.people_served == 0
    assert electric_refueling_service.electric_cars_served == 0
    assert gas_refueling_service.gas_cars_served == 0
    assert car_station.total_electric_consumption == 0
    assert car_station.total_gas_consumption == 0

def test_partial_processing():
    dining_service = PeopleDinner()
    electric_refueling_service = ElectricStation()
    gas_refueling_service = GasStation()
    car_queue = NumberQueue()

    car_station = CarStation(dining_service, electric_refueling_service, gas_refueling_service, car_queue)

    car_station.add_car(Car(1, "ELECTRIC", "PEOPLE", True, 20))
    car_station.add_car(Car(2, "GAS", "ROBOTS", False, 30))

    car_station.serve_cars()

    assert dining_service.people_served == 1
    assert electric_refueling_service.electric_cars_served == 1
    assert gas_refueling_service.gas_cars_served == 1
    assert car_station.total_electric_consumption == 20
    assert car_station.total_gas_consumption == 30

# python -m pytest test_carstation.py