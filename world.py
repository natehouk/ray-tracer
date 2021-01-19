from tuple import point, color, point_light, magnitude, normalize
from sphere import sphere, intersections, prepare_computations, hit
from shape import intersect
from matrix import scaling
from material import lighting
from ray import ray

LIMIT = 4

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


def shade_hit(world, comps, remaining = LIMIT):
    shadowed = is_shadowed(world, comps.over_point)
    surface = lighting(comps.object.material, comps.object, world.light, comps.over_point, comps.eyev, comps.normalv, shadowed)
    reflected = reflected_color(world, comps, remaining)
    return surface + reflected


def color_at(world, ray, remaining = LIMIT):
    xs = intersect_world(world, ray)
    if len(xs) == 0:
        return color(0, 0, 0)
    else:
        for i in xs:
            if i.t > 0:
                comps = prepare_computations(i, ray)
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

def reflected_color(world, comps, remaining = LIMIT):
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

class world:

    def __init__(self):
        self.objects = []
        self.light = None
