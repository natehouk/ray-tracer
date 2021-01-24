from math import sqrt

from shape import intersection, shape
from tuple import vector
from util import EPSILON


class cylinder(shape):
    def __init__(self):
        super().__init__()
        self.minimum = -float("inf")
        self.maximum = float("inf")
        self.closed = False

    def local_intersect(self, cylinder, ray):
        a = ray.direction.x ** 2 + ray.direction.z ** 2

        xs = []
        if abs(a) > EPSILON:
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

            y0 = ray.origin.y + t0 * ray.direction.y
            if cylinder.minimum < y0 and y0 < cylinder.maximum:
                xs.append(intersection(t0, cylinder))

            y1 = ray.origin.y + t1 * ray.direction.y
            if cylinder.minimum < y1 and y1 < cylinder.maximum:
                xs.append(intersection(t1, cylinder))

        xs = self.intersect_caps(cylinder, ray, xs)

        return xs

    def local_normal_at(self, cylinder, point):
        dist = point.x ** 2 + point.z ** 2

        if dist < 1 and point.y >= cylinder.maximum - EPSILON:
            return vector(0, 1, 0)
        elif dist < 1 and point.y <= cylinder.minimum + EPSILON:
            return vector(0, -1, 0)
        else:
            return vector(point.x, 0, point.z)

    def check_cap(self, ray, t):
        x = ray.origin.x + t * ray.direction.x
        z = ray.origin.z + t * ray.direction.z

        return x ** 2 + z ** 2 <= 1

    def intersect_caps(self, cylinder, ray, xs):
        if cylinder.closed is not True or abs(ray.direction.y) < EPSILON:
            return xs

        t = (cylinder.minimum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t):
            xs.append(intersection(t, cylinder))

        t = (cylinder.maximum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t):
            xs.append(intersection(t, cylinder))

        return xs
