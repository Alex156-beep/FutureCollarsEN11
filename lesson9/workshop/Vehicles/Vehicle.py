from abc import ABC, abstractmethod


class Vehicle(ABC):  # Abstract Base Class
    def __init__(self, brand, weight, engine):
        self.brand = brand
        self.weight = weight
        self.engine = engine
        self._speed = 0

    @abstractmethod  # Mandatory to override in subclasses
    def drive(self):
        pass

    def stop(self):
        self._speed = 0
        print(f"{self.brand} has stopped")