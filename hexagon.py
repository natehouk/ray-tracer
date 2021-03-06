from math import pi

from cylinder import cylinder
from group import add_child, group
from matrix import rotation_y, rotation_z, scaling, translation
from shape import set_transform
from sphere import sphere


def hexagon_corner():
    corner = sphere()
    set_transform(corner, translation(0, 0, -1) * scaling(0.25, 0.25, 0.25))
    return corner


def hexagon_edge():
    edge = cylinder()
    edge.minimum = 0
    edge.maximum = 1
    set_transform(
        edge,
        translation(0, 0, -1)
        * rotation_y(-pi / 6)
        * rotation_z(-pi / 2)
        * scaling(0.25, 1, 0.25),
    )
    return edge


def hexagon_side():
    side = group()
    add_child(side, hexagon_corner())
    add_child(side, hexagon_edge())
    return side


def hexagon():
    hex = group()

    for n in range(5):
        side = hexagon_side()
        set_transform(side, rotation_y(n * pi / 3))
        add_child(hex, side)

    return hex
