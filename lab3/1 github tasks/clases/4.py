"""Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Method to display the coordinates of the point
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    # Method to move the point to new coordinates
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    # Method to calculate the distance between two points
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Example usage
point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()  # Displays: Point(1, 2)
point2.show()  # Displays: Point(4, 6)

# Moving point1 to new coordinates
point1.move(3, 3)
point1.show()  # Displays: Point(3, 3)

# Calculating the distance between point1 and point2
distance = point1.dist(point2)
print(f"Distance between points: {distance}")
