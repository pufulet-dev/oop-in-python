from dineable import PeopleDinner, RobotDinner
from refuelable import ElectricStation, GasStation

def main():

    people_dinner = PeopleDinner()
    robot_dinner = RobotDinner()
    electric_station = ElectricStation()
    gas_station = GasStation()

    people_dinner.serveDinner("Car1")
    robot_dinner.serveDinner("Car2")

    electric_station.refuel("Car3")
    gas_station.refuel("Car4")

    print(f"People served: {people_dinner.people_served}")
    print(f"Robots served: {robot_dinner.robots_served}")
    print(f"Electric cars refueled: {electric_station.electric_cars_served}")
    print(f"Gas cars refueled: {gas_station.gas_cars_served}")

if __name__ == "__main__":
    main()