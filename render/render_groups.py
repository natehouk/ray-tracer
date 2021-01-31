import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
import time
from math import pi

from camera import camera, render
from canvas import canvas_to_ppm
from hexagon import hexagon
from matrix import view_transform
from tuple import color, point, point_light, vector
from world import world

if __name__ == "__main__":
    start = time.time()
    print("Starting render...")

    w = world()
    w.light = point_light(point(-10, 10, -10), color(1, 1, 1))

    hex = hexagon()
    w.objects.append(hex)

    cam = camera(1600, 800, pi / 2)
    cam.transform = view_transform(point(0, 1.5, -5), point(0, 1, 0), vector(0, 1, 0))

    canvas = render(cam, w)

    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(canvas).write_file("images/groups.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")
