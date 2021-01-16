from behave import *
from math import sqrt
from material import material
from tuple import color, point, vector, point_light
from material import lighting

@given(u'm ← material()')
def step_impl(context):
    context.m = material()


@then(u'm.color = color(1, 1, 1)')
def step_impl(context):
    assert context.m.color == color(1, 1, 1)


@then(u'm.ambient = 0.1')
def step_impl(context):
    assert context.m.ambient == 0.1


@then(u'm.diffuse = 0.9')
def step_impl(context):
    assert context.m.diffuse == 0.9


@then(u'm.specular = 0.9')
def step_impl(context):
    assert context.m.specular == 0.9


@then(u'm.shininess = 200.0')
def step_impl(context):
    assert context.m.shininess == 200.0


@given(u'eyev ← vector(0, 0, -1)')
def step_impl(context):
    context.eyev = vector(0, 0, -1)


@given(u'normalv ← vector(0, 0, -1)')
def step_impl(context):
    context.normalv = vector(0, 0, -1)


@given(u'light ← point_light(point(0, 0, -10), color(1, 1, 1))')
def step_impl(context):
    context.light = point_light(point(0, 0, -10), color(1, 1, 1))


@when(u'result ← lighting(m, light, position, eyev, normalv)')
def step_impl(context):
    context.result = lighting(context.m, context.light, context.position, context.eyev, context.normalv)


@then(u'result = color(1.9, 1.9, 1.9)')
def step_impl(context):
    assert context.result == color(1.9, 1.9, 1.9)


@given(u'eyev ← vector(0, √2/2, -√2/2)')
def step_impl(context):
    context.eyev = vector(0, sqrt(2)/2, -sqrt(2)/2)


@then(u'result = color(1.0, 1.0, 1.0)')
def step_impl(context):
    assert context.result == color(1.0, 1.0, 1.0)


@given(u'light ← point_light(point(0, 10, -10), color(1, 1, 1))')
def step_impl(context):
    context.light = point_light(point(0, 10, -10), color(1, 1, 1))


@then(u'result = color(0.7364, 0.7364, 0.7364)')
def step_impl(context):
    assert context.result == color(0.7364, 0.7364, 0.7364)


@given(u'eyev ← vector(0, -√2/2, -√2/2)')
def step_impl(context):
    context.eyev = vector(0, -sqrt(2)/2, -sqrt(2)/2)


@then(u'result = color(1.6364, 1.6364, 1.6364)')
def step_impl(context):
    assert context.result == color(1.6364, 1.6364, 1.6364)


@given(u'light ← point_light(point(0, 0, 10), color(1, 1, 1))')
def step_impl(context):
    context.light = point_light(point(0, 0, 10), color(1, 1, 1))


@then(u'result = color(0.1, 0.1, 0.1)')
def step_impl(context):
    assert context.result == color(0.1, 0.1, 0.1)


@given(u'in_shadow ← true')
def step_impl(context):
    context.in_shadow = True


@when(u'result ← lighting(m, light, position, eyev, normalv, in_shadow)')
def step_impl(context):
    context.result = lighting(context.m, context.light, context.position, context.eyev, context.normalv, context.in_shadow)