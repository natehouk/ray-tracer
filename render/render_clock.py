import time
from math import pi
from tuple import point, color
from canvas import canvas, write_pixel, canvas_to_ppm
from matrix import rotation_y



def main():
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

if __name__ == "__main__":
    main()