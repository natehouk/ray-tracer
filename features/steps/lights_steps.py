from behave import *
from tuple import color, point, point_light

@given(u'intensity ← color(1, 1, 1)')
def step_impl(context):
    context.intensity = color(1, 1, 1)


@given(u'position ← point(0, 0, 0)')
def step_impl(context):
    context.position = point(0, 0, 0)


@when(u'light ← point_light(position, intensity)')
def step_impl(context):
    context.light = point_light(context.position, context.intensity)


@then(u'light.position = position')
def step_impl(context):
    assert context.light.position == context.position


@then(u'light.intensity = intensity')
def step_impl(context):
    assert context.light.intensity == context.intensity
