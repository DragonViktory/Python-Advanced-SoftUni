from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TYPE_HORSE = "Thoroughbred"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.max_speed = self.MAX_SPEED

    def train(self):
        self.speed = self.max_speed + 3 if self.max_speed + 3 <= self.max_speed else self.max_speed