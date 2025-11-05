from geometry.two_d import circles
# or from ..two_d import circles

def cylinder_volume(radius, length):
    return circles.area(radius) * length

def sphere_volume(radius):
    return circles.area(radius) * radius * 4 / 3