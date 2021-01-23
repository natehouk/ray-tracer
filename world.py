from math import sqrt

from material import lighting
from matrix import scaling
from ray import ray
from shape import intersect
from sphere import hit, prepare_computations, sphere
from tuple import color, dot, magnitude, normalize, point, point_light
from util import LIMIT


def default_world():
    w = world()
    w.light = point_light(point(-10, 10, -10), color(1, 1, 1))
    s1 = sphere()
    s1.material.color = color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    w.objects.append(s1)
    s2 = sphere()
    s2.transform = scaling(0.5, 0.5, 0.5)
    w.objects.append(s2)
    return w


def intersect_world(world, ray):
    s = []
    for o in world.objects:
        i = intersect(o, ray)
        if len(i) != 0:
            for j in i:
                s.append(j)
    s = sorted(s, key=lambda x: x.t)

    return s


def shade_hit(world, comps, remaining=LIMIT):
    shadowed = is_shadowed(world, comps.over_point)
    surface = lighting(
        comps.object.material,
        comps.object,
        world.light,
        comps.over_point,
        comps.eyev,
        comps.normalv,
        shadowed,
    )
    reflected = reflected_color(world, comps, remaining)
    refracted = refracted_color(world, comps, remaining)

    material = comps.object.material
    if material.reflective > 0 and material.transparency > 0:
        reflectance = schlick(comps)
        return surface + reflected * reflectance + refracted * (1 - reflectance)
    else:
        return surface + reflected + refracted


def color_at(world, ray, remaining=LIMIT):
    xs = intersect_world(world, ray)
    if len(xs) == 0:
        return color(0, 0, 0)
    else:
        for i in xs:
            if i.t > 0:
                comps = prepare_computations(i, ray, xs)
                return shade_hit(world, comps, remaining)
    return color(0, 0, 0)


def is_shadowed(world, point):
    v = world.light.position - point
    distance = magnitude(v)
    direction = normalize(v)

    r = ray(point, direction)
    intersections = intersect_world(world, r)

    h = hit(intersections)
    if h is not None and h.t < distance:
        return True
    else:
        return False


def reflected_color(world, comps, remaining=LIMIT):
    if remaining <= 0:
        return color(0, 0, 0)
    else:
        if comps.object.material.reflective == 0:
            return color(0, 0, 0)
        else:
            reflect_ray = ray(comps.over_point, comps.reflectv)
            remaining -= 1
            c = color_at(world, reflect_ray, remaining)

            return c * comps.object.material.reflective


def refracted_color(world, comps, remaining):
    if comps.object.material.transparency == 0 or remaining <= 0:
        return color(0, 0, 0)
    else:
        n_ratio = comps.n1 / comps.n2
        cos_i = dot(comps.eyev, comps.normalv)
        sin2_t = n_ratio ** 2 * (1 - cos_i ** 2)
        if sin2_t > 1:
            return color(0, 0, 0)
        else:
            cos_t = sqrt(1.0 - sin2_t)
            direction = comps.normalv * (n_ratio * cos_i - cos_t) - comps.eyev * n_ratio
            refract_ray = ray(comps.under_point, direction)
            c = (
                color_at(world, refract_ray, remaining - 1)
                * comps.object.material.transparency
            )
            return c


def schlick(comps):
    cos = dot(comps.eyev, comps.normalv)
    if comps.n1 > comps.n2:
        n = comps.n1 / comps.n2
        sin2_t = (n ** 2) * (1.0 - cos ** 2)
        if sin2_t > 1.0:
            return 1.0
        cos_t = sqrt(1.0 - sin2_t)
        cos = cos_t

    r0 = ((comps.n1 - comps.n2) / (comps.n1 + comps.n2)) ** 2
    return r0 + (1 - r0) * (1 - cos) ** 5


class world:
    def __init__(self):
        self.objects = []
        self.light = None
