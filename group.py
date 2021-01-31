from shape import intersect, shape


def add_child(group, shape):
    shape.parent = group
    group.children.append(shape)


class group(shape):
    def __init__(self):
        super().__init__()
        self.children = []

    def local_intersect(self, cube, ray):
        xs = []
        for child in self.children:
            for intersection in intersect(child, ray):
                xs.append(intersection)
        xs = sorted(xs, key=lambda x: x.t)
        return xs

    def local_normal_at(self, cube, point):
        raise Exception
