import time
from copy import deepcopy
from math import cos, isnan, pi, sin

from canvas import canvas, canvas_to_ppm, write_pixel
from ray import ray
from tuple import color, cross, normalize, point, tuple
from util import equals


def transpose(m):
    t = matrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    for i in range(4):
        for j in range(4):
            t.matrix[j][i] = m.matrix[i][j]
    return t


def determinant(m):

    # calculate determinant of 2x2 matrix
    if m.size == 2:
        return m.matrix[0][0] * m.matrix[1][1] - m.matrix[0][1] * m.matrix[1][0]

    # calculate determinant of 3x3 or 4x4 matrix
    else:
        det = 0
        for i in range(m.size):
            det = det + m.matrix[0][i] * cofactor(m, 0, i)
        return det


def submatrix(m, row, column):

    # calculate submatrix of 3x3 or 4x4 matrix
    if m.size == 3:
        s = matrix(0, 0, 0, 0)
    else:
        s = matrix(0, 0, 0, 0, 0, 0, 0, 0, 0)
    l = []
    for i in range(m.size):
        if i == row:
            continue
        for j in range(m.size):
            if j == column:
                continue
            l.append(m.matrix[i][j])
    for i in range(m.size - 1):
        for j in range(m.size - 1):
            s.matrix[i][j] = l.pop(0)
    return s


def minor(m, row, column):

    # calculate minor of 3x3 matrix
    if m.size == 3 or m.size == 4:
        return determinant(submatrix(m, row, column))
    else:
        return NotImplemented


def cofactor(m, row, column):
    return minor(m, row, column) * (-1 if (row + column) % 2 != 0 else 1)


def is_invertable(m):
    return True if determinant(m) != 0 else False


def inverse(m):
    if m.inverse is not None:
        return m.inverse
    elif is_invertable(m) is not True:
        return Exception
    inverse = deepcopy(m)
    for i in range(m.size):
        for j in range(m.size):
            c = cofactor(m, i, j)
            inverse.matrix[j][i] = c / determinant(m)
    m.inverse = inverse
    return inverse


def identity_matrix():
    return matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)


def translation(x, y, z):
    return matrix(1, 0, 0, x, 0, 1, 0, y, 0, 0, 1, z, 0, 0, 0, 1)


def scaling(x, y, z):
    return matrix(x, 0, 0, 0, 0, y, 0, 0, 0, 0, z, 0, 0, 0, 0, 1)


def rotation_x(r):
    return matrix(1, 0, 0, 0, 0, cos(r), -sin(r), 0, 0, sin(r), cos(r), 0, 0, 0, 0, 1)


def rotation_y(r):
    return matrix(cos(r), 0, sin(r), 0, 0, 1, 0, 0, -sin(r), 0, cos(r), 0, 0, 0, 0, 1)


def rotation_z(r):
    return matrix(cos(r), -sin(r), 0, 0, sin(r), cos(r), 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)


def shearing(x_y, x_z, y_x, y_z, z_x, z_y):
    return matrix(1, x_y, x_z, 0, y_x, 1, y_z, 0, z_x, z_y, 1, 0, 0, 0, 0, 1)


def view_transform(frm, to, up):
    forward = normalize(to - frm)
    upn = normalize(up)
    left = cross(forward, upn)
    true_up = cross(left, forward)
    orientation = matrix(
        left.x,
        left.y,
        left.z,
        0,
        true_up.x,
        true_up.y,
        true_up.z,
        0,
        -forward.x,
        -forward.y,
        -forward.z,
        0,
        0,
        0,
        0,
        1,
    )
    return orientation * translation(-frm.x, -frm.y, -frm.z)


class matrix:
    def __init__(
        self,
        a,
        b,
        c,
        d,
        e=float("nan"),
        f=float("nan"),
        g=float("nan"),
        h=float("nan"),
        i=float("nan"),
        j=float("nan"),
        k=float("nan"),
        l=float("nan"),
        m=float("nan"),
        n=float("nan"),
        o=float("nan"),
        p=float("nan"),
    ):
        self.matrix = [[float("nan") for x in range(4)] for y in range(4)]
        if isnan(e):
            self.size = 2
            self.matrix[0][0] = a
            self.matrix[0][1] = b
            self.matrix[1][0] = c
            self.matrix[1][1] = d
        elif isnan(j):
            self.size = 3
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
            self.size = 4
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
        self.inverse = None

    def __eq__(self, other):
        if (
            equals(self.matrix[0][0], other.matrix[0][0])
            and equals(self.matrix[0][1], other.matrix[0][1])
            and equals(self.matrix[0][2], other.matrix[0][2])
            and equals(self.matrix[0][3], other.matrix[0][3])
            and equals(self.matrix[1][0], other.matrix[1][0])
            and equals(self.matrix[1][1], other.matrix[1][1])
            and equals(self.matrix[1][2], other.matrix[1][2])
            and equals(self.matrix[1][3], other.matrix[1][3])
            and equals(self.matrix[2][0], other.matrix[2][0])
            and equals(self.matrix[2][1], other.matrix[2][1])
            and equals(self.matrix[2][2], other.matrix[2][2])
            and equals(self.matrix[2][3], other.matrix[2][3])
            and equals(self.matrix[3][0], other.matrix[3][0])
            and equals(self.matrix[3][1], other.matrix[3][1])
            and equals(self.matrix[3][2], other.matrix[3][2])
            and equals(self.matrix[3][3], other.matrix[3][3])
        ):
            return True
        else:
            return False

    def __mul__(self, other):
        if isinstance(other, matrix):
            M = matrix(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            for i in range(4):
                for j in range(4):
                    M.matrix[i][j] = (
                        self.matrix[i][0] * other.matrix[0][j]
                        + self.matrix[i][1] * other.matrix[1][j]
                        + self.matrix[i][2] * other.matrix[2][j]
                        + self.matrix[i][3] * other.matrix[3][j]
                    )
            return M
        elif isinstance(other, tuple):
            T = tuple(0, 0, 0, 0)
            T.x = (
                self.matrix[0][0] * other.x
                + self.matrix[0][1] * other.y
                + self.matrix[0][2] * other.z
                + self.matrix[0][3] * other.w
            )
            T.y = (
                self.matrix[1][0] * other.x
                + self.matrix[1][1] * other.y
                + self.matrix[1][2] * other.z
                + self.matrix[1][3] * other.w
            )
            T.z = (
                self.matrix[2][0] * other.x
                + self.matrix[2][1] * other.y
                + self.matrix[2][2] * other.z
                + self.matrix[2][3] * other.w
            )
            T.w = (
                self.matrix[3][0] * other.x
                + self.matrix[3][1] * other.y
                + self.matrix[3][2] * other.z
                + self.matrix[3][3] * other.w
            )
            return T
        else:
            return NotImplemented

    def __str__(self):
        string = ""
        for i in range(self.size):
            for j in range(self.size):
                string += str(round(self.matrix[i][j], 2)).rjust(5, " ")
                if j != self.size - 1:
                    string += " | "
            string += "\n"
        return string
