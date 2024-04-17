from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.name = name
        self.fuel = fuel
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        return f"{super().__str__()}, {self.price_per_km} plus flagfall of ${self.flagfall}"
