from shape import shape
from tuple import  normalize, cross


class triangle(shape):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.e1 = p2 - p1
        self.e2 = p3 - p1
        self.normal = normalize(cross(self.e2, self.e1))

    def local_intersect(self, s, local_ray):
        pass

    def local_normal_at(self, sphere, world_point):
        return self.normal
