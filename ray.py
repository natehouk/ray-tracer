def position(ray, t):
    return ray.origin + ray.direction * t

def transform(ray, matrix):
    ray.origin = matrix * ray.origin 
    return ray

class ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction