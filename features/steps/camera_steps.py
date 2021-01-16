from behave import *
from math import pi, sqrt
from tuple import point, vector, color, equals
from camera import camera
from matrix import identity_matrix, rotation_y, translation, view_transform
from util import ray_for_pixel, render
from canvas import pixel_at

@given(u'hsize ← 160')
def step_impl(context):
    context.hsize = 160


@given(u'vsize ← 120')
def step_impl(context):
    context.vsize = 120


@given(u'field_of_view ← π/2')
def step_impl(context):
    context.field_of_view = pi/2


@when(u'c ← camera(hsize, vsize, field_of_view)')
def step_impl(context):
    context.c = camera(context.hsize, context.vsize, context.field_of_view)


@then(u'c.hsize = 160')
def step_impl(context):
    assert context.c.hsize == 160


@then(u'c.vsize = 120')
def step_impl(context):
    assert context.c.vsize == 120


@then(u'c.field_of_view = π/2')
def step_impl(context):
    assert context.c.field_of_view == pi/2


@then(u'c.transform = identity_matrix')
def step_impl(context):
    assert context.c.transform == identity_matrix()


@given(u'c ← camera(200, 125, π/2)')
def step_impl(context):
    context.c = camera(200, 125, pi/2)


@then(u'c.pixel_size = 0.01')
def step_impl(context):
    assert equals(context.c.pixel_size, 0.01)


@given(u'c ← camera(125, 200, π/2)')
def step_impl(context):
    context.c = camera(125, 200, pi/2)


@given(u'c ← camera(201, 101, π/2)')
def step_impl(context):
    context.c = camera(201, 101, pi/2)


@when(u'r ← ray_for_pixel(c, 100, 50)')
def step_impl(context):
    context.r = ray_for_pixel(context.c, 100, 50)


@then(u'r.origin = point(0, 0, 0)')
def step_impl(context):
    assert context.r.origin == point(0, 0, 0)


@then(u'r.direction = vector(0, 0, -1)')
def step_impl(context):
    assert context.r.direction == vector(0, 0, -1)


@when(u'r ← ray_for_pixel(c, 0, 0)')
def step_impl(context):
    context.r = ray_for_pixel(context.c, 0, 0)


@then(u'r.direction = vector(0.66519, 0.33259, -0.66851)')
def step_impl(context):
    assert context.r.direction == vector(0.66519, 0.33259, -0.66851)


@when(u'c.transform ← rotation_y(π/4) * translation(0, -2, 5)')
def step_impl(context):
    context.c.transform = rotation_y(pi/4) * translation(0, -2, 5)


@then(u'r.origin = point(0, 2, -5)')
def step_impl(context):
    assert context.r.origin == point(0, 2, -5)


@then(u'r.direction = vector(√2/2, 0, -√2/2)')
def step_impl(context):
    assert context.r.direction == vector(sqrt(2)/2, 0, -sqrt(2)/2)


@given(u'c ← camera(11, 11, π/2)')
def step_impl(context):
    context.c = camera(11, 11, pi/2)


@given(u'from ← point(0, 0, -5)')
def step_impl(context):
    context.frm = point(0, 0, -5)


@given(u'c.transform ← view_transform(from, to, up)')
def step_impl(context):
    context.c.transform = view_transform(context.frm, context.to, context.up)


@when(u'image ← render(c, w)')
def step_impl(context):
    context.image = render(context.c, context.w)


@then(u'pixel_at(image, 5, 5) = color(0.38066, 0.47583, 0.2855)')
def step_impl(context):
    print(pixel_at(context.image, 5, 5))
    assert pixel_at(context.image, 5, 5) == color(0.38066, 0.47583, 0.2855)
