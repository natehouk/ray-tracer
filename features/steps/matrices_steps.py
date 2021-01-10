from behave import *
from matrix import matrix, transpose, determinant, submatrix, minor, cofactor, is_invertable, inverse
from tuple import tuple

@given(u'the following 4x4 matrix M')
def step_impl(context):
    context.M = matrix(1, 2, 3, 4, 5.5, 6.5, 7.5, 8.5, 9, 10, 11, 12, 13.5, 14.5, 15.5, 16.5)


@then(u'M[0,0] = 1')
def step_impl(context):
    assert context.M.matrix[0][0] == 1


@then(u'M[0,3] = 4')
def step_impl(context):
    assert context.M.matrix[0][3] == 4


@then(u'M[1,0] = 5.5')
def step_impl(context):
    assert context.M.matrix[1][0] == 5.5


@then(u'M[1,2] = 7.5')
def step_impl(context):
    assert context.M.matrix[1][2] == 7.5


@then(u'M[2,2] = 11')
def step_impl(context):
    assert context.M.matrix[2][2] == 11


@then(u'M[3,0] = 13.5')
def step_impl(context):
    assert context.M.matrix[3][0] == 13.5


@then(u'M[3,2] = 15.5')
def step_impl(context):
    assert context.M.matrix[3][2] == 15.5


@given(u'the following 2x2 matrix M')
def step_impl(context):
    context.M = matrix(-3, 5, 1, -2)


@then(u'M[0,0] = -3')
def step_impl(context):
    assert context.M.matrix[0][0] == -3


@then(u'M[0,1] = 5')
def step_impl(context):
    assert context.M.matrix[0][1] == 5


@then(u'M[1,0] = 1')
def step_impl(context):
    assert context.M.matrix[1][0] == 1


@then(u'M[1,1] = -2')
def step_impl(context):
    assert context.M.matrix[1][1] == -2


@given(u'the following 3x3 matrix M')
def step_impl(context):
    context.M = matrix(-3, 5, 0, 1, -2, -7, 0, 1, 1)


@then(u'M[2,2] = 1')
def step_impl(context):
    assert context.M.matrix[2][2] == 1


@given(u'the following matrix A')
def step_impl(context):
    context.A = matrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2)


@given(u'the following matrix B')
def step_impl(context):
    context.B = matrix(1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2)


@then(u'A = B')
def step_impl(context):
    assert context.A == context.B


@given(u'the following matrix B2')
def step_impl(context):
    context.B2 = matrix(2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1)


@then(u'A != B2')
def step_impl(context):
    assert context.A != context.B2


@given(u'the following matrix B3')
def step_impl(context):
    context.B3 = matrix(-2, 1, 2, 3, 3, 2, 1, -1, 4, 3, 6, 5, 1, 2, 7, 8)


@then(u'A * B3 is the following 4x4 matrix')
def step_impl(context):
    assert context.A * context.B3 == matrix(20, 22, 50, 48, 44, 54, 114, 108, 40, 58, 110, 102, 16, 26, 46, 42)


@given(u'the following matrix A2')
def step_impl(context):
    context.A2 = matrix(1, 2, 3, 4, 2, 4, 4, 2, 8, 6, 4, 1, 0, 0, 0, 1)


@given(u'b ← tuple(1, 2, 3, 1)')
def step_impl(context):
    context.b = tuple(1, 2, 3, 1)


@then(u'A2 * b = tuple(18, 24, 33, 1)')
def step_impl(context):
    assert context.A2 * context.b == tuple(18, 24, 33, 1)


@given(u'the following matrix A3')
def step_impl(context):
    context.A3 = matrix(0, 1, 2, 4, 1, 2, 4, 8, 2, 4, 8, 16, 4, 8, 16, 32)


@then(u'A3 * identity_matrix = A3')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    assert context.A3 * identity_matrix == context.A3


@given(u'a ← tuple(1, 2, 3, 4)')
def step_impl(context):
    context.a = tuple(1, 2, 3, 4)


@then(u'identity_matrix * a = a')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    assert identity_matrix * context.a == context.a


