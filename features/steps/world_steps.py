from math import sqrt

from behave import *

from matrix import scaling, translation
from pattern import test_pattern
from plane import plane
from ray import ray
from sphere import intersection, intersections, sphere
from tuple import color, point, point_light, vector
from world import (
    LIMIT,
    color_at,
    default_world,
    intersect_world,
    is_shadowed,
    reflected_color,
    refracted_color,
    shade_hit,
    world,
)


@given(u"w ← world()")
def step_impl(context):
    context.w = world()


@then(u"w contains no objects")
def step_impl(context):
    assert len(context.w.objects) == 0


@then(u"w has no light source")
def step_impl(context):
    assert context.w.light == None


@given(u"light ← point_light(point(-10, 10, -10), color(1, 1, 1))")
def step_impl(context):
    context.light = point_light(point(-10, 10, -10), color(1, 1, 1))


@given(u"s1 ← sphere() with")
def step_impl(context):
    context.s1 = sphere()
    context.s1.material.color = color(0.8, 1.0, 0.6)
    context.s1.material.diffuse = 0.7
    context.s1.material.specular = 0.2


@given(u"s2 ← sphere() with")
def step_impl(context):
    context.s2 = sphere()
    context.s2.transform = scaling(0.5, 0.5, 0.5)


@when(u"w ← default_world()")
def step_impl(context):
    context.w = default_world()


@then(u"w.light = light")
def step_impl(context):
    assert context.w.light == context.light


@then(u"w contains s1")
def step_impl(context):
    assert context.s1 in context.w.objects


@then(u"w contains s2")
def step_impl(context):
    assert context.s2 in context.w.objects


@given(u"w ← default_world()")
def step_impl(context):
    context.w = default_world()


@when(u"xs ← intersect_world(w, r)")
def step_impl(context):
    context.xs = intersect_world(context.w, context.r)


@then(u"xs.count = 4")
def step_impl(context):
    assert len(context.xs) == 4


@then(u"xs[0].t = 4")
def step_impl(context):
    assert context.xs[0].t == 4


@then(u"xs[1].t = 4.5")
def step_impl(context):
    print(context.xs[0].t)
    print(context.xs[1].t)
    print(context.xs[2].t)
    print(context.xs[3].t)
    print("FDSFS")
    assert context.xs[1].t == 4.5


@then(u"xs[2].t = 5.5")
def step_impl(context):
    print(context.xs[2].t)
    assert context.xs[2].t == 5.5


@then(u"xs[3].t = 6")
def step_impl(context):
    assert context.xs[3].t == 6


@given(u"shape ← the first object in w")
def step_impl(context):
    context.shape = context.w.objects[0]


@when(u"c ← shade_hit(w, comps)")
def step_impl(context):
    context.c = shade_hit(context.w, context.comps)


@then(u"c = color(0.38066, 0.47583, 0.2855)")
def step_impl(context):
    print(context.c)
    assert context.c == color(0.38066, 0.47583, 0.2855)


@given(u"w.light ← point_light(point(0, 0.25, 0), color(1, 1, 1))")
def step_impl(context):
    context.w.light = point_light(point(0, 0.25, 0), color(1, 1, 1))


@given(u"shape ← the second object in w")
def step_impl(context):
    context.shape = context.w.objects[1]


@given(u"i ← intersection(0.5, shape)")
def step_impl(context):
    context.i = intersection(0.5, context.shape)


@then(u"c = color(0.90498, 0.90498, 0.90498)")
def step_impl(context):
    assert context.c == color(0.90498, 0.90498, 0.90498)


@given(u"r ← ray(point(0, 0, -5), vector(0, 1, 0))")
def step_impl(context):
    context.r = ray(point(0, 0, -5), vector(0, 1, 0))


@when(u"c ← color_at(w, r)")
def step_impl(context):
    context.c = color_at(context.w, context.r)


@then(u"c = color(0, 0, 0)")
def step_impl(context):
    assert context.c == color(0, 0, 0)


@given(u"outer ← the first object in w")
def step_impl(context):
    context.outer = context.w.objects[0]


@given(u"outer.material.ambient ← 1")
def step_impl(context):
    context.outer.material.ambient = 1


@given(u"inner ← the second object in w")
def step_impl(context):
    context.inner = context.w.objects[1]


