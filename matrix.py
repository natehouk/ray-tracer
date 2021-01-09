from math import isnan
from tuple import equals

class matrix:

    def __init__(self, a, b, c, d, 
                       e = float('nan'), f = float('nan'), g = float('nan'), h = float('nan'), 
                       i = float('nan'), j = float('nan'), k = float('nan'), l = float('nan'),
                       m = float('nan'), n = float('nan'), o = float('nan'), p = float('nan')):
        self.matrix = [[float('nan') for x in range(4)] for y in range(4)]
        if isnan(e):
            self.matrix[0][0] = a
            self.matrix[0][1] = b
            self.matrix[1][0] = c
            self.matrix[1][1] = d
        elif isnan(j):
            self.matrix[0][0] = a
            self.matrix[0][1] = b
            self.matrix[0][2] = c
            self.matrix[1][0] = d
            self.matrix[1][1] = e
            self.matrix[1][2] = f
            self.matrix[2][0] = g
            self.matrix[2][1] = h
            self.matrix[2][2] = i
        else:
            self.matrix[0][0] = a
            self.matrix[0][1] = b
            self.matrix[0][2] = c
            self.matrix[0][3] = d
            self.matrix[1][0] = e
            self.matrix[1][1] = f
            self.matrix[1][2] = g
            self.matrix[1][3] = h
            self.matrix[2][0] = i
            self.matrix[2][1] = j
            self.matrix[2][2] = k
            self.matrix[2][3] = l
            self.matrix[3][0] = m
            self.matrix[3][1] = n
            self.matrix[3][2] = o
            self.matrix[3][3] = p

    def __eq__(self, other):
        if (equals(self.matrix[0][0], other.matrix[0][0]) and
            equals(self.matrix[0][1], other.matrix[0][1]) and
            equals(self.matrix[0][2], other.matrix[0][2]) and
            equals(self.matrix[0][3], other.matrix[0][3]) and
            equals(self.matrix[1][0], other.matrix[1][0]) and
            equals(self.matrix[1][1], other.matrix[1][1]) and
            equals(self.matrix[1][2], other.matrix[1][2]) and
            equals(self.matrix[1][3], other.matrix[1][3]) and
            equals(self.matrix[2][0], other.matrix[2][0]) and
            equals(self.matrix[2][1], other.matrix[2][1]) and
            equals(self.matrix[2][2], other.matrix[2][2]) and
            equals(self.matrix[2][3], other.matrix[2][3]) and
            equals(self.matrix[3][0], other.matrix[3][0]) and
            equals(self.matrix[3][1], other.matrix[3][1]) and
            equals(self.matrix[3][2], other.matrix[3][2]) and
            equals(self.matrix[3][3], other.matrix[3][3])):
            return True
        else:
            return False