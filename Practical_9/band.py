from musician import Musician


class Band:
    def __init__(self, name):
        self.name = name

    def add(self, musician):
        Musician(musician)

    def play(self):
        Musician.play()
