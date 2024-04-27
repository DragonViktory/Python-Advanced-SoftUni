# Place order
# Receive order
# start cooking
# cutting
# boiling


class Cook:

    def slice(self):
        print("slicing")

    def boil(self):
        print("boiling")

    def cut(self):
        print("cutting")


class Waitress:

    def __init__(self, name):
        self.name = name

    def gather_request(self):
        pass

    def place_order(self):
        pass


class Restaurant:
    def __init__(self, name, cook, waitress):
        self.name = name
        self.cook = cook
        self.waitress = waitress

    def execute_order(self):
        self.waitress.place_order()
        self.cook.cut()
        self.cook.slice()
        self.cook.boil()


class Client:
    pass


w = Waitress("Test")
c = Cook()
res = Restourant("KFC", c, w)
res.execute_order()
