from math import sqrt

# Equality precision
EPSILON = 0.00001

def equals(a, b):
    return abs(a - b) < EPSILON

def is_point(p):
    return p.w == 1.0

def is_vector(v):
    return v.w == 0.0

def point(x, y, z):
    return tuple(x, y, z, 1.0)

def vector(x, y, z):
    return tuple(x, y, z, 0.0)

def magnitude(v):
    return sqrt(v.x ** 2 + v.y ** 2 + v.z ** 2 + v.w ** 2)

def normalize(v):
    return tuple(v.x / magnitude(v),
                 v.y / magnitude(v),
                 v.z / magnitude(v),
                 v.w / magnitude(v))

def dot(a, b):
    return (a.x * b.x +
            a.y * b.y +
            a.z * b.z +
            a.w * b.w)

def cross(a, b):
    return vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)

class tuple:

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __eq__(self, t):
        return bool((equals(self.x, t.x) and
                     equals(self.y, t.y) and
                     equals(self.z, t.z) and
                     equals(self.w, t.w)))

    def __add__(self, t):
        return tuple(self.x + t.x, self.y + t.y, self.z + t.z, self.w + t.w)

    def __sub__(self, t):
        return tuple(self.x - t.x, self.y - t.y, self.z - t.z, self.w - t.w)

    def __mul__(self, scalar):
        return tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def __truediv__(self, scalar):
        return tuple(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __neg__(self):
        return vector(0, 0, 0) - self

    def __str__(self):
        return "T<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w) + ">"

if __name__ == "__main__":
    t = tuple(1, 1, 1, 1)
    print(t.x)