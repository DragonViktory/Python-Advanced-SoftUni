from abc import ABC

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    def __init__(self, table_number: int, capacity: int):
        self.table_number: int = table_number
        self.capacity: int = capacity
        self.food_orders: list = []
        self.drink_orders: list = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if not value > 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int):
        pass

    def order_food(self, baked_food: BakedFood):
        pass

    def order_drink(self, drink: Drink):
        pass

    def get_bill(self):
        pass

    def clear(self):
        pass

    def free_table_info(self):
        return f"""Table: {self.table_number}
                Type: {type(self).__name__}
                Capacity: {self.capacity}"""
