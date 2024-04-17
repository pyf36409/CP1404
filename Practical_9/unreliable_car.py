from Practical_6.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name=0, fuel=0)
        self.reliability = reliability
        self.name = name
        self.fuel = fuel

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            self.drive(distance)
        else:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
            return distance
