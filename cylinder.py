from shape import shape
from sphere import intersection
from tuple import EPSILON

class cylinder(shape):
    def __init__(self):
        super().__init__()

    def local_intersect(self, cylinder, ray):
        a = ray.direction.x ** 2 + ray.direction.z ** 2
        print('ray')
        print(ray.direction.z ** 2)
        if abs(a) < EPSILON:
            return []
        
        b = 2 * ray.origin.x * ray.direction.x + 2 * ray.origin.z * ray.direction.z
        c = ray.origin.x ** 2 + ray.origin.z ** 2 - 1

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return []

        print(abs(a))
        print (discriminant)
        input()

        return [intersection(1, cylinder)]
