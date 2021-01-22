from math import sqrt

from behave import *

from matrix import translation
from shape import intersect, normal_at, set_transform, test_shape
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
