from abc import ABC, abstractmethod

class Refuelable(ABC):
    @abstractmethod
    def refuel(self, carId: str) -> None:
        pass


class ElectricStation(Refuelable):
    def __init__(self):
        self.electric_cars_served = 0

    def refuel(self, carId: str) -> None:
        self.electric_cars_served += 1
        print(f"Refueling electric car {carId}.")


class GasStation(Refuelable):
    def __init__(self):
        self.gas_cars_served = 0

    def refuel(self, carId: str) -> None:
        self.gas_cars_served += 1
        print(f"Refueling gas car {carId}.")