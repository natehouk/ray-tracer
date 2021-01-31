import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
import time

from canvas import canvas, canvas_to_ppm, write_pixel
from matrix import normalize
from ray import ray
from shape import hit, intersect
from sphere import sphere
from tuple import color, point

if __name__ == "__main__":
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    canvas_pixels = 400
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
