from lesson9.workshop.Vehicles.Car import Car


class ElectricCar(Car):
    def drive(self):
        self.engine.start()
        self._speed = 150
        print(
            f"Electric car {self.brand} is driving quietly "
            f"at {self._speed} km/h"
        )