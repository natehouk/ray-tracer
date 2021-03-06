import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import time
from math import pi

from camera import camera, render
from canvas import canvas_to_ppm
from cone import cone
from cube import cube
from material import material
from matrix import rotation_x, rotation_y, scaling, translation, view_transform
from pattern import checkers_pattern, gradient_pattern, ring_pattern, stripe_pattern
from plane import plane
from sphere import sphere
from tuple import color, point, point_light, vector
from world import world

if __name__ == "__main__":
    start = time.time()
    print("Starting render...")

    w = world()
    w.light = point_light(point(-10, 10, -10), color(1, 1, 1))

    black = color(0, 0, 0)
    white = color(1, 1, 1)

    floor = plane()
    floor.transform = scaling(0.75, 0.75, 0.75)
    floor.material.color = color(0.9, 0.9, 0.9)
    floor.material.specular = 0.1
    floor.material.pattern = checkers_pattern(color(1, 0.8, 0.1), color(0.1, 0.1, 0.85))
    floor.material.reflective = 0.1
    w.objects.append(floor)

    left_wall = plane()
    left_wall.transform = (
        translation(0, 0, 5)
        * rotation_y(-pi / 4)
        * rotation_x(pi / 2)
        * scaling(0.25, 0.25, 0.25)
    )
    left_wall.material.specular = 0.1
    left_wall.material.pattern = stripe_pattern(black, white)
    w.objects.append(left_wall)

    right_wall = plane()
    right_wall.transform = (
        translation(0, 0, 5)
        * rotation_y(pi / 4)
        * rotation_x(pi / 2)
        * scaling(0.25, 0.25, 0.25)
    )
    right_wall.material.specular = 0.1
    right_wall.material.pattern = stripe_pattern(black, white)
    w.objects.append(right_wall)

    middle = sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    middle.material = material()
    middle.material.color = color(0.1, 0.1, 0.85)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    middle.material.reflective = 0.8
    middle.material.transparency = 0
    # middle.material.pattern = checkers_pattern(
    #     color(0.2, 0.5, 0.7), color(0.8, 0.8, 0.2)
    # )
    w.objects.append(middle)

    right = cone()
    right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
    right.material = material()
    right.material.color = color(0.1, 0.1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    right.material.reflective = 0.7
    middle.material.transparency = 0
    right.material.pattern = ring_pattern(color(0.2, 0.5, 0.7), color(0.8, 0.8, 0.2))
    w.objects.append(right)

    left = cube()
    left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
    left.material = material()
    left.material.color = color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    left.material.reflective = 0.6
    left.material.transparency = 0
    left.material.pattern = gradient_pattern(color(0.7, 0.5, 0.7), color(0, 0.8, 0.2))
    w.objects.append(left)

    cam = camera(1600, 800, pi / 2)
    cam.transform = view_transform(point(0, 1.5, -5), point(0, 1, 0), vector(0, 1, 0))

    canvas = render(cam, w)

    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(canvas).write_file("images/cones.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")