@given(u'the following matrix A4')
def step_impl(context):
    context.A4 = matrix(0, 9, 3, 0, 9, 8, 0, 8, 1, 8, 5, 3, 0, 0, 5, 8)


@then(u'transpose(A4) is the following matrix')
def step_impl(context):
    assert transpose(context.A4) == matrix(0, 9, 1, 0, 9, 8, 8, 0, 3, 0, 5, 5, 0, 8, 3, 8)


@given(u'A5 ← transpose(identity_matrix)')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    context.A5 = transpose(identity_matrix)


@then(u'A5 = identity_matrix')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    assert context.A5 == identity_matrix


@given(u'the following 2x2 matrix A6')
def step_impl(context):
    context.A6 = matrix(1, 5, -3, 2)


@then(u'determinant(A6) = 17')
def step_impl(context):
    assert determinant(context.A6) == 17


@given(u'the following 3x3 matrix A7')
def step_impl(context):
    context.A7 = matrix(1, 5, 0, -3, 2, 7, 0, 6, -3)


@then(u'submatrix(A7, 0, 2) is the following 2x2 matrix')
def step_impl(context):
    assert submatrix(context.A7, 0, 2) == matrix(-3, 2, 0, 6)


@given(u'the following 4x4 matrix A8')
def step_impl(context):
    context.A = matrix(-6, 1, 1, 6, -8, 5, 8, 6, -1, 0, 8, 2, -7, 1, -1, 1)


@then(u'submatrix(A8, 2, 1) is the following 3x3 matrix')
def step_impl(context):
    assert submatrix(context.A, 2, 1) == matrix(-6, 1, 6, -8, 8, 6, -7, -1, 1)


@given(u'the following 3x3 matrix A9')
def step_impl(context):
    context.A9 = matrix(3, 5, 0, 2, -1, -7, 6, -1, 5)


@given(u'B ← submatrix(A9, 1, 0)')
def step_impl(context):
    context.B = submatrix(context.A9, 1, 0)


@then(u'determinant(B) = 25')
def step_impl(context):
    assert determinant(context.B) == 25


@then(u'minor(A9, 1, 0) = 25')
def step_impl(context):
    assert minor(context.A9, 1, 0) == 25


@then(u'minor(A9, 0, 0) = -12')
def step_impl(context):
    assert minor(context.A9, 0, 0) == -12


@then(u'cofactor(A9, 0, 0) = -12')
def step_impl(context):
    assert cofactor(context.A9, 0, 0) == -12


@then(u'cofactor(A9, 1, 0) = -25')
def step_impl(context):
    assert cofactor(context.A9, 1, 0) == -25


@given(u'the following 3x3 matrix A10')
def step_impl(context):
    context.A10 = matrix(1, 2, 6, -5, 8, -4, 2, 6, 4)


@then(u'cofactor(A10, 0, 0) = 56')
def step_impl(context):
    assert cofactor(context.A10, 0, 0) == 56


@then(u'cofactor(A10, 0, 1) = 12')
def step_impl(context):
    assert cofactor(context.A10, 0, 1) == 12


@then(u'cofactor(A10, 0, 2) = -46')
def step_impl(context):
    assert cofactor(context.A10, 0, 2) == -46


@then(u'determinant(A10) = -196')
def step_impl(context):
    assert determinant(context.A10) == -196


@given(u'the following 4x4 matrix A11')
def step_impl(context):
    context.A11 = matrix(-2, -8, 3, 5, -3, 1, 7, 3, 1, 2, -9, 6, -6, 7, 7, -9)


@then(u'cofactor(A11, 0, 0) = 690')
def step_impl(context):
    print(cofactor(context.A11, 0, 0))
    assert cofactor(context.A11, 0, 0) == 690


@then(u'cofactor(A11, 0, 1) = 447')
def step_impl(context):
    assert cofactor(context.A11, 0, 1) == 447


@then(u'cofactor(A11, 0, 2) = 210')
def step_impl(context):
    assert cofactor(context.A11, 0, 2) == 210


@then(u'cofactor(A11, 0, 3) = 51')
def step_impl(context):
    assert cofactor(context.A11, 0, 3) == 51


