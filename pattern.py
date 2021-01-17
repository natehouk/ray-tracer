from math import floor
from matrix import inverse, identity_matrix


def stripe_pattern(a, b):
    return pattern(a, b)

def set_pattern_transform(pattern, transform):
    pattern.transform = transform
    return

def stripe_at(pattern, point):
    if floor(point.x) % 2 == 0:
        return pattern.a
    else:
        return pattern.b

def stripe_at_object(p, obj, world_point):
    object_point = inverse(obj.transform) * world_point
    pattern_point = inverse(p.transform) * object_point

    return stripe_at(p, pattern_point)

class pattern:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.transform = identity_matrix()

    def __eq__(self, other):
        return (self.a == other.a and
                self.b == other.b and
                self.transform == other.transform)