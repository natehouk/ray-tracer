from shape import shape
from sphere import intersection
from tuple import vector
from util import EPSILON


class cube(shape):
    def __init__(self):
        super().__init__()

    def local_intersect(self, cube, ray):

        xtmin, xtmax = self.check_axis(ray.origin.x, ray.direction.x)
        ytmin, ytmax = self.check_axis(ray.origin.y, ray.direction.y)
        ztmin, ztmax = self.check_axis(ray.origin.z, ray.direction.z)

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        if tmin > tmax:
            return []

        return [intersection(tmin, cube), intersection(tmax, cube)]

    def check_axis(self, origin, direction):
        tmin_numerator = -1 - origin
        tmax_numerator = 1 - origin

        if abs(direction) >= EPSILON:
            tmin = tmin_numerator / direction
            tmax = tmax_numerator / direction
        else:
            tmin = tmin_numerator * float("inf")
            tmax = tmax_numerator * float("inf")

        if tmin > tmax:
            tmin, tmax = tmax, tmin

        return tmin, tmax

    def local_normal_at(self, cube, point):
        maxc = max(abs(point.x), abs(point.y), abs(point.z))

        if maxc == abs(point.x):
            return vector(point.x, 0, 0)
        elif maxc == abs(point.y):
            return vector(0, point.y, 0)
        else:
            return vector(0, 0, point.z)
