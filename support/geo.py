from math import sqrt

# Pythagorean theorem for finding the distance between two points

def pytha_the(length, height):
    """The pythagorean theorem"""
    a = length ** 2
    b = height ** 2

    return sqrt(a + b)


def cir_test(circle_center_x,
             circle_center_y,
             test_point_x,
             test_point_y,
             circle_radius):
    """Returns false if the point is outside the circle. True if inside"""
    # Calculate horizontal distance
    hor = abs(circle_center_x - test_point_x)

    # Calculate vertical distance
    vert = abs(circle_center_y - test_point_y)

    # Calculate distance between two points
    distance = pytha_the(hor, vert)

    # If the distance variable is greater than the radius of the circle, it cant be inside it
    if distance > circle_radius:
        return False
    else:
        return True

