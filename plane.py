from matrix import identity_matrix
from shape import shape
from sphere import intersection
from tuple import EPSILON, vector


class plane(shape):
    def __init__(self):
        self.transform = identity_matrix()
        self.test = True
        super().__init__()

    def local_normal_at(self, s, p):
        return vector(0, 1, 0)

    def local_intersect(self, s, local_ray):
        if abs(local_ray.direction.y) < EPSILON:
            return []
        else:
            t = -local_ray.origin.y / local_ray.direction.y
            return [intersection(t, s)]
