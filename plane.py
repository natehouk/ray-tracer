from tuple import vector

class plane():

    def __init__(self):
        super().__init__()

    def local_normal_at(self, s, p):
        return vector(0, 1, 0)