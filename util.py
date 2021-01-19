from matrix import inverse
from tuple import point, normalize
from ray import ray
from canvas import canvas, write_pixel
from world import color_at

LIMIT = 4

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

    for y in range(camera.vsize):
        print(str(y))
        for x in range(camera.hsize):
            ray = ray_for_pixel(camera, x, y)
            color = color_at(world, ray, LIMIT)
            write_pixel(image, x, y, color)
    
    return image