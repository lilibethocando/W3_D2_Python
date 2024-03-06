import math

def circle_area(radius):
    area = math.pi * radius**2
    return round(area, 2)

def hypotenuse(side1, side2):
    hypotenuse_length = math.sqrt(side1**2 + side2**2)
    return round(hypotenuse_length, 2)
