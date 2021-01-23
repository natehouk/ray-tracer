from behave import *

from cylinder import cylinder
from ray import ray
from tuple import normalize, point, vector
from util import equals


@given(u"cyl ← cylinder()")
def step_impl(context):
    context.cyl = cylinder()


@given(u"direction ← normalize(vector(0, 1, 0))")
def step_impl(context):
    context.direction = normalize(vector(0, 1, 0))


@given(u"r ← ray(point(1, 0, 0), direction)")
def step_impl(context):
    context.r = ray(point(1, 0, 0), context.direction)


@when(u"xs ← local_intersect(cyl, r)")
def step_impl(context):
    context.xs = context.cyl.local_intersect(context.cyl, context.r)


@given(u"r ← ray(point(0, 0, 0), direction)")
def step_impl(context):
    context.r = ray(point(0, 0, 0), context.direction)


@given(u"direction ← normalize(vector(1, 1, 1))")
def step_impl(context):
    context.direction = normalize(vector(1, 1, 1))


@given(u"r ← ray(point(0, 0, -5), direction)")
def step_impl(context):
    context.r = ray(point(0, 0, -5), context.direction)


@given(u"direction ← normalize(vector(0, 0, 1))")
def step_impl(context):
    context.direction = normalize(vector(0, 0, 1))


@given(u"r ← ray(point(1, 0, -5), direction)")
def step_impl(context):
    context.r = ray(point(1, 0, -5), context.direction)


@then(u"xs[0].t = 5")
def step_impl(context):
    assert context.xs[0].t == 5


@then(u"xs[1].t = 5")
def step_impl(context):
    assert context.xs[1].t == 5


@given(u"direction ← normalize(vector(0.1, 1, 1))")
def step_impl(context):
    context.direction = normalize(vector(0.1, 1, 1))


@given(u"r ← ray(point(0.5, 0, -5), direction)")
def step_impl(context):
    context.r = ray(point(0.5, 0, -5), context.direction)


@then(u"xs[0].t = 6.80798")
def step_impl(context):
    assert equals(context.xs[0].t, 6.80798)


@then(u"xs[1].t = 7.08872")
def step_impl(context):
    assert equals(context.xs[1].t, 7.08872)


@when(u"n ← local_normal_at(cyl, point(1, 0, 0))")
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(1, 0, 0))


@when(u"n ← local_normal_at(cyl, point(0, 5, -1))")
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0, 5, -1))


@then(u"n = vector(0, 0, -1)")
def step_impl(context):
    assert context.n == vector(0, 0, -1)


@when(u"n ← local_normal_at(cyl, point(0, -2, 1))")
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0, -2, 1))


@when(u"n ← local_normal_at(cyl, point(-1, 1, 0))")
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(-1, 1, 0))


@then(u"n = vector(-1, 0, 0)")
def step_impl(context):
    assert context.n == vector(-1, 0, 0)


@then(u'cyl.minimum = -infinity')
def step_impl(context):
    assert context.cyl.minimum == -float('inf')


@then(u'cyl.maximum = infinity')
def step_impl(context):
    assert context.cyl.maximum == float('inf')


@given(u'cyl.minimum ← 1')
def step_impl(context):
    context.cyl.minimum = 1


@given(u'cyl.maximum ← 2')
def step_impl(context):
    context.cyl.maximum = 2


@given(u'direction ← normalize(vector(0.1, 1, 0))')
def step_impl(context):
    context.direction = normalize(vector(0.1, 1, 0))


@given(u'r ← ray(point(0, 1.5, 0), direction)')
def step_impl(context):
    context.r = ray(point(0, 1.5, 0), context.direction)


@given(u'r ← ray(point(0, 3, -5), direction)')
def step_impl(context):
    context.r = ray(point(0, 3, -5), context.direction)


@given(u'r ← ray(point(0, 2, -5), direction)')
def step_impl(context):
    context.r = ray(point(0, 2, -5), context.direction)


@given(u'r ← ray(point(0, 1, -5), direction)')
def step_impl(context):
    context.r = ray(point(0, 1, -5), context.direction)


@given(u'r ← ray(point(0, 1.5, -2), direction)')
def step_impl(context):
    context.r = ray(point(0, 1.5, -2), context.direction)


@then(u'cyl.closed = false')
def step_impl(context):
    assert context.cyl.closed == False


@given(u'cyl.closed ← true')
def step_impl(context):
    context.cyl.closed = True


@given(u'direction ← normalize(vector(0, -1, 0))')
def step_impl(context):
    context.direction = normalize(vector(0, -1, 0))


@given(u'r ← ray(point(0, 3, 0), direction)')
def step_impl(context):
    context.r = ray(point(0, 3, 0), context.direction)


@given(u'direction ← normalize(vector(0, -1, 2))')
def step_impl(context):
    context.direction = normalize(vector(0, -1, 2))


@given(u'r ← ray(point(0, 3, -2), direction)')
def step_impl(context):
    context.r = ray(point(0, 3, -2), context.direction)


@given(u'direction ← normalize(vector(0, -1, 1))')
def step_impl(context):
    context.direction = normalize(vector(0, -1, 1))


@given(u'r ← ray(point(0, 4, -2), direction)')
def step_impl(context):
    context.r = ray(point(0, 4, -2), context.direction)


@given(u'direction ← normalize(vector(0, 1, 2))')
def step_impl(context):
    context.direction = normalize(vector(0, 1, 2))


@given(u'r ← ray(point(0, 0, -2), direction)')
def step_impl(context):
    context.r = ray(point(0, 0, -2), context.direction)


@given(u'direction ← normalize(vector(0, 1, 1))')
def step_impl(context):
    context.direction = normalize(vector(0, 1, 1))


@given(u'r ← ray(point(0, -1, -2), direction)')
def step_impl(context):
    context.r = ray(point(0, -1, -2), context.direction)


@when(u'n ← local_normal_at(cyl, point(0, 1, 0))')
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0, 1, 0))


@then(u'n = vector(0, -1, 0)')
def step_impl(context):
    assert context.n == vector(0, -1, 0)


@when(u'n ← local_normal_at(cyl, point(0.5, 1, 0))')
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0.5, 1, 0))


@when(u'n ← local_normal_at(cyl, point(0, 1, 0.5))')
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0, 1, 0.5))


@when(u'n ← local_normal_at(cyl, point(0, 2, 0))')
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0, 2, 0))


@when(u'n ← local_normal_at(cyl, point(0.5, 2, 0))')
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0.5, 2, 0))


@when(u'n ← local_normal_at(cyl, point(0, 2, 0.5))')
def step_impl(context):
    context.n = context.cyl.local_normal_at(context.cyl, point(0, 2, 0.5))