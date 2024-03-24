NOW = 2024


class Guitar:
    def __init__(self, name=0, year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}), worth ${self.cost}"

    def get_age(self):
        age = NOW - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return "(vintage)"
        else:
            return ""

    def __lt__(self, other):
        return self.year < other.year
