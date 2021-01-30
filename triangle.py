from shape import shape
from ray import ray
from tuple import dot, normalize, cross
from shape import intersection
from util import EPSILON


class triangle(shape):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.e1 = p2 - p1
        self.e2 = p3 - p1
        self.normal = normalize(cross(self.e2, self.e1))

    def local_intersect(self, triangle, ray):
        dir_cross_e2 = cross(ray.direction, triangle.e2)
        det = dot(triangle.e1, dir_cross_e2)
        if abs(det) < EPSILON:
            return []
        else:
            f = 1.0 / det
            p1_to_origin = ray.origin - triangle.p1
            u = f * dot(p1_to_origin, dir_cross_e2)
            if u < 0 or u > 1:
                return []
            origin_cross_e1 = cross(p1_to_origin, triangle.e1)
            v = f * dot(ray.direction, origin_cross_e1)
            if v < 0 or (u + v) > 1:
                return []
            t = f * dot(triangle.e2, origin_cross_e1)
            return [intersection(t, triangle)]

    def local_normal_at(self, triangle, world_point):
        return self.normal
