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
        object_point = inverse(sphere.transform) * world_point
        object_normal = object_point - point(0, 0, 0)
        world_normal = transpose(inverse(sphere.transform)) * object_normal
        world_normal.w = 0
        return normalize(world_normal)


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
