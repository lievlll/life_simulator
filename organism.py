class Organism:
    def __init__(self, name: str, energy: float):
        self.name = name
        self.energy = energy

    def is_alive(self) -> bool:
        return self.energy > 0
    def lose_energy(self, amount: float):
        self.energy -= amount

    def __repr__(self):
        return f"{self.name}(энергия={self.energy:.1f})"

class Rabbit(Organism):
    def __init__(self):
        super().__init__("Заяц", energy=20.0)

    def eat_grass(self):
        self.energy += 5.0

class Fox(Organism):
    def __init__(self):
        super().__init__("Лиса", energy=30.0)

    def hunt(self, rabbit: Rabbit) -> bool:
        import random
        if random.random() < 0.5:
            self.energy += 15.0
            rabbit.energy = 0
            return True
        return False

#upd: сделать размножение организмов
