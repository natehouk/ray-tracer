from behave import *
from matrix import matrix, translation, inverse, scaling, rotation_x, rotation_y, rotation_z, shearing, identity_matrix, view_transform
from tuple import point, vector
from math import pi, sqrt

@given(u'transform ← translation(5, -3, 2)')
def step_impl(context):
    context.transform = translation(5, -3, 2)


@given(u'p ← point(-3, 4, 5)')
def step_impl(context):
    context.p = point(-3, 4, 5)


@then(u'transform * p = point(2, 1, 7)')
def step_impl(context):
    assert context.transform * context.p == point(2, 1, 7)


@given(u'inv ← inverse(transform)')
def step_impl(context):
    context.inv = inverse(context.transform)


@then(u'inv * p = point(-8, 7, 3)')
def step_impl(context):
    context.inv * context.p == point(-8, 7, 3)


@given(u'v ← vector(-3, 4, 5)')
def step_impl(context):
    context.v = vector(-3, 4, 5)


@then(u'transform * v = v')
def step_impl(context):
    assert context.transform * context.v == context.v


@given(u'transform ← scaling(2, 3, 4)')
def step_impl(context):
    context.transform = scaling(2, 3, 4)


@given(u'p ← point(-4, 6, 8)')
def step_impl(context):
    context.p = point(-4, 6, 8)


@then(u'transform * p = point(-8, 18, 32)')
def step_impl(context):
    assert context.transform * context.p == point(-8, 18, 32)


@given(u'v ← vector(-4, 6, 8)')
def step_impl(context):
    context.v = vector(-4, 6, 8)


@then(u'transform * v = vector(-8, 18, 32)')
def step_impl(context):
    assert context.transform * context.v == vector(-8, 18, 32)


@then(u'inv * v = vector(-2, 2, 2)')
def step_impl(context):
    assert context.inv * context.v == vector(-2, 2, 2)


@given(u'transform ← scaling(-1, 1, 1)')
def step_impl(context):
    context.transform = scaling(-1, 1, 1)


@given(u'p ← point(2, 3, 4)')
def step_impl(context):
    context.p = point(2, 3, 4)


@then(u'transform * p = point(-2, 3, 4)')
def step_impl(context):
    assert context.transform * context.p == point(-2, 3, 4)


@given(u'p ← point(0, 1, 0)')
def step_impl(context):
    context.p = point(0, 1, 0)


@given(u'half_quarter ← rotation_x(π / 4)')
def step_impl(context):
    context.half_quarter = rotation_x(pi / 4)


@given(u'full_quarter ← rotation_x(π / 2)')
def step_impl(context):
    context.full_quarter = rotation_x(pi / 2)


@then(u'half_quarter * p = point(0, √2/2, √2/2)')
def step_impl(context):
    assert context.half_quarter * context.p == point(0, sqrt(2)/2, sqrt(2)/2)


@then(u'full_quarter * p = point(0, 0, 1)')
def step_impl(context):
    assert context.full_quarter * context.p == point(0, 0, 1)


@given(u'inv ← inverse(half_quarter)')
def step_impl(context):
    context.inv = inverse(context.half_quarter)


@then(u'inv * p = point(0, √2/2, -√2/2)')
def step_impl(context):
    assert context.inv * context.p == point(0, sqrt(2)/2, -sqrt(2)/2)


@given(u'p ← point(0, 0, 1)')
def step_impl(context):
    context.p = point(0, 0, 1)


@given(u'half_quarter ← rotation_y(π / 4)')
def step_impl(context):
    context.half_quarter = rotation_y(pi / 4)


@given(u'full_quarter ← rotation_y(π / 2)')
def step_impl(context):
    context.full_quarter = rotation_y(pi / 2)


@then(u'half_quarter * p = point(√2/2, 0, √2/2)')
def step_impl(context):
    assert context.half_quarter * context.p == point(sqrt(2)/2, 0, sqrt(2)/2)


@then(u'full_quarter * p = point(1, 0, 0)')
def step_impl(context):
    assert context.full_quarter * context.p == point(1, 0, 0)


@given(u'half_quarter ← rotation_z(π / 4)')
def step_impl(context):
    context.half_quarter = rotation_z(pi / 4)


@given(u'full_quarter ← rotation_z(π / 2)')
def step_impl(context):
    context.full_quarter = rotation_z(pi / 2)


@then(u'half_quarter * p = point(-√2/2, √2/2, 0)')
def step_impl(context):
    assert context.half_quarter * context.p == point(-sqrt(2)/2, sqrt(2)/2, 0)


@then(u'full_quarter * p = point(-1, 0, 0)')
def step_impl(context):
    assert context.full_quarter * context.p == point(-1, 0, 0)


@given(u'transform ← shearing(1, 0, 0, 0, 0, 0)')
def step_impl(context):
    context.transform = shearing(1, 0, 0, 0, 0, 0)


