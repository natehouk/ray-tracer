import random
from math import pi

from material import material
from matrix import identity_matrix, inverse, rotation_y, transpose
from ray import position, transform
from tuple import dot, normalize, reflect, vector
from util import EPSILON


def set_transform(shape, transform):
    shape.transform = transform
    return


def intersect(shape, ray):
    local_ray = transform(ray, inverse(shape.transform))
    return shape.local_intersect(shape, local_ray)


def normal_at(shape, world_point):
    local_point = world_to_object(shape, world_point)
    local_normal = shape.local_normal_at(shape, local_point)
    return normal_to_world(shape, local_normal)


def intersections(*argv):
    i = []
    for arg in argv:
        i.append(arg)
    i = sorted(i, key=lambda x: x.t)
    return i


def hit(intersections):
    min = float("inf")
    h = None
    for i in intersections:
        if i.t >= 0 and i.t <= min:
            min = i.t
            h = i
    return h


def prepare_computations(intersection, ray, xs=None):
    c = comps()
    c.t = intersection.t
    c.object = intersection.object
    c.point = position(ray, c.t)
    c.eyev = -ray.direction
    c.normalv = normal_at(c.object, c.point)
    if dot(c.normalv, c.eyev) < 0:
        c.inside = True
        c.normalv = -c.normalv
    else:
        c.inside = False
    c.over_point = c.point + c.normalv * EPSILON
    c.under_point = c.point - c.normalv * EPSILON
    c.reflectv = reflect(ray.direction, c.normalv)
    containers = []
    if xs:
        for i in xs:
            if i == intersection:
                if len(containers) == 0:
                    c.n1 = 1.0
                else:
                    c.n1 = containers[-1].material.refractive_index
            if i.object in containers:
                containers.remove(i.object)
            else:
                containers.append(i.object)
            if i == intersection:
                if len(containers) == 0:
                    c.n2 = 1.0
                else:
                    c.n2 = containers[-1].material.refractive_index
                break
    return c


def world_to_object(shape, point):
    if shape.parent is not None:
        point = world_to_object(shape.parent, point)
    return inverse(shape.transform) * point


def normal_to_world(shape, normal):
    normal = transpose(inverse(shape.transform)) * normal
    normal.w = 0
    normal = normalize(normal)

    if shape.parent is not None:
        normal = normal_to_world(shape.parent, normal)

    return normal


class shape:
    def __init__(self):
        self.id = str.format("%032x" % random.getrandbits(128))
        self.parent = None
        self.transform = identity_matrix()
        self.material = material()

    def __eq__(self, other):
        return self.transform == other.transform and self.material == other.material

    def local_intersect(self, s, local_ray):
        s.saved_ray = local_ray

    def local_normal_at(self, s, point):
        return vector(point.x, point.y, point.z)


class comps:
    def __init__(self):
        self.t = None
        self.object = None
        self.point = None
        self.eyev = None
        self.normalv = None
        self.inside = None

    def __str__(self):
        return (
            "<"
            + str(self.t)
            + ", "
            + str(self.object)
            + ", "
            + str(self.point)
            + ", "
            + str(self.eyev)
            + ", "
            + str(self.normalv)
            + ", "
            + str(self.inside)
            + ">"
        )


class test_shape(shape):
    def __init__(self):
        super().__init__()


class intersection:
    def __init__(self, t, o):
        self.t = t
        self.object = o
