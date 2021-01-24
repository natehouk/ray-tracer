from math import sqrt

from behave import *

from cone import cone
from ray import ray
from tuple import normalize, point, vector
from util import equals


@given(u"shape ← cone()")
def step_impl(context):
    context.shape = cone()


@when(u"xs ← local_intersect(shape, r)")
def step_impl(context):
    context.xs = context.shape.local_intersect(context.shape, context.r)


@then(u"xs[0].t = 8.66025")
def step_impl(context):
    assert equals(context.xs[0].t, 8.66025)


@then(u"xs[1].t = 8.66025")
def step_impl(context):
    assert equals(context.xs[1].t, 8.66025)


@given(u"direction ← normalize(vector(-0.5, -1, 1))")
def step_impl(context):
    context.direction = normalize(vector(-0.5, -1, 1))


@given(u"r ← ray(point(1, 1, -5), direction)")
def step_impl(context):
    context.r = ray(point(1, 1, -5), context.direction)


@then(u"xs[0].t = 4.55006")
def step_impl(context):
    assert equals(context.xs[0].t, 4.55006)


@then(u"xs[1].t = 49.44994")
def step_impl(context):
    assert equals(context.xs[1].t, 49.44994)


@given(u"r ← ray(point(0, 0, -1), direction)")
def step_impl(context):
    context.r = ray(point(0, 0, -1), context.direction)


@then(u"xs[0].t = 0.35355")
def step_impl(context):
    assert equals(context.xs[0].t, 0.35355)


@given(u"shape.minimum ← -0.5")
def step_impl(context):
    context.shape.minimum = -0.5


@given(u"shape.maximum ← 0.5")
def step_impl(context):
    context.shape.maximum = 0.5


@given(u"shape.closed ← true")
def step_impl(context):
    context.shape.closed = True


@given(u"r ← ray(point(0, 0, -0.25), direction)")
def step_impl(context):
    context.r = ray(point(0, 0, -0.25), context.direction)


@when(u"n ← local_normal_at(shape, point(0, 0, 0))")
def step_impl(context):
    context.n = context.shape.local_normal_at(context.shape, point(0, 0, 0))


@then(u"n = vector(0, 0, 0)")
def step_impl(context):
    assert context.n == vector(0, 0, 0)


@when(u"n ← local_normal_at(shape, point(1, 1, 1))")
def step_impl(context):
    context.n = context.shape.local_normal_at(context.shape, point(1, 1, 1))


@then(u"n = vector(1, -√2, 1)")
def step_impl(context):
    assert context.n == vector(1, -sqrt(2), 1)


@when(u"n ← local_normal_at(shape, point(-1, -1, 0))")
def step_impl(context):
    context.n = context.shape.local_normal_at(context.shape, point(-1, -1, 0))


@then(u"n = vector(-1, 1, 0)")
def step_impl(context):
    assert context.n == vector(-1, 1, 0)