@then(u'determinant(A11) = -4071')
def step_impl(context):
    assert determinant(context.A11) == -4071


@given(u'the following 4x4 matrix A12')
def step_impl(context):
    context.A12 = matrix(6, 4, 4, 4, 5, 5, 7, 6, 4, -9, 3, -7, 9, 1, 7, -6)


@then(u'determinant(A12) = -2120')
def step_impl(context):
    assert determinant(context.A12) == -2120


@then(u'A12 is invertible')
def step_impl(context):
    assert is_invertable(context.A12) is True


@given(u'the following 4x4 matrix A13')
def step_impl(context):
    context.A13 = matrix(-4, 2, -2, -3, 9, 6, 2, 6, 0, -5, 1, -5, 0, 0, 0, 0)


@then(u'determinant(A13) = 0')
def step_impl(context):
    assert determinant(context.A13) == 0


@then(u'A13 is not invertible')
def step_impl(context):
    assert is_invertable(context.A13) is False


@given(u'the following 4x4 matrix A14')
def step_impl(context):
    context.A14 = matrix(-5, 2, 6, -8, 1, -5, 1, 8, 7, 7, -6, -7, 1, -3, 7, 4)


@given(u'B ← inverse(A14)')
def step_impl(context):
    context.B = inverse(context.A14)


@then(u'determinant(A14) = 532')
def step_impl(context):
    assert determinant(context.A14) == 532


@then(u'cofactor(A14, 2, 3) = -160')
def step_impl(context):
    assert cofactor(context.A14, 2, 3) == -160


@then(u'B[3,2] = -160/532')
def step_impl(context):
    assert context.B.matrix[3][2] == -160/532


@then(u'cofactor(A14, 3, 2) = 105')
def step_impl(context):
    assert cofactor(context.A14, 3, 2) == 105


@then(u'B[2,3] = 105/532')
def step_impl(context):
    context.B.matrix[2][3] == 105/532


@then(u'B is the following 4x4 matrix')
def step_impl(context):
    context.B = matrix(0.21805, 0.45113, 0.24060, -0.04511, -0.80827, -1.45677, -0.44361, 0.52068, -0.07895, -0.22368, -0.05263, 0.19737, -0.52256, -0.81391, -0.30075, 0.30639)


@given(u'the following 4x4 matrix A15')
def step_impl(context):
    context.A15 = matrix(8, -5, 9, 2, 7, 5, 6, 1, -6, 0, 9, 6, -3, 0, -9, -4)


@then(u'inverse(A15) is the following 4x4 matrix')
def step_impl(context):
    assert inverse(context.A15) == matrix(-0.15385, -0.15385, -0.28205, -0.53846, -0.07692, 0.12308, 0.02564, 0.03077, 0.35897, 0.35897, 0.43590, 0.92308, -0.69231, -0.69231, -0.76923, -1.92308)


@given(u'the following 4x4 matrix A16')
def step_impl(context):
    context.A16 = matrix(9, 3, 0, 9, -5, -2, -6, -3, -4, 9, 6, 4, -7, 6, 6, 2)


@then(u'inverse(A16) is the following 4x4 matrix')
def step_impl(context):
    assert inverse(context.A16) == matrix(-0.04074, -0.07778, 0.14444, -0.22222, -0.07778, 0.03333, 0.36667, -0.33333, -0.02901, -0.14630, -0.10926, 0.12963, 0.17778, 0.06667, -0.26667, 0.33333)


@given(u'the following 4x4 matrix A17')
def step_impl(context):
    context.A17 = matrix(3, -9, 7, 3, 3, -8, 2, -9, -4, 4, 4, 1, -6, 5, -1, 1)


@given(u'the following 4x4 matrix B')
def step_impl(context):
    context.B = matrix(8, 2, 2, 2, 3, -1, 7, 0, 7, 0, 5, 4, 6, -2, 0, 5)


@given(u'C ← A17 * B')
def step_impl(context):
    context.C = context.A17 * context.B


@then(u'C * inverse(B) = A17')
def step_impl(context):
    assert context.C * inverse(context.B) == context.A17