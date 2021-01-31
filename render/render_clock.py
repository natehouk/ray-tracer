import os.path
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
import time
from math import pi

from canvas import canvas, canvas_to_ppm, write_pixel
from matrix import rotation_y
from tuple import color, point

if __name__ == "__main__":
    origin = point(0, 0, 0)
    twelve = point(0, 0, 1)
    c = canvas(600, 600)
    red = color(1, 0, 0)

    start = time.time()
    print("Starting render...")

    for i in range(12):
        r = rotation_y(i * pi / 6)
        pixel = r * twelve
        write_pixel(c, 225 * pixel.x + 300, c.height - 225 * pixel.z - 300, red)

    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(c).write_file("images/clock.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")
