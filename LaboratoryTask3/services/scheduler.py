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
    def __init__(self, semaphore, input_dir, read_interval=2, serve_interval=3):
        self.semaphore = semaphore
        self.input_dir = input_dir
        self.read_interval = read_interval
        self.serve_interval = serve_interval
        self.lock = Lock()
        self.running = True

    def read_files(self):
        while self.running:
            files = os.listdir(self.input_dir)
            for file_name in files:
                file_path = os.path.join(self.input_dir, file_name)
                try:
                    with open(file_path, "r") as f:
                        car_data = json.load(f)
                        car = Car.from_dict(car_data)
                        with self.lock:
                            self.semaphore.guide_car(car)
                    os.remove(file_path)  # Remove file after processing
                except Exception as e:
                    print(f"Error processing file {file_name}: {e}")
            time.sleep(self.read_interval)

    def serve_cars(self):
        while self.running:
            with self.lock:
                self.semaphore.serve_all()
            time.sleep(self.serve_interval)

    def start(self):
        self.running = True
        self.reader_thread = Thread(target=self.read_files)
        self.server_thread = Thread(target=self.serve_cars)
        self.reader_thread.start()
        self.server_thread.start()

    def stop(self):
        self.running = False
        self.reader_thread.join()
        self.server_thread.join()