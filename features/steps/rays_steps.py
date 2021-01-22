from behave import *

from matrix import scaling, translation
from ray import position, ray, transform
from tuple import point, vector


@given(u"origin ← point(1, 2, 3)")
def step_impl(context):
    context.origin = point(1, 2, 3)


@given(u"direction ← vector(4, 5, 6)")
def step_impl(context):
    context.direction = vector(4, 5, 6)


@when(u"r ← ray(origin, direction)")
def step_impl(context):
    context.r = ray(context.origin, context.direction)


@then(u"r.origin = origin")
def step_impl(context):
    assert context.r.origin == context.origin


@then(u"r.direction = direction")
def step_impl(context):
    assert context.r.direction == context.direction


@given(u"r ← ray(point(2, 3, 4), vector(1, 0, 0))")
def step_impl(context):
    context.r = ray(point(2, 3, 4), vector(1, 0, 0))


@then(u"position(r, 0) = point(2, 3, 4)")
def step_impl(context):
    assert position(context.r, 0) == point(2, 3, 4)


@then(u"position(r, 1) = point(3, 3, 4)")
def step_impl(context):
    assert position(context.r, 1) == point(3, 3, 4)


@then(u"position(r, -1) = point(1, 3, 4)")
def step_impl(context):
    assert position(context.r, -1) == point(1, 3, 4)


@then(u"position(r, 2.5) = point(4.5, 3, 4)")
def step_impl(context):
    assert position(context.r, 2.5) == point(4.5, 3, 4)


@given(u"r ← ray(point(1, 2, 3), vector(0, 1, 0))")
def step_impl(context):
    context.r = ray(point(1, 2, 3), vector(0, 1, 0))


@given(u"m ← translation(3, 4, 5)")
def step_impl(context):
    context.m = translation(3, 4, 5)


@when(u"r2 ← transform(r, m)")
def step_impl(context):
    context.r2 = transform(context.r, context.m)


@then(u"r2.origin = point(4, 6, 8)")
def step_impl(context):
    assert context.r2.origin == point(4, 6, 8)


@then(u"r2.direction = vector(0, 1, 0)")
def step_impl(context):
    assert context.r2.direction == vector(0, 1, 0)


@given(u"m ← scaling(2, 3, 4)")
def step_impl(context):
    context.m = scaling(2, 3, 4)


@then(u"r2.origin = point(2, 6, 12)")
def step_impl(context):
    context.r2.origin == point(2, 6, 12)


@then(u"r2.direction = vector(0, 3, 0)")
def step_impl(context):
    context.r2.direction == vector(0, 3, 0)
