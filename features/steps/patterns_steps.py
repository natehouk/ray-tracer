from behave import *
from tuple import color, point
from matrix import scaling, translation
from shape import set_transform
from pattern import stripe_pattern, stripe_at, stripe_at_object, set_pattern_transform
from sphere import sphere

@given(u'black ← color(0, 0, 0)')
def step_impl(context):
    context.black = color(0, 0, 0)


@given(u'white ← color(1, 1, 1)')
def step_impl(context):
    context.white = color(1, 1, 1)


@given(u'pattern ← stripe_pattern(white, black)')
def step_impl(context):
    context.pattern = stripe_pattern(context.white, context.black)


@then(u'pattern.a = white')
def step_impl(context):
    assert context.pattern.a == context.white


@then(u'pattern.b = black')
def step_impl(context):
    assert context.pattern.b == context.black


@then(u'stripe_at(pattern, point(0, 0, 0)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(0, 0, 0)) == context.white


@then(u'stripe_at(pattern, point(0, 1, 0)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(0, 1, 0)) == context.white


@then(u'stripe_at(pattern, point(0, 2, 0)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(0, 2, 0)) == context.white


@then(u'stripe_at(pattern, point(0, 0, 1)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(0, 0, 1)) == context.white


@then(u'stripe_at(pattern, point(0, 0, 2)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(0, 0, 2)) == context.white


@then(u'stripe_at(pattern, point(0.9, 0, 0)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(0.9, 0, 0)) == context.white


@then(u'stripe_at(pattern, point(1, 0, 0)) = black')
def step_impl(context):
    assert stripe_at(context.pattern, point(1, 0, 0)) == context.black


@then(u'stripe_at(pattern, point(-0.1, 0, 0)) = black')
def step_impl(context):
    assert stripe_at(context.pattern, point(-0.1, 0, 0)) == context.black


@then(u'stripe_at(pattern, point(-1, 0, 0)) = black')
def step_impl(context):
    assert stripe_at(context.pattern, point(-1, 0, 0)) == context.black


@then(u'stripe_at(pattern, point(-1.1, 0, 0)) = white')
def step_impl(context):
    assert stripe_at(context.pattern, point(-1.1, 0, 0)) == context.white


@given(u'object ← sphere()')
def step_impl(context):
    context.object = sphere()


@given(u'set_transform(object, scaling(2, 2, 2))')
def step_impl(context):
    set_transform(context.object, scaling(2, 2, 2))


@when(u'c ← stripe_at_object(pattern, object, point(1.5, 0, 0))')
def step_impl(context):
    context.c = stripe_at_object(context.pattern, context.object, point(1.5, 0, 0))


@then(u'c = white')
def step_impl(context):
    assert context.c == context.white


@given(u'set_pattern_transform(pattern, scaling(2, 2, 2))')
def step_impl(context):
    set_pattern_transform(context.pattern, scaling(2, 2, 2))


@given(u'set_pattern_transform(pattern, translation(0.5, 0, 0))')
def step_impl(context):
    set_pattern_transform(context.pattern, translation(0.5, 0, 0))


@when(u'c ← stripe_at_object(pattern, object, point(2.5, 0, 0))')
def step_impl(context):
    context.c = stripe_at_object(context.pattern, context.object, point(2.5, 0, 0))
