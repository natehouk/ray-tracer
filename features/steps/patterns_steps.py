from behave import *

from matrix import identity_matrix, scaling, translation
from pattern import (
    checkers_pattern,
    gradient_pattern,
    pattern_at_shape,
    ring_pattern,
    set_pattern_transform,
    stripe_pattern,
    test_pattern,
)
from shape import set_transform
from sphere import sphere
from tuple import color, point


@given(u"black ← color(0, 0, 0)")
def step_impl(context):
    context.black = color(0, 0, 0)


@given(u"white ← color(1, 1, 1)")
def step_impl(context):
    context.white = color(1, 1, 1)


@given(u"pattern ← stripe_pattern(white, black)")
def step_impl(context):
    context.pattern = stripe_pattern(context.white, context.black)


@then(u"pattern.a = white")
def step_impl(context):
    assert context.pattern.a == context.white


@then(u"pattern.b = black")
def step_impl(context):
    assert context.pattern.b == context.black


@then(u"stripe_at(pattern, point(0, 0, 0)) = white")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 0, 0)) == context.white


@then(u"stripe_at(pattern, point(0, 1, 0)) = white")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 1, 0)) == context.white


@then(u"stripe_at(pattern, point(0, 2, 0)) = white")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 2, 0)) == context.white


@then(u"stripe_at(pattern, point(0, 0, 1)) = white")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 0, 1)) == context.white


@then(u"stripe_at(pattern, point(0, 0, 2)) = white")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 0, 2)) == context.white


@then(u"stripe_at(pattern, point(0.9, 0, 0)) = white")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0.9, 0, 0)) == context.white
    )


@then(u"stripe_at(pattern, point(1, 0, 0)) = black")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(1, 0, 0)) == context.black


@then(u"stripe_at(pattern, point(-0.1, 0, 0)) = black")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(-0.1, 0, 0)) == context.black
    )


@then(u"stripe_at(pattern, point(-1, 0, 0)) = black")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(-1, 0, 0)) == context.black


@then(u"stripe_at(pattern, point(-1.1, 0, 0)) = white")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(-1.1, 0, 0)) == context.white
    )


@given(u"object ← sphere()")
def step_impl(context):
    context.object = sphere()


@given(u"set_transform(object, scaling(2, 2, 2))")
def step_impl(context):
    set_transform(context.object, scaling(2, 2, 2))


@when(u"c ← stripe_at_object(pattern, object, point(1.5, 0, 0))")
def step_impl(context):
    context.c = pattern_at_shape(context.pattern, context.object, point(1.5, 0, 0))


@then(u"c = white")
def step_impl(context):
    assert context.c == context.white


@given(u"set_pattern_transform(pattern, scaling(2, 2, 2))")
def step_impl(context):
    set_pattern_transform(context.pattern, scaling(2, 2, 2))


@given(u"set_pattern_transform(pattern, translation(0.5, 0, 0))")
def step_impl(context):
    set_pattern_transform(context.pattern, translation(0.5, 0, 0))


@when(u"c ← stripe_at_object(pattern, object, point(2.5, 0, 0))")
def step_impl(context):
    context.c = pattern_at_shape(context.pattern, context.object, point(2.5, 0, 0))


@given(u"pattern ← test_pattern()")
def step_impl(context):
    context.pattern = test_pattern()


@then(u"pattern.transform = identity_matrix")
def step_impl(context):
    assert context.pattern.transform == identity_matrix()


@when(u"set_pattern_transform(pattern, translation(1, 2, 3))")
def step_impl(context):
    set_pattern_transform(context.pattern, translation(1, 2, 3))


@then(u"pattern.transform = translation(1, 2, 3)")
def step_impl(context):
    assert context.pattern.transform == translation(1, 2, 3)


@given(u"set_transform(shape, scaling(2, 2, 2))")
def step_impl(context):
    set_transform(context.shape, scaling(2, 2, 2))


@when(u"c ← pattern_at_shape(pattern, shape, point(2, 3, 4))")
def step_impl(context):
    context.c = pattern_at_shape(context.pattern, context.shape, point(2, 3, 4))


@then(u"c = color(1, 1.5, 2)")
def step_impl(context):
    print(context.c)
    assert context.c == color(1, 1.5, 2)


@given(u"set_pattern_transform(pattern, translation(0.5, 1, 1.5))")
def step_impl(context):
    set_pattern_transform(context.pattern, translation(0.5, 1, 1.5))


@when(u"c ← pattern_at_shape(pattern, shape, point(2.5, 3, 3.5))")
def step_impl(context):
    context.c = pattern_at_shape(context.pattern, context.shape, point(2.5, 3, 3.5))


@then(u"c = color(0.75, 0.5, 0.25)")
def step_impl(context):
    print(context.c)
    assert context.c == color(0.75, 0.5, 0.25)


@given(u"pattern ← gradient_pattern(white, black)")
def step_impl(context):
    context.pattern = gradient_pattern(context.white, context.black)


@then(u"pattern_at(pattern, point(0, 0, 0)) = white")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 0, 0)) == context.white


@then(u"pattern_at(pattern, point(0.25, 0, 0)) = color(0.75, 0.75, 0.75)")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0.25, 0, 0)) == color(
        0.75, 0.75, 0.75
    )


@then(u"pattern_at(pattern, point(0.5, 0, 0)) = color(0.5, 0.5, 0.5)")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0.5, 0, 0)) == color(
        0.5, 0.5, 0.5
    )


@then(u"pattern_at(pattern, point(0.75, 0, 0)) = color(0.25, 0.25, 0.25)")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0.75, 0, 0)) == color(
        0.25, 0.25, 0.25
    )


@given(u"pattern ← ring_pattern(white, black)")
def step_impl(context):
    context.pattern = ring_pattern(context.white, context.black)


@then(u"pattern_at(pattern, point(1, 0, 0)) = black")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(1, 0, 0)) == context.black


@then(u"pattern_at(pattern, point(0, 0, 1)) = black")
def step_impl(context):
    assert context.pattern.pattern_at(context.pattern, point(0, 0, 1)) == context.black


@then(u"pattern_at(pattern, point(0.708, 0, 0.708)) = black")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0.708, 0, 0.708))
        == context.black
    )


@given(u"pattern ← checkers_pattern(white, black)")
def step_impl(context):
    context.pattern = checkers_pattern(context.white, context.black)


@then(u"pattern_at(pattern, point(0.99, 0, 0)) = white")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0.99, 0, 0)) == context.white
    )


@then(u"pattern_at(pattern, point(1.01, 0, 0)) = black")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(1.01, 0, 0)) == context.black
    )


@then(u"pattern_at(pattern, point(0, 0.99, 0)) = white")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0, 0.99, 0)) == context.white
    )


@then(u"pattern_at(pattern, point(0, 1.01, 0)) = black")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0, 1.01, 0)) == context.black
    )


@then(u"pattern_at(pattern, point(0, 0, 0.99)) = white")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0, 0, 0.99)) == context.white
    )


@then(u"pattern_at(pattern, point(0, 0, 1.01)) = black")
def step_impl(context):
    assert (
        context.pattern.pattern_at(context.pattern, point(0, 0, 1.01)) == context.black
    )
