from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TYPE_HORSE = "Appaloosa"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.max_speed = self.MAX_SPEED

    def train(self):
        self.speed = self.max_speed + 2 if self.max_speed + 2 <= self.max_speed else self.max_speed

