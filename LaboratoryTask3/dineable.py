from abc import ABC, abstractmethod

class Dineable(ABC):
    @abstractmethod
    def serveDinner(self, carId: str) -> None:
        pass


class PeopleDinner(Dineable):
    def __init__(self):
        self.people_served = 0

    def serveDinner(self, carId: str) -> None:
        self.people_served += 1
        print(f"Serving dinner to people in car {carId}.")


class RobotDinner(Dineable):
    def __init__(self):
        self.robots_served = 0

    def serveDinner(self, carId: str) -> None:
        self.robots_served += 1
        print(f"Serving dinner to robots in car {carId}.")