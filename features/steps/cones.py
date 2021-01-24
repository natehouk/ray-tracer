from behave import *
from cone import cone
from tuple import normalize, vector, point
from ray import ray
from util import equals

@given(u'shape ← cone()')
def step_impl(context):
    context.shape = cone()


@when(u'xs ← local_intersect(shape, r)')
def step_impl(context):
    context.xs = context.shape.local_intersect(context.shape, context.r)


@then(u'xs[0].t = 8.66025')
def step_impl(context):
    assert equals(context.xs[0].t, 8.66025)


@then(u'xs[1].t = 8.66025')
def step_impl(context):
    assert equals(context.xs[1].t, 8.66025)


@given(u'direction ← normalize(vector(-0.5, -1, 1))')
def step_impl(context):
    context.direction = normalize(vector(-0.5, -1, 1))


@given(u'r ← ray(point(1, 1, -5), direction)')
def step_impl(context):
    context.r = ray(point(1, 1, -5), context.direction)


@then(u'xs[0].t = 4.55006')
def step_impl(context):
    assert equals(context.xs[0].t, 4.55006)


@then(u'xs[1].t = 49.44994')
def step_impl(context):
    assert equals(context.xs[1].t, 49.44994)


@given(u'r ← ray(point(0, 0, -1), direction)')
def step_impl(context):
    context.r = ray(point(0, 0, -1), context.direction)


@then(u'xs[0].t = 0.35355')
def step_impl(context):
    assert equals(context.xs[0].t, 0.35355)
