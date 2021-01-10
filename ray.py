def position(ray, t):
    return ray.origin + ray.direction * t

class ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction