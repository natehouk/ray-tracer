from tuple import color

def write_pixel(c, width, height, color):
    c.canvas[width][height] = color

def pixel_at(c, width, height):
    return c.canvas[width][height]

def canvas_to_ppm(c):
    return ppm(c)

def clamp(c):
    return color(int(max(min(c.red * 255, 255), 0) + .5),
                 int(max(min(c.green * 255, 255), 0) + .5),
                 int(max(min(c.blue * 255, 255), 0) + .5 ))

class canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[color(0, 0, 0) for x in range(height)] for y in range(width)]

    def __str__(self):
        body = ""
        for i in range(0, self.height):
            for j in range (0, self.width):
                body += str(clamp(self.canvas[j][i]))
                if j != self.width - 1:
                    body += " "
            if i != self.height - 1:
                body += "\n"
        return body

class ppm:

    def __init__(self, c):
        self.header = "P3\n" + str(c.width) + " " + str(c.height) + "\n255"
        self.body = str(c)

    def __str__(self):
        print(self.header + self.body)