import math

class T:
    EPSILON = 0.00001

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return (self.w == 1.0)

    def is_vector(self):
        return (self.w == 0.0)

    @staticmethod
    def point(x, y, z):
        return T(x, y, z, 1.0)

    @staticmethod
    def vector(x, y, z):
        return T(x, y, z, 0.0)

    @staticmethod
    def equals(a, b):
        return abs(a - b) < T.EPSILON

    @staticmethod
    def magnitude(v):
        return math.sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2 + v.w ** 2)

    def __eq__(self, other):
        return bool((self.equals(self.x, other.x) and
                     self.equals(self.y, other.y) and
                     self.equals(self.z, other.z) and
                     self.equals(self.w, other.w)))

    def __add__(self, other):
        return T(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return T(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, scalar):
        return T(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def __floordiv__(self, scalar):
        return T(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __truediv__(self, scalar):
        return T(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __neg__(self):
        return T.vector(0, 0, 0) - self

    def __str__(self):
        return "T<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w) + ">"

if __name__ == "__main__":
    t = T(1, 1, 1, 1)
    print(t.x)