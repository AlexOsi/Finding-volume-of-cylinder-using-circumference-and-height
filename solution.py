# Finding volume of cylinder using circumference and height
def volume_circumference_height(circumference, height):
    pi = 3.14
    radius = circumference / (2 * pi)
    volume = pi * radius ** 2 * height
    return volume
