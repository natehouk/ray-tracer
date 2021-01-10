import random
from math import sqrt
from tuple import point, dot

def intersect(sphere, ray):
    sphere_to_ray = ray.origin - point(0, 0, 0)
    
    a = dot(ray.direction, ray.direction)
    b = 2 * dot(ray.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) -1

    descriminant = b ** 2 - 4 * a * c

    if descriminant < 0:
        t = []
        return t
    
    t1 = (-b - sqrt(descriminant)) / (2 * a)
    t2 = (-b + sqrt(descriminant)) / (2 * a)
    t = [t1, t2]
    t = sorted(t)

    return t

class sphere:

    def __init__(self):
        self.id = str.format("%032x" % random.getrandbits(128))


class intersection:

    def __init__(self, t, o):
        self.t = t
        self.object = o


if __name__ == "__main__":
    s = sphere()