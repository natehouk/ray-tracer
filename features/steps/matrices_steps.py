from behave import *
from matrix import matrix, transpose
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


@given(u'the following matrix C')
def step_impl(context):
    context.C = matrix(2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1)


@then(u'A != C')
def step_impl(context):
    assert context.A != context.C


@given(u'the following matrix D')
def step_impl(context):
    context.D = matrix(-2, 1, 2, 3, 3, 2, 1, -1, 4, 3, 6, 5, 1, 2, 7, 8)


@then(u'A * D is the following 4x4 matrix')
def step_impl(context):
    assert context.A * context.D == matrix(20, 22, 50, 48, 44, 54, 114, 108, 40, 58, 110, 102, 16, 26, 46, 42)


@given(u'the following matrix E')
def step_impl(context):
    context.E = matrix(1, 2, 3, 4, 2, 4, 4, 2, 8, 6, 4, 1, 0, 0, 0, 1)


@given(u'b ← tuple(1, 2, 3, 1)')
def step_impl(context):
    context.b = tuple(1, 2, 3, 1)


@then(u'E * b = tuple(18, 24, 33, 1)')
def step_impl(context):
    assert context.E * context.b == tuple(18, 24, 33, 1)


@given(u'the following matrix F')
def step_impl(context):
    context.F = matrix(0, 1, 2, 4, 1, 2, 4, 8, 2, 4, 8, 16, 4, 8, 16, 32)


@then(u'F * identity_matrix = F')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    assert context.F * identity_matrix == context.F


@given(u'a ← tuple(1, 2, 3, 4)')
def step_impl(context):
    context.a = tuple(1, 2, 3, 4)


@then(u'identity_matrix * a = a')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    assert identity_matrix * context.a == context.a


@given(u'the following matrix G')
def step_impl(context):
    context.G = matrix(0, 9, 3, 0, 9, 8, 0, 8, 1, 8, 5, 3, 0, 0, 5, 8)


@then(u'transpose(G) is the following matrix')
def step_impl(context):
    assert transpose(context.G) == matrix(0, 9, 1, 0, 9, 8, 8, 0, 3, 0, 5, 5, 0, 8, 3, 8)


@given(u'A ← transpose(identity_matrix)')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    context.A = transpose(identity_matrix)


@then(u'A = identity_matrix')
def step_impl(context):
    identity_matrix = matrix(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
    assert context.A == identity_matrix


@given(u'the following 2x2 matrix A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following 2x2 matrix A')


@then(u'determinant(A) = 17')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 17')


@given(u'the following 3x3 matrix A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following 3x3 matrix A')


@then(u'submatrix(A, 0, 2) is the following 2x2 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then submatrix(A, 0, 2) is the following 2x2 matrix')


@given(u'the following 4x4 matrix A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following 4x4 matrix A')


@then(u'submatrix(A, 2, 1) is the following 3x3 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then submatrix(A, 2, 1) is the following 3x3 matrix')


@given(u'B ← submatrix(A, 1, 0)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← submatrix(A, 1, 0)')


@then(u'determinant(B) = 25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(B) = 25')


@then(u'minor(A, 1, 0) = 25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then minor(A, 1, 0) = 25')


@then(u'minor(A, 0, 0) = -12')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then minor(A, 0, 0) = -12')


@then(u'cofactor(A, 0, 0) = -12')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = -12')


@then(u'cofactor(A, 1, 0) = -25')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 1, 0) = -25')


@then(u'cofactor(A, 0, 0) = 56')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = 56')


@then(u'cofactor(A, 0, 1) = 12')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 1) = 12')


@then(u'cofactor(A, 0, 2) = -46')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 2) = -46')


@then(u'determinant(A) = -196')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = -196')


@then(u'cofactor(A, 0, 0) = 690')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 0) = 690')


@then(u'cofactor(A, 0, 1) = 447')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 1) = 447')


@then(u'cofactor(A, 0, 2) = 210')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 2) = 210')


@then(u'cofactor(A, 0, 3) = 51')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 0, 3) = 51')


@then(u'determinant(A) = -4071')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = -4071')


@then(u'determinant(A) = -2120')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = -2120')


@then(u'A is invertible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A is invertible')


@then(u'determinant(A) = 0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 0')


@then(u'A is not invertible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A is not invertible')


@given(u'B ← inverse(A)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← inverse(A)')


@then(u'determinant(A) = 532')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then determinant(A) = 532')


@then(u'cofactor(A, 2, 3) = -160')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 2, 3) = -160')


@then(u'B[3,2] = -160/532')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then B[3,2] = -160/532')


@then(u'cofactor(A, 3, 2) = 105')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then cofactor(A, 3, 2) = 105')


@then(u'B[2,3] = 105/532')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then B[2,3] = 105/532')


@then(u'B is the following 4x4 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then B is the following 4x4 matrix')


@then(u'inverse(A) is the following 4x4 matrix')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then inverse(A) is the following 4x4 matrix')


@given(u'the following 4x4 matrix B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following 4x4 matrix B')


@given(u'C ← A * B')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given C ← A * B')


@then(u'C * inverse(B) = A')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then C * inverse(B) = A')