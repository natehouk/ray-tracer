from behave import *
from world import world, default_world, intersect_world
from tuple import point, color, point_light
from sphere import sphere
from matrix import scaling

@given(u'w ← world()')
def step_impl(context):
    context.w = world()


@then(u'w contains no objects')
def step_impl(context):
    assert len(context.w.objects) == 0


@then(u'w has no light source')
def step_impl(context):
    assert context.w.light == None


@given(u'light ← point_light(point(-10, 10, -10), color(1, 1, 1))')
def step_impl(context):
    context.light = point_light(point(-10, 10, -10), color(1, 1, 1))


@given(u's1 ← sphere() with')
def step_impl(context):
    context.s1 = sphere()
    context.s1.material.color = color(0.8, 1.0, 0.6)
    context.s1.material.diffuse = 0.7
    context.s1.material.specular = 0.2


@given(u's2 ← sphere() with')
def step_impl(context):
    context.s2 = sphere()
    context.s2.transform = scaling(0.5, 0.5, 0.5)


@when(u'w ← default_world()')
def step_impl(context):
    context.w = default_world()


@then(u'w.light = light')
def step_impl(context):
    assert context.w.light == context.light


@then(u'w contains s1')
def step_impl(context):
    assert context.s1 in context.w.objects


@then(u'w contains s2')
def step_impl(context):
    assert context.s2 in context.w.objects


@given(u'w ← default_world()')
def step_impl(context):
    context.w = default_world()


@when(u'xs ← intersect_world(w, r)')
def step_impl(context):
    context.xs = intersect_world(context.w, context.r)


@then(u'xs.count = 4')
def step_impl(context):
    assert len(context.xs) == 4


@then(u'xs[0].t = 4')
def step_impl(context):
    assert context.xs[0].t == 4


@then(u'xs[1].t = 4.5')
def step_impl(context):
    assert context.xs[1].t == 4.5


@then(u'xs[2].t = 5.5')
def step_impl(context):
    assert context.xs[2].t == 5.5


@then(u'xs[3].t = 6')
def step_impl(context):
    assert context.xs[3].t == 6
