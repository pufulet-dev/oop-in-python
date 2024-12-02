class Car:
    def __init__(self, car_id: int, car_type: str, passengers: str, is_dining: bool, consumption: int):
        self.car_id = car_id
        self.car_type = car_type 
        self.passengers = passengers  
        self.is_dining = is_dining
        self.consumption = consumption

    @staticmethod
    def from_dict(data: dict) -> "Car":
        return Car(
            car_id=data["id"],
            car_type=data["type"],
            passengers=data["passengers"],
            is_dining=data["isDining"],
            consumption=data["consumption"],
        )