import random
from organism import Organism, Rabbit, Fox
class Population:
    def __init__(self, species_class):
        self.members: list = []
        self.species_class = species_class

    def add(self, count: int):
        for _ in range(count):
            self.members.append(self.species_class())

    def alive(self) -> list:
        return [m for m in self.members if m.is_alive()]

    def count(self) -> int:
        return len(self.alive())

class Ecosystem:
    def __init__(self):
        self.rabbits = Population(Rabbit)
        self.foxes = Population(Fox)
        self.day = 0

    def setup(self, rabbit_count: int, fox_count: int):
        self.rabbits.add(rabbit_count)
        self.foxes.add(fox_count)

    def simulate_day(self):
        self.day += 1
        for rabbit in self.rabbits.alive():
            rabbit.eat_grass()
            rabbit.lose_energy(3.0)

        for fox in self.foxes.alive():
            fox.lose_energy(5.0)
            alive_rabbits = self.rabbits.alive()
            if alive_rabbits:
                target = random.choice(alive_rabbits)
                fox.hunt(target)
        if self.rabbits.count() < 3:
            self.rabbits.add(2)

    def is_over(self) -> bool:
        return self.rabbits.count() == 0 or self.foxes.count() == 0
#todo размножение
