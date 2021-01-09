from tuple import color

def write_pixel(c, width, height, color):
    c.canvas[width][height] = color

def pixel_at(c, width, height):
    return c.canvas[width][height]

class canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[color(0, 0, 0) for x in range(height)] for y in range(width)]

    