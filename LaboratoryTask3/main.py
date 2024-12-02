import time
import os
import json
from queue_interface import NumberQueue
from dineable import PeopleDinner, RobotDinner
from refuelable import ElectricStation, GasStation
from services.car_station import CarStation
from car import Car
from services.semaphore import Semaphore
from services.scheduler import Scheduler

def main():
    input_dir = "queue"  

    dining_service_people = PeopleDinner()
    dining_service_robots = RobotDinner()
    refueling_service_electric = ElectricStation()
    refueling_service_gas = GasStation()
    electric_queue = NumberQueue()
    gas_queue = NumberQueue()

    electric_station = CarStation(
        dining_service_people,
        refueling_service_electric,
        electric_queue
    )
    gas_station = CarStation(
        dining_service_robots,
        refueling_service_gas,
        gas_queue
    )

    semaphore = Semaphore(electric_station, gas_station)

    scheduler = Scheduler(semaphore, input_dir, read_interval=4)

    try:
        scheduler.start()
    except KeyboardInterrupt:
        print("Shutting down...")
        scheduler.stop()

    print(f"Total people served: {dining_service_people.people_served}")
    print(f"Total robots served: {dining_service_robots.robots_served}")
    print(f"Total electric cars refueled: {refueling_service_electric.electric_cars_served}")
    print(f"Total gas cars refueled: {refueling_service_gas.gas_cars_served}")
    print(f"Total electric consumption: {electric_station.total_electric_consumption}")
    print(f"Total gas consumption: {gas_station.total_gas_consumption}")

if __name__ == "__main__":
    main()