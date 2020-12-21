class T:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return (self.w == 1.0)

    def is_vector(self):
        return (self.w == 0.0)
    

if __name__ == "__main__":
    t = T(1, 1, 1, 1)
    print(t.x)