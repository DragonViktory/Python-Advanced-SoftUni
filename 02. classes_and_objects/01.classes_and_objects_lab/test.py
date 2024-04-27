# class Car:
#
#     def __init__(self, engine):
#         self.engine = engine

# class MyClass:
#     def say_hello(self):
#         return 'Hello'
# x = MyClass()
# x.say_hello() # conventional way
# MyClass.say_hello(x) # equivalent to

# class Dog:
#     def __init__(self, name):
#
#         self.name = name
#
#
# x = Dog("Max")
# print(x.__dict__)

# class Dog:
#
#
#     def __init__(self, name):
#         self.name = name
#
#
#     def change_name(self, new_name):
#         self.name = new_name
#
# x = Dog("Max")
# x.change_name("Rex")
# print(x.name)  # Rex


# class MyClass:
#     def __str__(self):
#         return 'This is My Class'
#
# my_instance = MyClass()
# print(str(my_instance)) # This is My Class
# print(my_instance.__str__()) # This is My Class
# print(my_instance) # This is My Class

# class MyClass:
#     def __repr__(self):
#         return 'This is My Class'
#
# my_instance = MyClass()
# print(repr(my_instance))
# print(my_instance.__repr__())
# print(my_instance) # This is My Class
# # use print() only when __repr__() returns string

# class Laptop:
#     brand = "Dell" # class variable
#
#     def __init__(self, name):
#         self.name = name # instance variable
#
# first_laptop = Laptop("Latitude 5300")
# second_laptop = Laptop("Inspiron 15")
# print(first_laptop.brand == second_laptop.brand) # True
# print(first_laptop.name == second_laptop.name) # False

# class Laptop:
#     def __init__(self, model):
#         self.model = model
#
# my_laptop = Laptop("Swift")
# my_laptop.ram = 8
# Laptop.brand = "Dell"
# del my_laptop.model

# class Dog:
#     tricks = [] # mistaken use of a class variable
#     def __init__(self, name):
#         self.name = name
#
# poodle = Dog("Bella")
# beagle = Dog("Max")
# poodle.tricks.append('roll over')
# print(beagle.tricks) # shared by all dogs ['roll over']

# Example: Good Practice

# class Dog:
#     kind = 'canine' # class variable shared by all instances
#     def __init__(self, name):
#         self.name = name
#         self.tricks = [] # creates empty list for each dog
#
# poodle = Dog("Bella")
# beagle = Dog("Max")
# print(poodle.name, poodle.kind) # Bella canine
# print(beagle.name, beagle.kind) # Max canine
# poodle.tricks.append('roll over')
# beagle.tricks.append('play dead')
# print(poodle.tricks) # ['roll over']
# print(beagle.tricks) # ['play dead']

# class MyClass:
#     """This is MyClass."""
#     def example(self):
#         """This is the example module of MyClass."""
#
# print(MyClass.__doc__) # This is MyClass.
# print(MyClass.example.__doc__)
# # This is the example module of MyClass.

# class MyClass:
#     class_variable = 1
#
#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable
#
#
# first = MyClass(2)
# second = MyClass(3)
# print(MyClass.__dict__)  # {'__module__': '__main__', ... }
# print(first.__dict__)  # { 'instance_variable': 2 }
# print(second.__dict__)  # { 'instance_variable': 3 }
