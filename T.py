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
    def equals(a, b):
        return abs(a - b) < T.EPSILON

    def __eq__(self, other):
        return bool((self.equals(self.x, other.x) and
                     self.equals(self.y, other.y) and
                     self.equals(self.z, other.z) and
                     self.equals(self.w, other.w)))

    def __add__(self, other):
        return T(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return T(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __str__(self):
        return "T<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ", " + str(self.w) + ">"

if __name__ == "__main__":
    t = T(1, 1, 1, 1)
    print(t.x)