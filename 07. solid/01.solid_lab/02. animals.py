class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        return "Making sound "


class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + "meow"


class Turtle(Animal):
    def make_sound(self):
        return super().make_sound() + "T sound"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog('Sharo'), Cat('Lady'), Turtle('Nemo')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
