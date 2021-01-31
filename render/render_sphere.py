import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import time

from canvas import canvas, canvas_to_ppm, write_pixel
from material import material
from ray import position, ray
from shape import hit, normal_at
from sphere import intersect, sphere
from tuple import color, normalize, point, point_light
from world import lighting

if __name__ == "__main__":
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = canvas(canvas_pixels, canvas_pixels)
    shape = sphere()
    shape.material = material()
    shape.material.color = color(0.2, 1, 1)

    light_position = point(-10, 10, -10)
    light_color = color(1, 1, 1)
    light = point_light(light_position, light_color)

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
            pos = point(world_x, world_y, wall_z)

            r = ray(ray_origin, normalize(pos - ray_origin))
            xs = intersect(shape, r)

            if hit(xs) is not None:
                pnt = position(r, xs[0].t)
                normal = normal_at(xs[0].object, pnt)
                eye = -r.direction
                color = lighting(xs[0].object.material, light, pnt, eye, normal)
                write_pixel(canvas, x, y, color)

    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(canvas).write_file("images/sphere.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")
