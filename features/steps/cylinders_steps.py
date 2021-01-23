from behave import *
from cylinder import cylinder
from tuple import normalize
from ray import ray
from tuple import point, vector

@given(u'cyl ← cylinder()')
def step_impl(context):
    context.cyl = cylinder()


@given(u'direction ← normalize(vector(0, 1, 0))')
def step_impl(context):
    context.direction = normalize(vector(0, 1, 0))


@given(u'r ← ray(point(1, 0, 0), direction)')
def step_impl(context):
    context.r = ray(point(1, 0, 0), context.direction)


@when(u'xs ← local_intersect(cyl, r)')
def step_impl(context):
    context.xs = context.cyl.local_intersect(context.cyl, context.r)


@given(u'r ← ray(point(0, 0, 0), direction)')
def step_impl(context):
    context.r = ray(point(0, 0, 0), context.direction)


@given(u'direction ← normalize(vector(1, 1, 1))')
def step_impl(context):
    context.direction = normalize(vector(1, 1, 1))


@given(u'r ← ray(point(0, 0, -5), direction)')
def step_impl(context):
    context.r = ray(point(0, 0, -5), context.direction)