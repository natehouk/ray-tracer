from behave import *
from tuple import point, vector
from plane import plane
from ray import ray

@given(u'p ← plane()')
def step_impl(context):
    context.p = plane()


@when(u'n1 ← local_normal_at(p, point(0, 0, 0))')
def step_impl(context):
    context.n1 = context.p.local_normal_at(context.p, point(0, 0, 0))


@when(u'n2 ← local_normal_at(p, point(10, 0, -10))')
def step_impl(context):
    context.n2 = context.p.local_normal_at(context.p, point(10, 0, -10))


@when(u'n3 ← local_normal_at(p, point(-5, 0, 150))')
def step_impl(context):
    context.n3 = context.p.local_normal_at(context.p, point(-5, 0, 150))


@then(u'n1 = vector(0, 1, 0)')
def step_impl(context):
    assert context.n1 == vector(0, 1, 0)


@then(u'n2 = vector(0, 1, 0)')
def step_impl(context):
    assert context.n2 == vector(0, 1, 0)


@then(u'n3 = vector(0, 1, 0)')
def step_impl(context):
    assert context.n3 == vector(0, 1, 0)


@given(u'r ← ray(point(0, 10, 0), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 10, 0), vector(0, 0, 1))


@when(u'xs ← local_intersect(p, r)')
def step_impl(context):
    context.xs = context.p.local_intersect(context.p, context.r)


@then(u'xs is empty')
def step_impl(context):
    assert len(context.xs) == 0


@given(u'r ← ray(point(0, 1, 0), vector(0, -1, 0))')
def step_impl(context):
    context.r = ray(point(0, 1, 0), vector(0, -1, 0))


@then(u'xs.count = 1')
def step_impl(context):
    assert len(context.xs) == 1


@then(u'xs[0].object = p')
def step_impl(context):
    assert context.xs[0].object == context.p


@given(u'r ← ray(point(0, -1, 0), vector(0, 1, 0))')
def step_impl(context):
    context.r = ray(point(0, -1, 0), vector(0, 1, 0))
