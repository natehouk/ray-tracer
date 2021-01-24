from shape import shape


class group(shape):
    def __init__(self):
        super().__init__()
        self.children = []

    def local_intersect(self, cube, ray):
        pass

    def check_axis(self, origin, direction):
        pass

    def local_normal_at(self, cube, point):
        pass
