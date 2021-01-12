import random
from math import sqrt
from tuple import point, dot
from matrix import identity_matrix, inverse
from ray import transform

def hit(intersections):
    min = float('inf')
    h = None
    for i in intersections:
        if i.t >= 0 and i.t <= min:
            min = i.t
            h = i
    return h

def intersections(*argv):
    i = []
    for arg in argv:
        i.append(arg)
    i = sorted(i, key=lambda x: x.t)
    return i

def intersect(sphere, ray):
    ray = transform(ray, inverse(sphere.transform))

    sphere_to_ray = ray.origin - point(0, 0, 0)
    
    a = dot(ray.direction, ray.direction)
    b = 2 * dot(ray.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) - 1

    descriminant = (b ** 2) - (4 * a * c)

    if descriminant < 0:
        t = []
        return t
    
    t1 = (-b - sqrt(descriminant)) / (2 * a)
    t2 = (-b + sqrt(descriminant)) / (2 * a)
    t = [t1, t2]
    t = sorted(t)
    assert t[0] <= t[1]

    return [intersection(t[0], sphere), intersection(t[1], sphere)]

def set_transform(sphere, transform):
    sphere.transform = transform
    return

class sphere:

    def __init__(self):
        self.id = str.format("%032x" % random.getrandbits(128))
        self.transform = identity_matrix()


class intersection:

    def __init__(self, t, o):
        self.t = t
        self.object = o


if __name__ == "__main__":
    s = sphere()