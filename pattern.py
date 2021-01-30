from math import floor, sqrt

from matrix import identity_matrix, inverse
from tuple import color


def set_pattern_transform(pattern, transform):
    pattern.transform = transform
    return


def world_to_object(shape, point):
    if shape.parent is not None:
        point = world_to_object(shape.parent, point)
    return inverse(shape.transform) * point

def pattern_at_shape(p, obj, world_point):
    object_point = world_to_object(obj, world_point)
    pattern_point = inverse(p.transform) * object_point
    return p.pattern_at(p, pattern_point)


class pattern:
    def __init__(self):
        self.transform = identity_matrix()

    def __eq__(self, other):
        return (
            self.a == other.a
            and self.b == other.b
            and self.transform == other.transform
        )


class stripe_pattern(pattern):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def pattern_at(self, pattern, point):
        if floor(point.x) % 2 == 0:
            return pattern.a
        else:
            return pattern.b


class gradient_pattern(pattern):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def pattern_at(self, pattern, point):
        distance = pattern.b - pattern.a
        fraction = point.x - floor(point.x)

        return pattern.a + distance * fraction


class ring_pattern(pattern):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def pattern_at(self, pattern, point):
        if floor(sqrt(point.x ** 2 + point.z ** 2)) % 2 == 0:
            return self.a
        else:
            return self.b


class checkers_pattern(pattern):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    def pattern_at(self, pattern, point):
        if (floor(point.x) + floor(point.y) + floor(point.z)) % 2 == 0:
            return self.a
        else:
            return self.b


class test_pattern(pattern):
    def __init__(self):
        super().__init__()

    def pattern_at(self, pattern, point):
        return color(point.x, point.y, point.z)
