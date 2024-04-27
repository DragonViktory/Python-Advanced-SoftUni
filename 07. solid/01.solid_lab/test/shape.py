class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        return "Drawing rectangle"


class Circle(Shape):

    def draw(self):
        return "Drawing circle"


for s in [Rectangle(), Circle()]:
    print(s.draw())
