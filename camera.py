import time
from math import tan

from canvas import canvas, write_pixel
from matrix import identity_matrix, inverse
from ray import ray
from tuple import normalize, point
from world import color_at


class camera:
    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = identity_matrix()

        # calculate pixel size
        half_view = tan(field_of_view / 2)
        aspect = hsize / vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / hsize


def ray_for_pixel(camera, px, py):
    xoffset = (px + 0.5) * camera.pixel_size
    yoffset = (py + 0.5) * camera.pixel_size

    world_x = camera.half_width - xoffset
    world_y = camera.half_height - yoffset

    pixel = inverse(camera.transform) * point(world_x, world_y, -1)
    origin = inverse(camera.transform) * point(0, 0, 0)
    direction = normalize(pixel - origin)

    return ray(origin, direction)


def render(camera, world):
    image = canvas(camera.hsize, camera.vsize)

    start = time.time()
    for y in range(camera.vsize):
        current = time.time()
        elapsed = round(current - start, 2)
        percent = round(y / camera.vsize * 100, 2)
        if y != 0:
            t = round((1 / (y / camera.vsize)) * elapsed - elapsed, 2)
            print(
                "\r"
                + str(percent).rjust(5)
                + "% : "
                + str(t)
                + "s left : "
                + str(elapsed)
                + "s elapsed",
                end=" ",
                flush=True,
            )
        for x in range(camera.hsize):
            ray = ray_for_pixel(camera, x, y)
            color = color_at(world, ray)
            write_pixel(image, x, y, color)
    print()

    return image
