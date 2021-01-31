import time
from math import sqrt

from canvas import canvas, canvas_to_ppm, write_pixel
from matrix import inverse, transpose
from ray import ray
from shape import hit, intersect, intersection, shape
from tuple import color, dot, normalize, point


def glass_sphere():
    s = sphere()
    s.material.transparency = 1.0
    s.material.refractive_index = 1.5
    return s


class sphere(shape):
    def __init__(self):
        super().__init__()

    def local_intersect(self, s, local_ray):

        sphere_to_ray = local_ray.origin - point(0, 0, 0)

        a = dot(local_ray.direction, local_ray.direction)
        b = 2 * dot(local_ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1

        discriminant = (b ** 2) - (4 * a * c)

        if discriminant < 0:
            t = []
            return t

        t0 = (-b - sqrt(discriminant)) / (2 * a)
        t1 = (-b + sqrt(discriminant)) / (2 * a)
        t = [t0, t1]
        t = sorted(t)
        assert t[0] <= t[1]

        return [intersection(t[0], s), intersection(t[1], s)]

    def local_normal_at(self, sphere, world_point):
        return normalize(world_point - point(0, 0, 0))
