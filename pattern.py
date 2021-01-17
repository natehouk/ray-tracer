from math import floor
from tuple import color
from matrix import inverse, identity_matrix


def set_pattern_transform(pattern, transform):
    pattern.transform = transform
    return

def pattern_at_shape(p, obj, world_point):
    object_point = inverse(obj.transform) * world_point
    pattern_point = inverse(p.transform) * object_point

    return p.pattern_at(p, pattern_point)

class pattern:

    def __init__(self):
        self.transform = identity_matrix()

    def __eq__(self, other):
        return (self.a == other.a and
                self.b == other.b and
                self.transform == other.transform)

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

class test_pattern(pattern):

    def __init__(self):
        super().__init__()

    def pattern_at(self, pattern, point):
        return color(point.x, point.y, point.z)