from math import tan
from matrix import identity_matrix

class camera:

    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = identity_matrix()
        
        # calculate pixel size
        half_view = tan(field_of_view / 2)
        aspect = hsize / vsize
        if aspect >= 1:
            camera.half_width = half_view
            camera.half_height = half_view / aspect
        else:
            camera.half_width = half_view * aspect
            camera.half_height = half_view
        self.pixel_size = (camera.half_width * 2) / hsize