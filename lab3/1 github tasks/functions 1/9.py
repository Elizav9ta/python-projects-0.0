
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
print(f"Volume of the sphere: {sphere_volume(radius)}")
