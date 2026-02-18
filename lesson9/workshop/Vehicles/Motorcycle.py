from lesson9.workshop.Vehicles.Vehicle import Vehicle


class Motorcycle(Vehicle):
    def drive(self):
        self.engine.start()
        self._speed = 250
        print(
            f"Motorcycle {self.brand} is riding"
            f"at {self._speed} km/h"
        )