@given(u"inner.material.ambient ← 1")
def step_impl(context):
    context.inner.material.ambient = 1


@given(u"r ← ray(point(0, 0, 0.75), vector(0, 0, -1))")
def step_impl(context):
    context.r = ray(point(0, 0, 0.75), vector(0, 0, -1))


@then(u"c = inner.material.color")
def step_impl(context):
    print(context.c)
    print(context.inner.material.color)
    assert context.c == context.inner.material.color


@given(u"p ← point(0, 10, 0)")
def step_impl(context):
    context.p = point(0, 10, 0)


@then(u"is_shadowed(w, p) is false")
def step_impl(context):
    assert is_shadowed(context.w, context.p) is False


@given(u"p ← point(10, -10, 10)")
def step_impl(context):
    context.p = point(10, -10, 10)


@then(u"is_shadowed(w, p) is true")
def step_impl(context):
    assert is_shadowed(context.w, context.p) is True


@given(u"p ← point(-20, 20, -20)")
def step_impl(context):
    context.p = point(-20, 20, -20)


@given(u"p ← point(-2, 2, -2)")
def step_impl(context):
    context.p = point(-2, 2, -2)


@given(u"w.light ← point_light(point(0, 0, -10), color(1, 1, 1))")
def step_impl(context):
    context.w.light = point_light(point(0, 0, -10), color(1, 1, 1))


@given(u"s1 ← sphere()")
def step_impl(context):
    context.s1 = sphere()


@given(u"s1 is added to w")
def step_impl(context):
    context.w.objects.append(context.s1)


@given(u"s2 is added to w")
def step_impl(context):
    context.w.objects.append(context.s2)


@given(u"i ← intersection(4, s2)")
def step_impl(context):
    context.i = intersection(4, context.s2)


@then(u"c = color(0.1, 0.1, 0.1)")
def step_impl(context):
    assert context.c == color(0.1, 0.1, 0.1)


@given(u"shape.material.ambient ← 1")
def step_impl(context):
    context.shape.material.ambient = 1


@when(u"color ← reflected_color(w, comps)")
def step_impl(context):
    context.color = reflected_color(context.w, context.comps)


@then(u"color = color(0, 0, 0)")
def step_impl(context):
    assert context.color == color(0, 0, 0)


@given(u"shape ← plane() with")
def step_impl(context):
    context.shape = plane()
    context.shape.material.reflective = 0.5
    context.shape.transform = translation(0, -1, 0)


@given(u"shape is added to w")
def step_impl(context):
    context.w.objects.append(context.shape)


@given(u"r ← ray(point(0, 0, -3), vector(0, -√2/2, √2/2))")
def step_impl(context):
    context.r = ray(point(0, 0, -3), vector(0, -sqrt(2) / 2, sqrt(2) / 2))


@then(u"color = color(0.19032, 0.2379, 0.14274)")
def step_impl(context):
    print(context.color)
    assert context.color == color(0.19032, 0.2379, 0.14274)


@when(u"color ← shade_hit(w, comps)")
def step_impl(context):
    context.color = shade_hit(context.w, context.comps)


@then(u"color = color(0.87677, 0.92436, 0.82918)")
def step_impl(context):
    assert context.color == color(0.87677, 0.92436, 0.82918)


@given(u"w.light ← point_light(point(0, 0, 0), color(1, 1, 1))")
def step_impl(context):
    context.w.light = point_light(point(0, 0, 0), color(1, 1, 1))


@given(u"lower ← plane() with")
def step_impl(context):
    context.lower = plane()
    context.lower.material.reflective = 1
    context.lower.material.transform = translation(0, -1, 0)


@given(u"lower is added to w")
def step_impl(context):
    context.w.objects.append(context.lower)


@given(u"upper ← plane() with")
def step_impl(context):
    context.upper = plane()
    context.upper.material.reflective = 1
    context.upper.material.transform = translation(0, 1, 0)


@given(u"upper is added to w")
def step_impl(context):
    context.w.objects.append(context.upper)


@given(u"r ← ray(point(0, 0, 0), vector(0, 1, 0))")
def step_impl(context):
    context.r = ray(point(0, 0, 0), vector(0, 1, 0))


