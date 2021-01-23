from behave import *
from cube import cube
from ray import ray
from tuple import vector, point

@given(u'c ← cube()')
def step_impl(context):
    context.c = cube()


@given(u'r ← ray(point(5, 0.5, 0), vector(-1, 0, 0))')
def step_impl(context):
    context.r = ray(point(5, 0.5, 0), vector(-1, 0, 0))


@when(u'xs ← local_intersect(c, r)')
def step_impl(context):
    context.xs = context.c.local_intersect(context.c, context.r)


@then(u'xs[1].t = 6')
def step_impl(context):
    assert context.xs[1].t == 6


@given(u'r ← ray(point(-5, 0.5, 0), vector(1, 0, 0))')
def step_impl(context):
    context.r = ray(point(-5, 0.5, 0), vector(1, 0, 0))


@given(u'r ← ray(point(0.5, 5, 0), vector(0, -1, 0))')
def step_impl(context):
    context.r = ray(point(0.5, 5, 0), vector(0, -1, 0))


@given(u'r ← ray(point(0.5, -5, 0), vector(0, 1, 0))')
def step_impl(context):
    context.r = ray(point(0.5, -5, 0), vector(0, 1, 0))


@given(u'r ← ray(point(0.5, 0, 5), vector(0, 0, -1))')
def step_impl(context):
    context.r = ray(point(0.5, 0, 5), vector(0, 0, -1))


@given(u'r ← ray(point(0.5, 0, -5), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0.5, 0, -5), vector(0, 0, 1))


@given(u'r ← ray(point(0, 0.5, 0), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0.5, 0), vector(0, 0, 1))


@then(u'xs[0].t = -1')
def step_impl(context):
    assert context.xs[0].t == -1


@then(u'xs[1].t = 1')
def step_impl(context):
    assert context.xs[1].t == 1


@given(u'r ← ray(point(-2, 0, 0), vector(0.2673, 0.5345, 0.8018))')
def step_impl(context):
    context.r = ray(point(-2, 0, 0), vector(0.2673, 0.5345, 0.8018))


@given(u'r ← ray(point(0, -2, 0), vector(0.8018, 0.2673, 0.5345))')
def step_impl(context):
    context.r = ray(point(0, -2, 0), vector(0.8018, 0.2673, 0.5345))


@given(u'r ← ray(point(0, 0, -2), vector(0.5345, 0.8018, 0.2673))')
def step_impl(context):
    context.r = ray(point(0, 0, -2), vector(0.5345, 0.8018, 0.2673))


@given(u'r ← ray(point(2, 0, 2), vector(0, 0, -1))')
def step_impl(context):
    context.r = ray(point(2, 0, 2), vector(0, 0, -1))


@given(u'r ← ray(point(0, 2, 2), vector(0, -1, 0))')
def step_impl(context):
    context.r = ray(point(0, 2, 2), vector(0, -1, 0))


@given(u'r ← ray(point(2, 2, 0), vector(-1, 0, 0))')
def step_impl(context):
    context.r = ray(point(2, 2, 0), vector(-1, 0, 0))