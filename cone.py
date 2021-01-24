from math import sqrt

from shape import intersection, shape
from tuple import vector
from util import EPSILON


class cone(shape):
    def __init__(self):
        super().__init__()
        self.minimum = -float("inf")
        self.maximum = float("inf")
        self.closed = False

    def local_intersect(self, cone, ray):
        a = ray.direction.x ** 2 - ray.direction.y ** 2 + ray.direction.z ** 2
        b = 2 * ray.origin.x * ray.direction.x - 2 * ray.origin.y * ray.direction.y + 2 * ray.origin.z * ray.direction.z
        c = ray.origin.x ** 2 - ray.origin.y ** 2 + ray.origin.z ** 2

        if abs(a) < EPSILON and abs(b) < EPSILON:
            return []
        elif abs(a) < EPSILON:
            t = -c / (2 * b)
            return [intersection(t, cone)]
        else:
            xs = []
            discriminant = b ** 2 - 4 * a * c

            if discriminant < 0:
                return []

            t0 = (-b - sqrt(discriminant)) / (2 * a)
            t1 = (-b + sqrt(discriminant)) / (2 * a)
            t = [t0, t1]
            t = sorted(t)
            assert t[0] <= t[1]

            y0 = ray.origin.y + t0 * ray.direction.y
            if cone.minimum < y0 and y0 < cone.maximum:
                xs.append(intersection(t0, cone))

            y1 = ray.origin.y + t1 * ray.direction.y
            if cone.minimum < y1 and y1 < cone.maximum:
                xs.append(intersection(t1, cone))

        #self.intersect_caps(cone, ray, xs)

        return xs

    def local_normal_at(self, cone, point):
        dist = point.x ** 2 + point.z ** 2

        if dist < 1 and point.y >= cone.maximum - EPSILON:
            return vector(0, 1, 0)
        elif dist < 1 and point.y <= cone.minimum + EPSILON:
            return vector(0, -1, 0)
        else:
            return vector(point.x, 0, point.z)

    def check_cap(self, ray, t):
        x = ray.origin.x + t * ray.direction.x
        z = ray.origin.z + t * ray.direction.z

        return x ** 2 + z ** 2 <= 1

    def intersect_caps(self, cone, ray, xs):
        if cone.closed is not True or abs(ray.direction.y) < EPSILON:
            return

        t = (cone.minimum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t):
            xs.append(intersection(t, cone))

        t = (cone.maximum - ray.origin.y) / ray.direction.y
        if self.check_cap(ray, t):
            xs.append(intersection(t, cone))
