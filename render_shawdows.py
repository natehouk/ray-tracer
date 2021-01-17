import time
from math import pi
from sphere import sphere
from matrix import scaling, translation, rotation_x, rotation_y, view_transform
from material import material
from tuple import color, point, vector, point_light
from world import world
from util import render
from canvas import canvas_to_ppm
from camera import camera

def main():

    start = time.time()
    print("Starting render...")

    w = world()
    w.light = point_light(point(-10, 10, -10), color(1, 1, 1))

    floor = sphere()
    floor.transform = scaling(10, 0.01, 10)
    floor.material.color = color(1, 0.9, 0.9)
    floor.material.specular = 0
    w.objects.append(floor)

    left_wall = sphere()
    left_wall.transform = translation(0, 0, 5) * rotation_y(-pi/4) * rotation_x(pi/2) * scaling(10, 0.01, 10)
    left_wall.material = floor.material
    w.objects.append(left_wall)

    right_wall = sphere()
    right_wall.transform = translation(0, 0, 5) * rotation_y(pi/4) * rotation_x(pi/2) * scaling(10, 0.01, 10)
    right_wall.material = floor.material
    w.objects.append(right_wall)

    middle = sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    middle.material = material()
    middle.material.color = color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    w.objects.append(middle)

    right = sphere()
    right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
    right.material = material()
    right.material.color = color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    w.objects.append(right)

    left = sphere()
    left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
    left.material = material()
    left.material.color = color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    w.objects.append(left)

    cam = camera(200, 100, pi/3)
    cam.transform = view_transform(point(0, 1.5, -5), point(0, 1, 0), vector(0, 1, 0))

    canvas = render(cam, w)

    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(canvas).write_file("images/shawdows.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")

if __name__ == "__main__":
    main()