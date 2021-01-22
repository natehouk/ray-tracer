import random
import time
from math import pi, sqrt

from canvas import canvas, canvas_to_ppm, write_pixel
from material import material
from matrix import identity_matrix, inverse, rotation_z, scaling, shearing, transpose
from ray import position, ray, transform
from tuple import EPSILON, color, dot, normalize, point, vector


def set_transform(shape, transform):
    shape.transform = transform
    return


def intersect(shape, ray):
    local_ray = transform(ray, inverse(shape.transform))
    return shape.local_intersect(shape, local_ray)


def normal_at(shape, point):
    local_point = inverse(shape.transform) * point
    local_normal = shape.local_normal_at(shape, local_point)
    world_normal = transpose(inverse(shape.transform)) * local_normal
    world_normal.w = 0

    return normalize(world_normal)


class shape:
    def __init__(self):
        self.id = str.format("%032x" % random.getrandbits(128))
        self.transform = identity_matrix()
        self.material = material()

    def __eq__(self, other):
        return self.transform == other.transform and self.material == other.material

    def local_intersect(self, s, local_ray):
        s.saved_ray = local_ray

    def local_normal_at(self, s, point):
        return vector(point.x, point.y, point.z)


class test_shape(shape):
    def __init__(self):
        super().__init__()
