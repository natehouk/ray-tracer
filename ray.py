from copy import deepcopy

def position(ray, t):
    return ray.origin + ray.direction * t

def transform(ray, matrix):

    # make sure you return a new array!
    r = deepcopy(ray)
    
    r.origin = matrix * ray.origin 
    r.direction = matrix * ray.direction
    
    return r

class ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction