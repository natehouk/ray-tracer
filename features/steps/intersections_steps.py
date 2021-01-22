from math import sqrt

from behave import *

from matrix import scaling, translation
from plane import plane
from ray import ray
from sphere import (
    glass_sphere,
    hit,
    intersection,
    intersections,
    prepare_computations,
    sphere,
)
from world import schlick
from tuple import EPSILON, point, vector, equals


@when(u"i ← intersection(3.5, s)")
def step_impl(context):
    context.i = intersection(3.5, context.s)


@then(u"i.t = 3.5")
def step_impl(context):
    assert context.i.t == 3.5


@then(u"i.object = s")
def step_impl(context):
    assert context.i.object == context.s


@given(u"shape ← sphere()")
def step_impl(context):
    context.shape = sphere()


@given(u"i ← intersection(4, shape)")
def step_impl(context):
    context.i = intersection(4, context.shape)


@when(u"comps ← prepare_computations(i, r)")
def step_impl(context):
    context.comps = prepare_computations(context.i, context.r)


@then(u"comps.t = i.t")
def step_impl(context):
    assert context.comps.t == context.i.t


@then(u"comps.object = i.object")
def step_impl(context):
    assert context.comps.object == context.i.object


@then(u"comps.point = point(0, 0, -1)")
def step_impl(context):
    assert context.comps.point == point(0, 0, -1)


@then(u"comps.eyev = vector(0, 0, -1)")
def step_impl(context):
    assert context.comps.eyev == vector(0, 0, -1)


@then(u"comps.normalv = vector(0, 0, -1)")
def step_impl(context):
    assert context.comps.normalv == vector(0, 0, -1)


@given(u"shape ← plane()")
def step_impl(context):
    context.shape = plane()


@given(u"r ← ray(point(0, 1, -1), vector(0, -√2/2, √2/2))")
def step_impl(context):
    context.r = ray(point(0, 1, -1), vector(0, -sqrt(2) / 2, sqrt(2) / 2))


@given(u"i ← intersection(√2, shape)")
def step_impl(context):
    context.i = intersection(sqrt(2), context.shape)


@then(u"comps.reflectv = vector(0, √2/2, √2/2)")
def step_impl(context):
    assert context.comps.reflectv == vector(0, sqrt(2) / 2, sqrt(2) / 2)


@then(u"comps.inside = false")
def step_impl(context):
    assert context.comps.inside == False


@given(u"i ← intersection(1, shape)")
def step_impl(context):
    context.i = intersection(1, context.shape)


@then(u"comps.point = point(0, 0, 1)")
def step_impl(context):
    assert context.comps.point == point(0, 0, 1)


@then(u"comps.inside = true")
def step_impl(context):
    assert context.comps.inside == True


@given(u"shape ← sphere() with")
def step_impl(context):
    context.shape = sphere()
    context.shape.transform = translation(0, 0, 1)


@given(u"i ← intersection(5, shape)")
def step_impl(context):
    context.i = intersection(5, context.shape)


@then(u"comps.over_point.z < -EPSILON/2")
def step_impl(context):
    print(context.comps.over_point.z)
    assert context.comps.over_point.z < -EPSILON / 2


@then(u"comps.point.z > comps.over_point.z")
def step_impl(context):
    assert context.comps.point.z > context.comps.over_point.z


@given(u"shape ← glass_sphere() with")
def step_impl(context):
    context.shape = glass_sphere()
    context.shape.transform = translation(0, 0, 1)


@given(u"xs ← intersections(i)")
def step_impl(context):
    context.xs = intersections(context.i)


