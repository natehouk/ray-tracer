from tuple import point

def parse_obj_file(file):
    p = parser()
    for line in file.split("\n"):
        if line == "" or (line[0] != "v" and line[0] != "f"):
            p.ignored += 1
        elif line[0] == "v":
            v = line.split(" ")
            p.vertices.append(point(float(v[1]), float(v[2]), float(v[3])))
        elif line[0] == "f":
            f = line.split(" ")
            p.default_group.append(face(p.vertices[int(f[1])],
                                        p.vertices[int(f[2])],
                                        p.vertices[int(f[3])]))
    return p

class parser:

    def __init__(self):
        self.ignored = 0
        self.vertices = []
        self.vertices.append(point(0, 0, 0))
        self.default_group = []

class face:

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3