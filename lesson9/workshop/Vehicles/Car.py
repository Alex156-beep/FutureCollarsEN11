from lesson9.workshop.Vehicles.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, weight, engine, number_of_doors):
        super().__init__(brand, weight, engine)
        self.number_of_doors = number_of_doors

    def drive(self):
        self.engine.start()
        self._speed = 160
        print(
            f"Car {self.brand} is driving "
            f"at {self._speed} km/h"
        )

