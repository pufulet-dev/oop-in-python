import os
import sys
import json
import time
from threading import Thread, Lock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from queue_interface import NumberQueue
from dineable import PeopleDinner, RobotDinner
from refuelable import ElectricStation, GasStation
from services.semaphore import Semaphore
from services.car_station import CarStation
from car import Car

class Scheduler:
    def __init__(self, semaphore, input_dir, read_interval=4):
        self.semaphore = semaphore
        self.input_dir = input_dir
        self.read_interval = read_interval
        self.lock = Lock()
        self.running = True

    def read_file(self):
        with self.lock:
            files = os.listdir(self.input_dir)
            if files: 
                file_path = os.path.join(self.input_dir, files[0]) 
                try:
                    with open(file_path, "r") as file:
                        car_data = json.load(file)  
                        car = Car.from_dict(car_data) 
                        self.semaphore.guide_car(car) 
                    os.remove(file_path) 
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

    def serve_cars(self):
        with self.lock:
            self.semaphore.serve_all()  
    def start(self):
        while self.running:
            self.read_file()  
            self.serve_cars()  
            time.sleep(self.read_interval)  

    def stop(self):
        self.running = False