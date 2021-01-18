from math import sqrt, isnan

# Equality precision
EPSILON = 0.0001

def equals(a, b):
    return abs(a - b) < EPSILON or (isnan(a) and isnan(b))

def is_point(p):
    return p.w == 1.0

def is_vector(v):
    return v.w == 0.0

def point(x, y, z):
    return tuple(x, y, z, 1.0)

def vector(x, y, z):
    return tuple(x, y, z, 0.0)

def color(r, g, b):
    return tuple(r, g, b, float('nan'))

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

def hadamard_product(c1, c2):
    return color(c1.red * c2.red, c1.green * c2.green, c1.blue * c2.blue)

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return projectile(position, velocity)

def reflect(i, normal):
    return i - normal * 2 * dot(i, normal)


class tuple:

    def __init__(self, x, y, z, w):
        self.x = x
        self.red = x
        self.y = y
        self.green = y
        self.z = z
        self.blue = z
        self.w = w

    def __eq__(self, other):
        if isnan(self.w) and isnan(other.w):
            return bool(equals(self.red, other.red) and
                        equals(self.green, other.green) and
                        equals(self.blue, other.blue))
        else:
            return bool(equals(self.x, other.x) and
                        equals(self.y, other.y) and
                        equals(self.z, other.z) and
                        equals(self.w, other.w))

    def __add__(self, other):
        if isnan(self.w) and isnan(other.w):
            return tuple(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z,
                         float('nan'))
        else:
            return tuple(self.x + other.x,
                         self.y + other.y,
                         self.z + other.z,
                         self.w + other.w)

    def __sub__(self, other):
        if isnan(self.w) and isnan(other.w):
            return tuple(self.x - other.x,
                         self.y - other.y,
                         self.z - other.z,
                         float('nan'))
        else:
            return tuple(self.x - other.x,
                         self.y - other.y,
                         self.z - other.z,
                         self.w - other.w)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            scalar = other
            return tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)
        elif isinstance(other, tuple) and  isnan(other.w):
            return hadamard_product(self, other)
        return NotImplementedError

    def __truediv__(self, scalar):
        return tuple(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def __neg__(self):
        return vector(0, 0, 0) - self

    def __str__(self):
        if (isnan(self.w)):
            return  str(self.x) + " " + str(self.y) + " " + str(self.z)
        else:
            return "tuple(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w) + ")"


class projectile:

    def __init__(self, p, v):
        self.position = p
        self.velocity = v

    def __str__(self):
        return "projectile(" + str(self.position) + ", " + str(self.velocity) + ")"


class environment:

    def __init__(self, g, w):
        self.gravity = g
        self.wind = w

    def __str__(self):
        return "environment(" + str(self.gravity) + ", " + str(self.wind) + ")"


class point_light:

    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def __eq__(self, other):
        return (self.position == other.position and
                self.intensity == other.intensity)


if __name__ == "__main__":
    # projectile starts one unit above the origin
    # velocity is normalzied to 1 unit/tick
    p = projectile(point(0, 1, 0), normalize(vector(1, 1, 0)))

    # gravity -0.1 unit/tick, and wind is -0.01 unit/tick
    e = environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))

    while(True):
        print(p)
        print(e)
        input()
        p = tick(e, p)