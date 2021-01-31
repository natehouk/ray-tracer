from math import pi, sqrt

from behave import *

from group import add_child, group
from matrix import inverse, rotation_y, scaling, translation
from shape import (
    intersect,
    normal_at,
    normal_to_world,
    set_transform,
    test_shape,
    world_to_object,
)
from tuple import point, vector


@given(u"s ← test_shape()")
def step_impl(context):
    context.s = test_shape()


@when(u"set_transform(s, translation(2, 3, 4))")
def step_impl(context):
    set_transform(context.s, translation(2, 3, 4))


@then(u"s.transform = translation(2, 3, 4)")
def step_impl(context):
    assert context.s.transform == translation(2, 3, 4)


@then(u"s.saved_ray.origin = point(0, 0, -2.5)")
def step_impl(context):
    context.s.saved_ray.origin = point(0, 0, -2.5)


@then(u"s.saved_ray.direction = vector(0, 0, 0.5)")
def step_impl(context):
    context.s.saved_ray.direction = vector(0, 0, 0.5)


@then(u"s.saved_ray.origin = point(-5, 0, -5)")
def step_impl(context):
    assert context.s.saved_ray.origin == point(-5, 0, -5)


@then(u"s.saved_ray.direction = vector(0, 0, 1)")
def step_impl(context):
    assert context.s.saved_ray.direction == vector(0, 0, 1)


@when(u"set_transform(s, translation(0, 1, 0))")
def step_impl(context):
    set_transform(context.s, translation(0, 1, 0))


@when(u"set_transform(s, m)")
def step_impl(context):
    set_transform(context.s, context.m)


@when(u"xs ← intersect(s, r)")
def step_impl(context):
    context.xs = intersect(context.s, context.r)


@when(u"n ← normal_at(s, point(0, 1.70711, -0.70711))")
def step_impl(context):
    context.n = normal_at(context.s, point(0, 1.70711, -0.70711))


@when(u"n ← normal_at(s, point(0, √2/2, -√2/2))")
def step_impl(context):
    context.n = normal_at(context.s, point(0, sqrt(2) / 2, -sqrt(2) / 2))


@then(u"s.parent is nothing")
def step_impl(context):
    assert context.s.parent is None


@given(u"g1 ← group()")
def step_impl(context):
    context.g1 = group()


@given(u"set_transform(g1, rotation_y(π/2))")
def step_impl(context):
    set_transform(context.g1, rotation_y(pi / 2))


@given(u"g2 ← group()")
def step_impl(context):
    context.g2 = group()


@given(u"set_transform(g2, scaling(2, 2, 2))")
def step_impl(context):
    set_transform(context.g2, scaling(2, 2, 2))


@given(u"add_child(g1, g2)")
def step_impl(context):
    add_child(context.g1, context.g2)


@given(u"add_child(g2, s)")
def step_impl(context):
    add_child(context.g2, context.s)


@when(u"p ← world_to_object(s, point(-2, 0, -10))")
def step_impl(context):
    context.p = world_to_object(context.s, point(-2, 0, -10))


@then(u"p = point(0, 0, -1)")
def step_impl(context):
    assert context.p == point(0, 0, -1)


@given(u"set_transform(g2, scaling(1, 2, 3))")
def step_impl(context):
    set_transform(context.g2, scaling(1, 2, 3))


@when(u"n ← normal_to_world(s, vector(√3/3, √3/3, √3/3))")
def step_impl(context):
    context.n = normal_to_world(
        context.s, vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3)
    )


@when(u"n ← normal_at(s, point(1.7321, 1.1547, -5.5774))")
def step_impl(context):
    context.n = normal_at(context.s, point(1.7321, 1.1547, -5.5774))


@then(u"n = vector(0.2857, 0.4286, -0.8571)")
def step_impl(context):
    assert context.n == vector(0.2857, 0.4286, -0.8571)
