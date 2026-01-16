# %%
class Vehicle:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        if distance > 0:
            self.mileage += distance

    def get_info(self):
        return f"{self.make} {self.year} {self.model}, mileage {self.mileage} km"

    def __str__(self):
        return self.get_info()

    @classmethod
    def from_string(cls, data_string):
        make, model, year = data_string.split("-")
        return cls(make, model, int(year))


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_capacity, mileage=0):
        super().__init__(make, model, year, mileage)

        self.fuel_capacity = fuel_capacity

    def get_info(self):
        return f"{self.make} {self.model} {self.year} {self.fuel_capacity} L, {self.mileage}Km"


class ElectricScooter(Vehicle):
    def __init__(self, make, model, year, battery_percentage=100, mileage=0):
        super().__init__(make, model, year, mileage)
        self.battery_percentage = battery_percentage

    def drive(self, distance):
        battery_drop = distance/2
        self.battery_percentage = max(
            0, self.battery_percentage - battery_drop)

    def get_info(self):
        return f"{self.make} {self.model} {self.battery_percentage}% {self.mileage} km"


@staticmethod
def is_charging_required(battery_percentage):
    return battery_percentage < 20


vehicles = [
    Car("Toyota", "Corolla", 2020, 50),
    ElectricScooter("Xiaomi", "M365", 2022, 85),
    Vehicle.from_string("Honda-Civic-2018")
]

for v in vehicles:
    v.drive(100)


def print_vehicle_report(vehicles):
    for v in vehicles:
        print(v.get_info())


print_vehicle_report(vehicles)
