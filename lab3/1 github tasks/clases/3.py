"""Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area."""


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    # method that takes length and width as arguments.
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):# method computes the area of the rectangle
        return self.length * self.width

# Usage
rectangle = Rectangle(4, 6)
print(f"Area of rectangle: {rectangle.area()}")
