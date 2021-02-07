from tuple import point

def parse_obj_file(file):
    p = parser()
    for line in file.split("\n"):
        if line[0] != "v" and line[0] != "f":
            p.ignored += 1
        elif line[0] == "v":
            v = line.split(" ")
            p.vertices.append(point(v[1], v[2], v[3]))
    return p

class parser:

    def __init__(self):
        self.ignored = 0
        self.vertices = []
        self.vertices.append(point(0, 0, 0))