from tuple import point, color, point_light
from sphere import sphere, intersect, intersections
from matrix import scaling

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
            s.append(i[0])
            s.append(i[1])
    s = sorted(s, key=lambda x: x.t)
    return s

class world:

    def __init__(self):
        self.objects = []
        self.light = None
