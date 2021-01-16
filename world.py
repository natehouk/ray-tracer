from tuple import point, color, point_light
from sphere import sphere, intersect, intersections, prepare_computations
from matrix import scaling
from material import lighting

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


def shade_hit(world, comps):
    return lighting(comps.object.material, world.light, comps.point, comps.eyev, comps.normalv)


def color_at(world, ray):
    xs = intersect_world(world, ray)
    if len(xs) == 0:
        return color(0, 0, 0)
    else:
        for i in xs:
            if i.t > 0:
                comps = prepare_computations(i, ray)
                return shade_hit(world, comps)
    return color(0, 0, 0)

class world:

    def __init__(self):
        self.objects = []
        self.light = None
