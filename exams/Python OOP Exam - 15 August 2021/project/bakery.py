class Bakery:

    def __init__(self, name: str):
        self.name: str = name
        self.food_menu: list = []
        self.drinks_meny: list = []
        self.tables_repository: list = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        pass

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        pass

    def add_table(self, table_type: str, table_number: int, capacity: int):
        pass

    def reserve_table(self, number_of_people: int):
        pass

    def order_food(self, table_number: int, *drink_names):
        pass

    def leave_table(self, table_number: int):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass

