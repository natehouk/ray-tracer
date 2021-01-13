import random
import time
from math import sqrt, pi
from tuple import point, dot, normalize, color
from matrix import identity_matrix, inverse, scaling, rotation_z, shearing
from ray import ray, transform
from canvas import canvas, write_pixel, canvas_to_ppm

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

def normal_at(sphere, p):
    return normalize(p - point(0, 0, 0))

class sphere:

    def __init__(self):
        self.id = str.format("%032x" % random.getrandbits(128))
        self.transform = identity_matrix()


class intersection:

    def __init__(self, t, o):
        self.t = t
        self.object = o


if __name__ == "__main__":
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = canvas(canvas_pixels, canvas_pixels)
    color = color(1, 0 , 0)
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