from math import sqrt

from shape import intersection, shape
from tuple import vector
from util import EPSILON


class cylinder(shape):
    def __init__(self):
        super().__init__()

    def local_intersect(self, cylinder, ray):
        a = ray.direction.x ** 2 + ray.direction.z ** 2

        if abs(a) < EPSILON:
            return []

        b = 2 * ray.origin.x * ray.direction.x + 2 * ray.origin.z * ray.direction.z
        c = ray.origin.x ** 2 + ray.origin.z ** 2 - 1

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return []

        t0 = (-b - sqrt(discriminant)) / (2 * a)
        t1 = (-b + sqrt(discriminant)) / (2 * a)
        t = [t0, t1]
        t = sorted(t)
        assert t[0] <= t[1]

        return [intersection(t[0], cylinder), intersection(t[1], cylinder)]

    def local_normal_at(self, cylinder, point):
        return vector(point.x, 0, point.z)
