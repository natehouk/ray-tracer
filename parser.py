from tuple import point

def fan_triangulation(vertices):
    triangles = []
    for i in range (2, len(vertices) - 1):
        tri = face(vertices[1], vertices[i], vertices[i+1])
        triangles.append(tri)
    return triangles

def parse_obj_file(file):
    p = parser()
    for line in file.split("\n"):
        if line == "":
            p.ignored += 1
        elif line[0] == "v" and len(line.split(" ")) == 4:
            v = line.split(" ")
            p.vertices.append(point(float(v[1]), float(v[2]), float(v[3])))
        elif line[0] == "f" and len(line.split(" ")) >= 4:
            f = line.split(" ")
            if len(f) == 4:
                p.default_group.append(face(p.vertices[int(f[1])],
                                            p.vertices[int(f[2])],
                                            p.vertices[int(f[3])]))
            else:
                triangles = fan_triangulation(p.vertices)
                for triangle in triangles:
                    p.default_group.append(triangle)
        else:
            p.ignored += 1
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