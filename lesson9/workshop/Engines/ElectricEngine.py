from lesson9.workshop.Engines.Engine import Engine


class ElectricEngine(Engine):
    def __init__(self, power, battery_capacity):
        super().__init__(power)
        self.battery_capacity = battery_capacity

    def start(self):
        print(
            f"Electric engine started, "
            f"power: {self.power} HP, "
            f"battery: {self.battery_capacity} kWh"
        )
