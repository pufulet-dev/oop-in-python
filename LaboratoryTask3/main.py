import os
import json
from queue_interface import NumberQueue
from dineable import PeopleDinner, RobotDinner
from refuelable import ElectricStation, GasStation
from services.car_station import CarStation
from car import Car

def main():
    dining_service = PeopleDinner()
    electric_refueling_service = ElectricStation()
    gas_refueling_service = GasStation()
    car_queue = NumberQueue()

    car_station = CarStation(dining_service, electric_refueling_service, gas_refueling_service, car_queue)

    input_dir = "queue"
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        with open(file_path, "r") as file:
            car_data = json.load(file)
            car = Car.from_dict(car_data)
            car_station.add_car(car)

    car_station.serve_cars()

    print(f"Total people served: {dining_service.people_served}")
    print(f"Total electric cars refueled: {electric_refueling_service.electric_cars_served}")
    print(f"Total gas cars refueled: {gas_refueling_service.gas_cars_served}")
    print(f"Total electric consumption: {car_station.total_electric_consumption}")
    print(f"Total gas consumption: {car_station.total_gas_consumption}")

if __name__ == "__main__":
    main()