@then(u'transform * p = point(5, 3, 4)')
def step_impl(context):
    assert context.transform * context.p == point(5, 3, 4)


@given(u'transform ← shearing(0, 1, 0, 0, 0, 0)')
def step_impl(context):
    context.transform = shearing(0, 1, 0, 0, 0, 0)


@then(u'transform * p = point(6, 3, 4)')
def step_impl(context):
    assert context.transform * context.p == point(6, 3, 4)


@given(u'transform ← shearing(0, 0, 1, 0, 0, 0)')
def step_impl(context):
    context.transform = shearing(0, 0, 1, 0, 0, 0)


@then(u'transform * p = point(2, 5, 4)')
def step_impl(context):
    assert context.transform * context.p == point(2, 5, 4)


@given(u'transform ← shearing(0, 0, 0, 1, 0, 0)')
def step_impl(context):
    context.transform = shearing(0, 0, 0, 1, 0, 0)


@then(u'transform * p = point(2, 7, 4)')
def step_impl(context):
    assert context.transform * context.p == point(2, 7, 4)


@given(u'transform ← shearing(0, 0, 0, 0, 1, 0)')
def step_impl(context):
    context.transform = shearing(0, 0, 0, 0, 1, 0)


@then(u'transform * p = point(2, 3, 6)')
def step_impl(context):
    assert context.transform * context.p == point(2, 3, 6)


@given(u'transform ← shearing(0, 0, 0, 0, 0, 1)')
def step_impl(context):
    context.transform = shearing(0, 0, 0, 0, 0, 1)


@then(u'transform * p = point(2, 3, 7)')
def step_impl(context):
    assert context.transform * context.p == point(2, 3, 7)


@given(u'p ← point(1, 0, 1)')
def step_impl(context):
    context.p = point(1, 0, 1)


@given(u'A ← rotation_x(π / 2)')
def step_impl(context):
    context.A = rotation_x(pi / 2)


@given(u'B ← scaling(5, 5, 5)')
def step_impl(context):
    context.B = scaling(5, 5, 5)


@given(u'C ← translation(10, 5, 7)')
def step_impl(context):
    context.C = translation(10, 5, 7)


@when(u'p2 ← A * p')
def step_impl(context):
    context.p2 = context.A * context.p


@then(u'p2 = point(1, -1, 0)')
def step_impl(context):
    assert context.p2 == point(1, -1, 0)


@when(u'p3 ← B * p2')
def step_impl(context):
    context.p3 = context.B * context.p2


@then(u'p3 = point(5, -5, 0)')
def step_impl(context):
    assert context.p3 == point(5, -5, 0)


@when(u'p4 ← C * p3')
def step_impl(context):
    context.p4 = context.C * context.p3


@then(u'p4 = point(15, 0, 7)')
def step_impl(context):
    assert context.p4 == point(15, 0, 7)


@when(u'T ← C * B * A')
def step_impl(context):
    context.T = context.C * context.B * context.A


@then(u'T * p = point(15, 0, 7)')
def step_impl(context):
    assert context.T * context.p == point(15, 0, 7)


@given(u'frm ← point(0, 0, 0)')
def step_impl(context):
    context.frm = point(0, 0, 0)


@given(u'to ← point(0, 0, -1)')
def step_impl(context):
    context.to = point(0, 0, -1)


@given(u'up ← vector(0, 1, 0)')
def step_impl(context):
    context.up = vector(0, 1, 0)


@when(u't ← view_transform(frm, to, up)')
def step_impl(context):
    context.t = view_transform(context.frm, context.to, context.up)


@then(u't = identity_matrix')
def step_impl(context):
    assert context.t == identity_matrix()


@given(u'to ← point(0, 0, 1)')
def step_impl(context):
    context.to = point(0, 0, 1)


@then(u't = scaling(-1, 1, -1)')
def step_impl(context):
    assert context.t == scaling(-1, 1, -1)


@given(u'frm ← point(0, 0, 8)')
def step_impl(context):
    context.frm = point(0, 0, 8)


@given(u'to ← point(0, 0, 0)')
def step_impl(context):
    context.to = point(0, 0, 0)


@then(u't = translation(0, 0, -8)')
def step_impl(context):
    assert context.t == translation(0, 0, -8)


@given(u'frm ← point(1, 3, 2)')
def step_impl(context):
    context.frm = point(1, 3, 2)


@given(u'to ← point(4, -2, 8)')
def step_impl(context):
    context.to = point(4, -2, 8)


@given(u'up ← vector(1, 1, 0)')
def step_impl(context):
    context.up = vector(1, 1, 0)


@then(u't is the following 4x4 matrix')
def step_impl(context):
    assert context.t == matrix(-0.50709, 0.50709, 0.67612, -2.36643, 0.76772, 0.60609, 0.12122, -2.82843, -0.35857, 0.59761, -0.71714, 0.00000, 0.00000, 0.00000, 0.00000, 1.00000)