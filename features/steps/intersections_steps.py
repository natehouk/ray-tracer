from behave import *
from sphere import intersection

@when(u'i ← intersection(3.5, s)')
def step_impl(context):
    context.i = intersection(3.5, context.s)


@then(u'i.t = 3.5')
def step_impl(context):
    assert context.i.t == 3.5


@then(u'i.object = s')
def step_impl(context):
    assert context.i.object == context.s


@given(u'shape ← sphere()')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given shape ← sphere()')


@given(u'i ← intersection(4, shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i ← intersection(4, shape)')


@when(u'comps ← prepare_computations(i, r)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(i, r)')


@then(u'comps.t = i.t')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.t = i.t')


@then(u'comps.object = i.object')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.object = i.object')


@then(u'comps.point = point(0, 0, -1)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.point = point(0, 0, -1)')


@then(u'comps.eyev = vector(0, 0, -1)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.eyev = vector(0, 0, -1)')


@then(u'comps.normalv = vector(0, 0, -1)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.normalv = vector(0, 0, -1)')


@given(u'shape ← plane()')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given shape ← plane()')


@given(u'r ← ray(point(0, 1, -1), vector(0, -√2/2, √2/2))')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given r ← ray(point(0, 1, -1), vector(0, -√2/2, √2/2))')


@given(u'i ← intersection(√2, shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i ← intersection(√2, shape)')


@then(u'comps.reflectv = vector(0, √2/2, √2/2)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.reflectv = vector(0, √2/2, √2/2)')


@then(u'comps.inside = false')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.inside = false')


@given(u'i ← intersection(1, shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i ← intersection(1, shape)')


@then(u'comps.point = point(0, 0, 1)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.point = point(0, 0, 1)')


@then(u'comps.inside = true')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.inside = true')


@given(u'shape ← sphere() with')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given shape ← sphere() with')


@given(u'i ← intersection(5, shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i ← intersection(5, shape)')


@then(u'comps.over_point.z < -EPSILON/2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.over_point.z < -EPSILON/2')


@then(u'comps.point.z > comps.over_point.z')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.point.z > comps.over_point.z')


@given(u'shape ← glass_sphere() with')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given shape ← glass_sphere() with')


@given(u'xs ← intersections(i)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(i)')


@when(u'comps ← prepare_computations(i, r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(i, r, xs)')


@then(u'comps.under_point.z > EPSILON/2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.under_point.z > EPSILON/2')


@then(u'comps.point.z < comps.under_point.z')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.point.z < comps.under_point.z')


@given(u'i1 ← intersection(1, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i1 ← intersection(1, s)')


@given(u'i2 ← intersection(2, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i2 ← intersection(2, s)')


@when(u'xs ← intersections(i1, i2)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When xs ← intersections(i1, i2)')


@then(u'xs[0].t = 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then xs[0].t = 1')


@then(u'xs[1].t = 2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then xs[1].t = 2')


@given(u'xs ← intersections(i2, i1)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(i2, i1)')


@when(u'i ← hit(xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i ← hit(xs)')


@then(u'i = i1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i = i1')


@given(u'i1 ← intersection(-1, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i1 ← intersection(-1, s)')


@given(u'i2 ← intersection(1, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i2 ← intersection(1, s)')


@then(u'i = i2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i = i2')


@given(u'i1 ← intersection(-2, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i1 ← intersection(-2, s)')


@given(u'i2 ← intersection(-1, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i2 ← intersection(-1, s)')


@then(u'i is nothing')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i is nothing')


@given(u'i1 ← intersection(5, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i1 ← intersection(5, s)')


@given(u'i2 ← intersection(7, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i2 ← intersection(7, s)')


@given(u'i3 ← intersection(-3, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i3 ← intersection(-3, s)')


@given(u'i4 ← intersection(2, s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given i4 ← intersection(2, s)')


@given(u'xs ← intersections(i1, i2, i3, i4)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(i1, i2, i3, i4)')


@then(u'i = i4')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i = i4')


@given(u'A ← glass_sphere() with')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given A ← glass_sphere() with')


@given(u'B ← glass_sphere() with')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given B ← glass_sphere() with')


@given(u'C ← glass_sphere() with')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given C ← glass_sphere() with')


@given(u'r ← ray(point(0, 0, -4), vector(0, 0, 1))')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given r ← ray(point(0, 0, -4), vector(0, 0, 1))')


@given(u'xs ← intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)')


@when(u'comps ← prepare_computations(xs[0], r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(xs[0], r, xs)')


@then(u'comps.n1 = 1.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n1 = 1.0')


@then(u'comps.n2 = 1.5')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n2 = 1.5')


@when(u'comps ← prepare_computations(xs[1], r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(xs[1], r, xs)')


@then(u'comps.n1 = 1.5')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n1 = 1.5')


@then(u'comps.n2 = 2.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n2 = 2.0')


@when(u'comps ← prepare_computations(xs[2], r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(xs[2], r, xs)')


@then(u'comps.n1 = 2.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n1 = 2.0')


@then(u'comps.n2 = 2.5')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n2 = 2.5')


@when(u'comps ← prepare_computations(xs[3], r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(xs[3], r, xs)')


@then(u'comps.n1 = 2.5')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n1 = 2.5')


@when(u'comps ← prepare_computations(xs[4], r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(xs[4], r, xs)')


@when(u'comps ← prepare_computations(xs[5], r, xs)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When comps ← prepare_computations(xs[5], r, xs)')


@then(u'comps.n2 = 1.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then comps.n2 = 1.0')


@given(u'shape ← glass_sphere()')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given shape ← glass_sphere()')


@given(u'r ← ray(point(0, 0, √2/2), vector(0, 1, 0))')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given r ← ray(point(0, 0, √2/2), vector(0, 1, 0))')


@given(u'xs ← intersections(-√2/2:shape, √2/2:shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(-√2/2:shape, √2/2:shape)')


@when(u'reflectance ← schlick(comps)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When reflectance ← schlick(comps)')


@then(u'reflectance = 1.0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then reflectance = 1.0')


@given(u'r ← ray(point(0, 0, 0), vector(0, 1, 0))')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given r ← ray(point(0, 0, 0), vector(0, 1, 0))')


@given(u'xs ← intersections(-1:shape, 1:shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(-1:shape, 1:shape)')


@then(u'reflectance = 0.04')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then reflectance = 0.04')


@given(u'r ← ray(point(0, 0.99, -2), vector(0, 0, 1))')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given r ← ray(point(0, 0.99, -2), vector(0, 0, 1))')


@given(u'xs ← intersections(1.8589:shape)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given xs ← intersections(1.8589:shape)')


@then(u'reflectance = 0.48873')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then reflectance = 0.48873')


@given(u's ← triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given s ← triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))')


@when(u'i ← intersection_with_uv(3.5, s, 0.2, 0.4)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When i ← intersection_with_uv(3.5, s, 0.2, 0.4)')


@then(u'i.u = 0.2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i.u = 0.2')


@then(u'i.v = 0.4')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then i.v = 0.4')
