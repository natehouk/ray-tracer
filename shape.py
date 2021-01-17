import random
import time
from math import sqrt, pi
from tuple import point, vector, dot, normalize, color, EPSILON
from matrix import identity_matrix, transpose, inverse, scaling, rotation_z, shearing
from ray import ray, transform, position
from canvas import canvas, write_pixel, canvas_to_ppm
from material import material

def set_transform(shape, transform):
    shape.transform = transform
    return

def intersect(shape, ray):
    local_ray = transform(ray, inverse(shape.transform))
    return shape.local_intersect(shape, local_ray)

def normal_at(shape, point):
    local_point = inverse(shape.transform) * point
    local_normal = local_normal_at(shape, local_point)
    world_normal = transpose(inverse(shape.transform)) * local_normal
    world_normal.w = 0

    return normalize(world_normal)

def local_normal_at(shape, point):
    return vector(point.x, point.y, point.z)

def test_shape():
    return testShape()


class shape():

    def __init__(self):
        self.id = str.format("%032x" % random.getrandbits(128))
        self.transform = identity_matrix()
        self.material = material()

    def __eq__(self, other):
        return (self.transform == other.transform and
                self.material == other.material)

    def local_intersect(self, s, local_ray):
        s.saved_ray = local_ray


class testShape(shape):

    def __init__(self):
        super().__init__()