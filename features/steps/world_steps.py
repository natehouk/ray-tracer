from behave import *
from world import world, default_world, intersect_world, shade_hit, color_at, is_shadowed
from tuple import point, vector, color, point_light
from sphere import sphere, intersection
from matrix import scaling
from ray import ray

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


@given(u'shape ← the first object in w')
def step_impl(context):
    context.shape = context.w.objects[0]


@when(u'c ← shade_hit(w, comps)')
def step_impl(context):
    context.c = shade_hit(context.w, context.comps)


@then(u'c = color(0.38066, 0.47583, 0.2855)')
def step_impl(context):
    print(context.c)
    assert context.c == color(0.38066, 0.47583, 0.2855)


@given(u'w.light ← point_light(point(0, 0.25, 0), color(1, 1, 1))')
def step_impl(context):
    context.w.light = point_light(point(0, 0.25, 0), color(1, 1, 1))


@given(u'shape ← the second object in w')
def step_impl(context):
    context.shape = context.w.objects[1]


@given(u'i ← intersection(0.5, shape)')
def step_impl(context):
    context.i = intersection(0.5, context.shape)


@then(u'c = color(0.90498, 0.90498, 0.90498)')
def step_impl(context):
    assert context.c == color(0.90498, 0.90498, 0.90498)


@given(u'r ← ray(point(0, 0, -5), vector(0, 1, 0))')
def step_impl(context):
    context.r = ray(point(0, 0, -5), vector(0, 1, 0))


@when(u'c ← color_at(w, r)')
def step_impl(context):
    context.c = color_at(context.w, context.r)


@then(u'c = color(0, 0, 0)')
def step_impl(context):
    assert context.c == color(0, 0, 0)


@given(u'outer ← the first object in w')
def step_impl(context):
    context.outer = context.w.objects[0]


@given(u'outer.material.ambient ← 1')
def step_impl(context):
    context.outer.material.ambient = 1


@given(u'inner ← the second object in w')
def step_impl(context):
    context.inner = context.w.objects[1]


@given(u'inner.material.ambient ← 1')
def step_impl(context):
    context.inner.material.ambient = 1


@given(u'r ← ray(point(0, 0, 0.75), vector(0, 0, -1))')
def step_impl(context):
    context.r = ray(point(0, 0, 0.75), vector(0, 0, -1))


@then(u'c = inner.material.color')
def step_impl(context):
    print(context.c)
    print(context.inner.material.color)
    assert context.c == context.inner.material.color


@given(u'p ← point(0, 10, 0)')
def step_impl(context):
    context.p = point(0, 10, 0)


@then(u'is_shadowed(w, p) is false')
def step_impl(context):
    assert is_shadowed(context.w, context.p) is False


@given(u'p ← point(10, -10, 10)')
def step_impl(context):
    context.p = point(10, -10, 10)


@then(u'is_shadowed(w, p) is true')
def step_impl(context):
    assert is_shadowed(context.w, context.p) is True


@given(u'p ← point(-20, 20, -20)')
def step_impl(context):
    context.p = point(-20, 20, -20)


@given(u'p ← point(-2, 2, -2)')
def step_impl(context):
    context.p = point(-2, 2, -2)


@given(u'w.light ← point_light(point(0, 0, -10), color(1, 1, 1))')
def step_impl(context):
    context.w.light = point_light(point(0, 0, -10), color(1, 1, 1))


@given(u's1 ← sphere()')
def step_impl(context):
    context.s1 = sphere()


@given(u's1 is added to w')
def step_impl(context):
    context.w.objects.append(context.s1)


@given(u's2 is added to w')
def step_impl(context):
    context.w.objects.append(context.s2)


@given(u'i ← intersection(4, s2)')
def step_impl(context):
    context.i = intersection(4, context.s2)


@then(u'c = color(0.1, 0.1, 0.1)')
def step_impl(context):
    assert context.c == color(0.1, 0.1, 0.1)
