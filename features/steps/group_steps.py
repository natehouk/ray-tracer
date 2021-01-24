from behave import *
from group import group, add_child
from matrix import identity_matrix, translation
from sphere import sphere
from tuple import point, vector
from ray import ray
from shape import set_transform

@given(u'g ← group()')
def step_impl(context):
    context.g = group()


@then(u'g.transform = identity_matrix')
def step_impl(context):
    assert context.g.transform == identity_matrix()


@then(u'g is empty')
def step_impl(context):
    assert len(context.g.children) == 0


@when(u'add_child(g, s)')
def step_impl(context):
    add_child(context.g, context.s)


@then(u'g is not empty')
def step_impl(context):
    assert len(context.g.children) != 0


@then(u'g includes s')
def step_impl(context):
    assert context.s in context.g.children


@then(u's.parent = g')
def step_impl(context):
    assert context.s.parent == context.g


@when(u'xs ← local_intersect(g, r)')
def step_impl(context):
    context.xs = context.g.local_intersect(context.g, context.r)


@given(u's2 ← sphere()')
def step_impl(context):
    context.s2 = sphere()


@given(u'set_transform(s2, translation(0, 0, -3))')
def step_impl(context):
    set_transform(context.s2, translation(0, 0, -3))


@given(u's3 ← sphere()')
def step_impl(context):
    context.s3 = sphere()


@given(u'set_transform(s3, translation(5, 0, 0))')
def step_impl(context):
    set_transform(context.s3, translation(5, 0, 0))


@given(u'add_child(g, s1)')
def step_impl(context):
    add_child(context.g, context.s1)


@given(u'add_child(g, s2)')
def step_impl(context):
    add_child(context.g, context.s2)


@given(u'add_child(g, s3)')
def step_impl(context):
    add_child(context.g, context.s3)


@when(u'r ← ray(point(0, 0, -5), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0, -5), vector(0, 0, 1))


@then(u'xs[0].object = s2')
def step_impl(context):
    assert context.xs[0].object == context.s2


@then(u'xs[1].object = s2')
def step_impl(context):
    assert context.xs[1].object == context.s2


@then(u'xs[2].object = s1')
def step_impl(context):
    assert context.xs[2].object == context.s1


@then(u'xs[3].object = s1')
def step_impl(context):
    assert context.xs[3].object == context.s1
