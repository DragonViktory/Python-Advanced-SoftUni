from abc import ABC
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    FISH_TYPES = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if type(fish).__name__ in self.FISH_TYPES and len(self.fish) < self.capacity:
            self.fish.append(fish)
            return f"Successfully added {type(fish).__name__} to {self.name}."
        return "Not enough capacity."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        name_fishes = " ".join([fish.name for fish in self.fish]) if self.fish else "none"
        return (f"{self.name}:Fish: {name_fishes}\n"
                f"Decorations: {len(self.decorations)}\n"
                f"Comfort: {self.calculate_comfort()}")
