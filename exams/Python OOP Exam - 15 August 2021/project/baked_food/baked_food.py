from abc import ABC


class BakedFood(ABC):

    def __init__(self, name: str, portion: float, price: float):
        self.name: str = name
        self.portion: float = portion
        self.price: float = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not value > 0:
            raise ValueError("Price cannot be less than or equal to zero!")

        self.__price = 0

    def __repr__(self):
        return f" - {type(self).__name__}: {self.portion}g - {self.price}lv"

