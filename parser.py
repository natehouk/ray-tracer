from tuple import point
from group import group
from triangle import triangle

def obj_to_group(parser):
    g = group()
    for grp in parser.groups.values():
        for tri in grp:
            g.children.append(tri)
    return g

def fan_triangulation(vertices):
    triangles = []
    for i in range (2, len(vertices) - 1):
        tri = triangle(vertices[1], vertices[i], vertices[i+1])
        triangles.append(tri)
    return triangles

def parse_obj_file(file):
    p = parser()
    group = "default_group"
    for line in file.split("\n"):
        if line == "":
            p.ignored += 1
        elif line[0] == "g" and len(line.split(" ")) == 2:
            g = line.split(" ")
            group = g[1]
        elif line[0] == "v" and len(line.split(" ")) == 4:
            v = line.split(" ")
            p.vertices.append(point(float(v[1]), float(v[2]), float(v[3])))
        elif line[0] == "f" and len(line.split(" ")) >= 4:
            f = line.split(" ")
            if len(f) == 4:
                if group not in p.groups:
                    p.groups[group] = []
                p.groups[group].append(triangle(p.vertices[int(f[1])],
                                            p.vertices[int(f[2])],
                                            p.vertices[int(f[3])]))
            else:
                triangles = fan_triangulation(p.vertices)
                for tri in triangles:
                    if group not in p.groups:
                        p.groups[group] = []
                    p.groups[group].append(tri)
        else:
            p.ignored += 1
    return p

class parser:

    def __init__(self):
        self.ignored = 0
        self.vertices = []
        self.vertices.append(point(0, 0, 0))
        self.groups = {"default_group": []}