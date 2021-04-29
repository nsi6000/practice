
from math import pi

class Shape:
    def __init__(self, color = 'red'):
        self.color = color

    def __str__(self):
        return 'Shape(color={})'.format(self.color)

    def __repr__(self):
        return self.__str__()

class Circle(Shape):
    def __init__(self, radius = 1.0, color = 'red'):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return 'Circle({}, radius = {})'.format(super().__str__(), self.radius)

    def __repr__(self):
        return self.__str__()

    def get_area(self):
        return self.radius * self.radius * pi

class Rectangle(Shape):
    def __init__(self, length = 1.0,  width = 1.0, color = 'red'):
        super().__init__(color)
        self.length = length
        self.width = width

    def __str__(self):
        return 'Rectangle({}, length={}, width={})'.format(super().__str__(), self.length, self.width)

    def __repr__(self):
        return self.__str__()

    def get_area(self):
        return self.length * self.width

if __name__ == '__main__':
    s1 = Shape('orange')
    print(s1)
    print(s1.color)
    print(str(s1))
    print(repr(s1))
    print("")

    c1 = Circle(1.2, 'yellow')
    print(c1)
    print(c1.get_area())
    print(c1.color)
    print(c1.radius)
    print(str(c1))
    print(repr(c1))
    print("")

    r1 = Rectangle(1.2, 3.4, 'blue')
    print(r1)
    print(r1.get_area())
    print(r1.color)
    print(r1.length)
    print(r1.width)
    print(str(r1))
    print(repr(r1))

