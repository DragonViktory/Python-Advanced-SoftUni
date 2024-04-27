from abc import ABC, abstractmethod


class Chair:

    def __init__(self, name):
        self.name = name


class Sofa:
    def __init__(self, name):
        self.name = name


class Table:
    def __init__(self, name):
        self.name = name


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()


class VictorianFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return Chair("Victorian chair")

    def create_table(self):
        return Table("Victorian table")

    def create_sofa(self):
        return Sofa("Victorian sofa")


class FuturisticFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return Chair("Futuristic chair")

    def create_table(self):
        return Table("Futuristic table")

    def create_sofa(self):
        return Sofa("Futuristic sofa")


class ModernFactory(AbstractFurnitureFactory):
    def create_chair(self):
        return Chair("Modern chair")

    def create_table(self):
        return Table("Modern table")

    def create_sofa(self):
        return Sofa("Modern sofa")


def get_furniture(style):
    if style == "victorian":
        factory = VictorianFactory()
    elif style == "modern":
        factory = ModernFactory()
    else:
        factory = FuturisticFactory()
    return factory.create_sofa(), factory.create_chair(), factory.create_table()


request = input()

print(get_furniture(request))