@then(u"color_at(w, r) should terminate successfully")
def step_impl(context):
    assert color_at(context.w, context.r)


@when(u"color ← reflected_color(w, comps, 0)")
def step_impl(context):
    context.color = reflected_color(context.w, context.comps, 0)


@given(u"xs ← intersections(4:shape, 6:shape)")
def step_impl(context):
    context.xs = intersections(
        intersection(4, context.shape), intersection(6, context.shape)
    )


@when(u"c ← refracted_color(w, comps, 5)")
def step_impl(context):
    context.c = refracted_color(context.w, context.comps, 5)


@given(u"shape has")
def step_impl(context):
    context.shape.material.transparency = 1.0
    context.shape.material.refractive_index = 1.5


@when(u"c ← refracted_color(w, comps, 0)")
def step_impl(context):
    context.c = refracted_color(context.w, context.comps, 0)


@given(u"r ← ray(point(0, 0, √2/2), vector(0, 1, 0))")
def step_impl(context):
    context.r = ray(point(0, 0, sqrt(2) / 2), vector(0, 1, 0))


@given(u"xs ← intersections(-√2/2:shape, √2/2:shape)")
def step_impl(context):
    context.xs = intersections(
        intersection(-sqrt(2) / 2, context.shape),
        intersection(sqrt(2) / 2, context.shape),
    )


@given(u"A ← the first object in w")
def step_impl(context):
    context.A = context.w.objects[0]


@given(u"A has")
def step_impl(context):
    context.A.material.ambient = 1.0
    context.A.material.pattern = test_pattern()


@given(u"B ← the second object in w")
def step_impl(context):
    context.B = context.w.objects[1]


@given(u"B has")
def step_impl(context):
    context.B.material.transparency = 1.0
    context.B.material.refractive_index = 1.5


@given(u"r ← ray(point(0, 0, 0.1), vector(0, 1, 0))")
def step_impl(context):
    context.r = ray(point(0, 0, 0.1), vector(0, 1, 0))


@given(u"xs ← intersections(-0.9899:A, -0.4899:B, 0.4899:B, 0.9899:A)")
def step_impl(context):
    context.xs = intersections(
        intersection(-0.9899, context.A),
        intersection(-0.4899, context.B),
        intersection(0.4899, context.B),
        intersection(0.9899, context.A),
    )


@then(u"c = color(0, 0.99888, 0.04725)")
def step_impl(context):
    assert context.c == color(0, 0.99888, 0.04725)


@given(u"floor ← plane() with")
def step_impl(context):
    context.floor = plane()
    context.floor.transform = translation(0, -1, 0)
    context.floor.material.transparency = 0.5
    context.floor.material.refractive_index = 1.5


@given(u"floor is added to w")
def step_impl(context):
    context.w.objects.append(context.floor)


@given(u"ball ← sphere() with")
def step_impl(context):
    context.ball = sphere()
    context.ball.material.color = color(1, 0, 0)
    context.ball.material.ambient = 0.5
    context.ball.transform = translation(0, -3.5, -0.5)


@given(u"ball is added to w")
def step_impl(context):
    context.w.objects.append(context.ball)


@given(u"xs ← intersections(√2:floor)")
def step_impl(context):
    context.xs = intersections(intersection(sqrt(2), context.floor))


@when(u"color ← shade_hit(w, comps, 5)")
def step_impl(context):
    context.color = shade_hit(context.w, context.comps, 5)


@then(u"color = color(0.93642, 0.68642, 0.68642)")
def step_impl(context):
    assert context.color == color(0.93642, 0.68642, 0.68642)


@given(u"floor2 ← plane() with")
def step_impl(context):
    context.floor2 = plane()
    context.floor2.transform = translation(0, -1, 0)
    context.floor2.material.reflective = 0.5
    context.floor2.material.transparency = 0.5
    context.floor2.material.refractive_index = 1.5


@given(u"floor2 is added to w")
def step_impl(context):
    context.w.objects.append(context.floor2)


@given(u"xs ← intersections(√2:floor2)")
def step_impl(context):
    context.xs = intersections(intersection(sqrt(2), context.floor2))


@then(u'color = color(0.93391, 0.69643, 0.69243)')
def step_impl(context):
    assert context.color == color(0.93391, 0.69643, 0.69243)