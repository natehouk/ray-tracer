import time
from tuple import color, point, vector, normalize, projectile, environment, tick

def write_pixel(c, width, height, color):
    if width >= 0 and width < c.width and height >= 0 and height < c.height:
        c.canvas[int(width)][int(height)] = color
        return
    else:
        return Exception
    
def pixel_at(c, width, height):
    if width >= 0 and width < c.width and height >= 0 and height < c.height:
        return c.canvas[width][height]
    else:
        return Exception

def canvas_to_ppm(c):
    return ppm(c)

def clamp(c):
    return color(int(max(min(c.red * 255, 255), 0) + .5),
                 int(max(min(c.green * 255, 255), 0) + .5),
                 int(max(min(c.blue * 255, 255), 0) + .5))

class canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[color(0, 0, 0) for x in range(height)] for y in range(width)]

    def __str__(self):
        body = ""
        for i in range(0, self.height):
            cur = ""
            for j in range (0, self.width):
                clamped = clamp(self.canvas[j][i])
                cur += str(clamped.red)
                if len(cur) >= 67 and j != self.width - 1:
                    cur += "\n"
                    body += cur
                    cur = ""
                else:
                    cur += " "
                cur += str(clamped.green)
                if len(cur) >= 67 and j != self.width - 1:
                    cur += "\n"
                    body += cur
                    cur = ""
                else:
                    cur += " "
                cur += str(clamped.blue)
                if len(cur) >= 67 and j != self.width - 1:
                    cur += "\n"
                    body += cur
                    cur = ""
                elif j != self.width - 1:
                    cur += " "
            body += cur
            if i != self.height - 1:
                body += "\n"
        return body

class ppm:

    def __init__(self, c):
        self.header = "P3\n" + str(c.width) + " " + str(c.height) + "\n255"
        self.canvas = c
        self.body = str(c)

    def __str__(self):
        return self.header + "\n" + self.body + "\n"

    def write_file(self, filename):
        f = open(filename, "w")
        f.write(str(self))
        f.close()
    

if __name__ == "__main__":
    start = point(0, 1, 0)
    velocity = normalize(vector(1, 1.8, 0)) * 11.25
    p = projectile(start, velocity)

    gravity = vector(0, -0.1, 0)
    wind = vector(-0.01, 0, 0)
    e = environment(gravity, wind)

    red = color(1, 0, 0)

    c = canvas(900, 550)

    start = time.time()
    print("Starting render...")

    x = 0
    while(x < 300):
        write_pixel(c, p.position.x, c.height - p.position.y, red)
        p = tick(e, p)
        x += 1
    
    end = time.time()
    print("Finished render.")
    print(str(round(end - start, 2)) + "s")

    start = time.time()
    print("Start writing file...")
    canvas_to_ppm(c).write_file("images/projectile.ppm")
    end = time.time()
    print("Finished writing file.")
    print(str(round(end - start, 2)) + "s")