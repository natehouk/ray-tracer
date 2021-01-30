from behave import *
from tuple import point, vector
from triangle import triangle
from ray import ray

@given(u'p1 ← point(0, 1, 0)')
def step_impl(context):
    context.p1 = point(0, 1, 0)


@given(u'p2 ← point(-1, 0, 0)')
def step_impl(context):
    context.p2 = point(-1, 0, 0)


@given(u'p3 ← point(1, 0, 0)')
def step_impl(context):
    context.p3 = point(1, 0, 0)


@given(u't ← triangle(p1, p2, p3)')
def step_impl(context):
    context.t = triangle(context.p1, context.p2, context.p3)


@then(u't.p1 = p1')
def step_impl(context):
    assert context.t.p1 == context.p1


@then(u't.p2 = p2')
def step_impl(context):
    assert context.t.p2 == context.p2


@then(u't.p3 = p3')
def step_impl(context):
    assert context.t.p3 == context.p3


@then(u't.e1 = vector(-1, -1, 0)')
def step_impl(context):
    assert context.t.e1 == vector(-1, -1, 0)


@then(u't.e2 = vector(1, -1, 0)')
def step_impl(context):
    assert context.t.e2 == vector(1, -1, 0)


@then(u't.normal = vector(0, 0, -1)')
def step_impl(context):
    assert context.t.normal == vector(0, 0, -1)


@given(u't ← triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))')
def step_impl(context):
    context.t = triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))


@when(u'n1 ← local_normal_at(t, point(0, 0.5, 0))')
def step_impl(context):
    context.n1 = context.t.local_normal_at(context.t, point(0, 0.5, 0))


@when(u'n2 ← local_normal_at(t, point(-0.5, 0.75, 0))')
def step_impl(context):
    context.n2 = context.t.local_normal_at(context.t, point(-0.5, 0.75, 0))


@when(u'n3 ← local_normal_at(t, point(0.5, 0.25, 0))')
def step_impl(context):
    context.n3 = context.t.local_normal_at(context.t, point(0.5, 0.25, 0))


@then(u'n1 = t.normal')
def step_impl(context):
    assert context.n1 == context.t.normal


@then(u'n2 = t.normal')
def step_impl(context):
    assert context.n2 == context.t.normal


@then(u'n3 = t.normal')
def step_impl(context):
    assert context.n3 == context.t.normal


@given(u'r ← ray(point(0, -1, -2), vector(0, 1, 0))')
def step_impl(context):
    context.r = ray(point(0, -1, -2), vector(0, 1, 0))


@when(u'xs ← local_intersect(t, r)')
def step_impl(context):
    context.xs = context.t.local_intersect(context.t, context.r)


@given(u'r ← ray(point(1, 1, -2), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(1, 1, -2), vector(0, 0, 1))


@given(u'r ← ray(point(-1, 1, -2), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(-1, 1, -2), vector(0, 0, 1))


@given(u'r ← ray(point(0, -1, -2), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, -1, -2), vector(0, 0, 1))


@given(u'r ← ray(point(0, 0.5, -2), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0.5, -2), vector(0, 0, 1))


@then(u'xs[0].t = 2')
def step_impl(context):
    assert context.xs[0].t == 2
