from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class Controller:
    DECORATION_TYPES = {"Ornament": Ornament, "Plant": Plant}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in BaseAquarium.FISH_TYPES:
            return "Invalid aquarium type."
        new_aquarium = BaseAquarium.FISH_TYPES[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.DECORATION_TYPES:
            return f"Invalid decoration type."
        new_decoration = self.DECORATION_TYPES[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_obj_name(aquarium_name, self.aquariums)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."
        self.decorations_repository.remove(decoration)
        aquarium.decorations.append(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.find_obj_name(aquarium_name, self.aquariums)
        if fish_type not in BaseAquarium.FISH_TYPES:
            return f"There isn't a fish of type {fish_type}."
        new_fish = BaseAquarium.FISH_TYPES[fish_type](fish_name, fish_species, price)
        if new_fish.AQUARIUM != type(aquarium).__name__:
            return "Water not suitable."
        return aquarium.add_fish(new_fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_obj_name(aquarium_name, self.aquariums)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_obj_name(aquarium_name, self.aquariums)
        total_value_fish = sum([fish.price for fish in aquarium.fish])
        total_value_decoration = sum([decoration.price for decoration in aquarium.decorations])
        total_total = total_value_fish + total_value_decoration
        return f"The value of Aquarium {aquarium_name} is {total_total:.2f}."

    def report(self):
        return "\n".join([str(aquarium) for aquarium in self.aquariums])

    @staticmethod
    def find_obj_name(name, object_list):
        for obj in object_list:
            if obj.name == name:
                return obj