@when(u"comps ← prepare_computations(i, r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.i, context.r, context.xs)


@then(u"comps.under_point.z > EPSILON/2")
def step_impl(context):
    assert context.comps.under_point.z > EPSILON / 2


@then(u"comps.point.z < comps.under_point.z")
def step_impl(context):
    assert context.comps.point.z < context.comps.under_point.z


@given(u"i1 ← intersection(1, s)")
def step_impl(context):
    context.i1 = intersection(1, context.s)


@given(u"i2 ← intersection(2, s)")
def step_impl(context):
    context.i2 = intersection(2, context.s)


@when(u"xs ← intersections(i1, i2)")
def step_impl(context):
    context.xs = intersections(context.i1, context.i2)


@then(u"xs[0].t = 1")
def step_impl(context):
    assert context.xs[0].t == 1


@then(u"xs[1].t = 2")
def step_impl(context):
    assert context.xs[1].t == 2


@given(u"xs ← intersections(i2, i1)")
def step_impl(context):
    context.xs = intersections(context.i2, context.i1)


@when(u"i ← hit(xs)")
def step_impl(context):
    context.i = hit(context.xs)


@then(u"i = i1")
def step_impl(context):
    assert context.i == context.i1


@given(u"i1 ← intersection(-1, s)")
def step_impl(context):
    context.i1 = intersection(-1, context.s)


@given(u"i2 ← intersection(1, s)")
def step_impl(context):
    context.i2 = intersection(1, context.s)


@then(u"i = i2")
def step_impl(context):
    assert context.i == context.i2


@given(u"i1 ← intersection(-2, s)")
def step_impl(context):
    context.i1 = intersection(-2, context.s)


@given(u"i2 ← intersection(-1, s)")
def step_impl(context):
    context.i2 = intersection(-1, context.s)


@then(u"i is nothing")
def step_impl(context):
    context.i is None


@given(u"i1 ← intersection(5, s)")
def step_impl(context):
    context.i1 = intersection(5, context.s)


@given(u"i2 ← intersection(7, s)")
def step_impl(context):
    context.i2 = intersection(7, context.s)


@given(u"i3 ← intersection(-3, s)")
def step_impl(context):
    context.i3 = intersection(-3, context.s)


@given(u"i4 ← intersection(2, s)")
def step_impl(context):
    context.i4 = intersection(2, context.s)


@given(u"xs ← intersections(i1, i2, i3, i4)")
def step_impl(context):
    context.xs = intersections(context.i1, context.i2, context.i3, context.i4)


@then(u"i = i4")
def step_impl(context):
    assert context.i == context.i4


@given(u"A ← glass_sphere() with")
def step_impl(context):
    context.A = glass_sphere()
    context.A.transform = scaling(2, 2, 2)
    context.A.material.refractive_index = 1.5


@given(u"B ← glass_sphere() with")
def step_impl(context):
    context.B = glass_sphere()
    context.B.transform = translation(0, 0, -0.25)
    context.B.material.refractive_index = 2.0


@given(u"C ← glass_sphere() with")
def step_impl(context):
    context.C = glass_sphere()
    context.C.transform = translation(0, 0, 0.25)
    context.C.material.refractive_index = 2.5


@given(u"r ← ray(point(0, 0, -4), vector(0, 0, 1))")
def step_impl(context):
    context.r = ray(point(0, 0, -4), vector(0, 0, 1))


@given(u"xs ← intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)")
def step_impl(context):
    context.xs = intersections(
        intersection(2, context.A),
        intersection(2.75, context.B),
        intersection(3.25, context.C),
        intersection(4.75, context.B),
        intersection(5.25, context.C),
        intersection(6, context.A),
    )


@when(u"comps ← prepare_computations(xs[0], r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.xs[0], context.r, context.xs)


@then(u"comps.n1 = 1.0")
def step_impl(context):
    assert context.comps.n1 == 1.0


@then(u"comps.n2 = 1.5")
def step_impl(context):
    assert context.comps.n2 == 1.5


@when(u"comps ← prepare_computations(xs[1], r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.xs[1], context.r, context.xs)


@then(u"comps.n1 = 1.5")
def step_impl(context):
    assert context.comps.n1 == 1.5


@then(u"comps.n2 = 2.0")
def step_impl(context):
    assert context.comps.n2 == 2.0


@when(u"comps ← prepare_computations(xs[2], r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.xs[2], context.r, context.xs)


@then(u"comps.n1 = 2.0")
def step_impl(context):
    assert context.comps.n1 == 2.0


@then(u"comps.n2 = 2.5")
def step_impl(context):
    assert context.comps.n2 == 2.5


@when(u"comps ← prepare_computations(xs[3], r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.xs[3], context.r, context.xs)


@then(u"comps.n1 = 2.5")
def step_impl(context):
    assert context.comps.n1 == 2.5


@when(u"comps ← prepare_computations(xs[4], r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.xs[4], context.r, context.xs)


@when(u"comps ← prepare_computations(xs[5], r, xs)")
def step_impl(context):
    context.comps = prepare_computations(context.xs[5], context.r, context.xs)


@then(u"comps.n2 = 1.0")
def step_impl(context):
    assert context.comps.n2 == 1.0


@given(u'shape ← glass_sphere()')
def step_impl(context):
    context.shape = glass_sphere()


@when(u'reflectance ← schlick(comps)')
def step_impl(context):
    context.reflectance = schlick(context.comps)


@then(u'reflectance = 1.0')
def step_impl(context):
    assert context.reflectance == 1.0


@given(u'xs ← intersections(-1:shape, 1:shape)')
def step_impl(context):
    context.xs = intersections(intersection(-1, context.shape), intersection(1, context.shape))


@then(u'reflectance = 0.04')
def step_impl(context):
    assert equals(context.reflectance, 0.04)


@given(u'r ← ray(point(0, 0.99, -2), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0.99, -2), vector(0, 0, 1))


@given(u'xs ← intersections(1.8589:shape)')
def step_impl(context):
    context.xs = intersections(intersection(1.8589, context.shape))


@then(u'reflectance = 0.48873')
def step_impl(context):
    assert equals(context.reflectance, 0.48873)


# @given(u's ← triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))')
# def step_impl(context):
#     context.s = triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))


# @when(u'i ← intersection_with_uv(3.5, s, 0.2, 0.4)')
# def step_impl(context):
#     context.i = intersection_with_uv(3.5, context.s, 0.2, 0.4)


# @then(u'i.u = 0.2')
# def step_impl(context):
#     assert context.i.u == 0.2


# @then(u'i.v = 0.4')
# def step_impl(context):
#     assert context.i.v == 0.4
