import time

from canvas import canvas, write_pixel
from matrix import inverse
from ray import ray
from tuple import normalize, point
from world import color_at


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
