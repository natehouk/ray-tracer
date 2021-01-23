import random
import time
from copy import deepcopy
from math import pi, sqrt

from canvas import canvas, canvas_to_ppm, write_pixel
from material import material
from matrix import identity_matrix, inverse, rotation_z, scaling, shearing, transpose
from ray import position, ray, transform
from shape import intersect, normal_at, shape
from tuple import EPSILON, color, dot, normalize, point, reflect


def hit(intersections):
    min = float("inf")
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


def prepare_computations(intersection, ray, xs=None):
    c = comps()
    c.t = intersection.t
    c.object = intersection.object
    c.point = position(ray, c.t)
    c.eyev = -ray.direction
    c.normalv = normal_at(c.object, c.point)
    if dot(c.normalv, c.eyev) < 0:
        c.inside = True
        c.normalv = -c.normalv
    else:
        c.inside = False
    c.over_point = c.point + c.normalv * EPSILON
    c.under_point = c.point - c.normalv * EPSILON
    c.reflectv = reflect(ray.direction, c.normalv)
    containers = []
    if xs:
        for i in xs:
            if i == intersection:
                if len(containers) == 0:
                    c.n1 = 1.0
                else:
                    c.n1 = containers[-1].material.refractive_index
            if i.object in containers:
                containers.remove(i.object)
            else:
                containers.append(i.object)
            if i == intersection:
                if len(containers) == 0:
                    c.n2 = 1.0
                else:
                    c.n2 = containers[-1].material.refractive_index
                break
    return c


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

        descriminant = (b ** 2) - (4 * a * c)

        if descriminant < 0:
            t = []
            return t

        t1 = (-b - sqrt(descriminant)) / (2 * a)
        t2 = (-b + sqrt(descriminant)) / (2 * a)
        t = [t1, t2]
        t = sorted(t)

        print(str(t[0]) + " " + str(t[1]))
        assert t[0] <= t[1]

        return [intersection(t[0], s), intersection(t[1], s)]

    def local_normal_at(self, sphere, world_point):
        object_point = inverse(sphere.transform) * world_point
        object_normal = object_point - point(0, 0, 0)
        world_normal = transpose(inverse(sphere.transform)) * object_normal
        world_normal.w = 0
        return normalize(world_normal)


class intersection:
    def __init__(self, t, o):
        self.t = t
        self.object = o


class comps:
    def __init__(self):
        self.t = None
        self.object = None
        self.point = None
        self.eyev = None
        self.normalv = None
        self.inside = None

    def __str__(self):
        return (
            "<"
            + str(self.t)
            + ", "
            + str(self.object)
            + ", "
            + str(self.point)
            + ", "
            + str(self.eyev)
            + ", "
            + str(self.normalv)
            + ", "
            + str(self.inside)
            + ">"
        )


if __name__ == "__main__":
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = canvas(canvas_pixels, canvas_pixels)
    color = color(1, 0, 0)
    shape = sphere()

    # transformations
    # shape.transform = scaling(1, 0.5, 1)
    # shape.transform = scaling(0.5, 1, 1)
    # shape.transform = rotation_z(pi / 4) * scaling(0.5, 1, 1)
    # shape.transform = shearing(1, 0, 0, 0, 0, 0) * scaling(0.5, 1, 1)

    start = time.time()
    print("Starting render...")

    for y in range(canvas_pixels):

        world_y = half - pixel_size * y

        for x in range(canvas_pixels):

            world_x = -half + pixel_size * x
            position = point(world_x, world_y, wall_z)

            r = ray(ray_origin, normalize(position - ray_origin))
            xs = intersect(shape, r)

            if hit(xs) is not None:
                write_pixel(canvas, x, y, color)

    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(canvas).write_file("images/circle.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")
