from behave import *
from ray import ray
from tuple import point, vector
from sphere import sphere, intersect, set_transform
from matrix import identity_matrix, translation, scaling

@given(u'r ← ray(point(0, 0, -5), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0, -5), vector(0, 0, 1))


@given(u's ← sphere()')
def step_impl(context):
    context.s = sphere()


@when(u'xs ← intersect(s, r)')
def step_impl(context):
    context.xs = intersect(context.s, context.r)


@then(u'xs.count = 2')
def step_impl(context):
    assert len(context.xs) == 2


@then(u'xs[0].t = 4.0')
def step_impl(context):
    assert context.xs[0].t == 4.0


@then(u'xs[1].t = 6.0')
def step_impl(context):
    assert context.xs[1].t == 6.0


@given(u'r ← ray(point(0, 1, -5), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 1, -5), vector(0, 0, 1))


@then(u'xs[0].t = 5.0')
def step_impl(context):
    assert context.xs[0].t == 5.0


@then(u'xs[1].t = 5.0')
def step_impl(context):
    assert context.xs[1].t == 5.0


@given(u'r ← ray(point(0, 2, -5), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 2, -5), vector(0, 0, 1))


@then(u'xs.count = 0')
def step_impl(context):
    assert len(context.xs) == 0


@given(u'r ← ray(point(0, 0, 0), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0, 0), vector(0, 0, 1))


@then(u'xs[0].t = -1.0')
def step_impl(context):
    assert context.xs[0].t == -1.0


@then(u'xs[1].t = 1.0')
def step_impl(context):
    assert context.xs[1].t == 1.0


@given(u'r ← ray(point(0, 0, 5), vector(0, 0, 1))')
def step_impl(context):
    context.r = ray(point(0, 0, 5), vector(0, 0, 1))


@then(u'xs[0].t = -6.0')
def step_impl(context):
    assert context.xs[0].t == -6.0


@then(u'xs[1].t = -4.0')
def step_impl(context):
    assert context.xs[1].t == -4.0


@then(u'xs[0].object = s')
def step_impl(context):
    assert context.xs[0].object == context.s


@then(u'xs[1].object = s')
def step_impl(context):
    assert context.xs[1].object == context.s


@then(u's.transform = identity_matrix')
def step_impl(context):
    assert context.s.transform == identity_matrix()


@given(u't ← translation(2, 3, 4)')
def step_impl(context):
    context.t = translation(2, 3, 4)


@when(u'set_transform(s, t)')
def step_impl(context):
    set_transform(context.s, context.t)


@then(u's.transform = t')
def step_impl(context):
    assert context.s.transform == context.t


@when(u'set_transform(s, scaling(2, 2, 2))')
def step_impl(context):
    set_transform(context.s, scaling(2, 2, 2))


@then(u'xs[0].t = 3')
def step_impl(context):
    print(context.xs[0].t)
    print(context.xs[1].t)
    assert context.xs[0].t == 3


@then(u'xs[1].t = 7')
def step_impl(context):
    assert context.xs[1].t == 7


@when(u'set_transform(s, translation(5, 0, 0))')
def step_impl(context):
    set_transform(context.s, translation(5, 0, 0))


# @when(u'n ← normal_at(s, point(1, 0, 0))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When n ← normal_at(s, point(1, 0, 0))')


# @then(u'n = vector(1, 0, 0)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = vector(1, 0, 0)')


# @when(u'n ← normal_at(s, point(0, 1, 0))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When n ← normal_at(s, point(0, 1, 0))')


# @then(u'n = vector(0, 1, 0)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = vector(0, 1, 0)')


# @when(u'n ← normal_at(s, point(0, 0, 1))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When n ← normal_at(s, point(0, 0, 1))')


# @then(u'n = vector(0, 0, 1)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = vector(0, 0, 1)')


# @when(u'n ← normal_at(s, point(√3/3, √3/3, √3/3))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When n ← normal_at(s, point(√3/3, √3/3, √3/3))')


# @then(u'n = vector(√3/3, √3/3, √3/3)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = vector(√3/3, √3/3, √3/3)')


# @then(u'n = normalize(n)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = normalize(n)')


# @given(u'set_transform(s, translation(0, 1, 0))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given set_transform(s, translation(0, 1, 0))')


# @when(u'n ← normal_at(s, point(0, 1.70711, -0.70711))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When n ← normal_at(s, point(0, 1.70711, -0.70711))')


# @then(u'n = vector(0, 0.70711, -0.70711)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = vector(0, 0.70711, -0.70711)')


# @given(u'm ← scaling(1, 0.5, 1) * rotation_z(π/5)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given m ← scaling(1, 0.5, 1) * rotation_z(π/5)')


# @given(u'set_transform(s, m)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given set_transform(s, m)')


# @when(u'n ← normal_at(s, point(0, √2/2, -√2/2))')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When n ← normal_at(s, point(0, √2/2, -√2/2))')


# @then(u'n = vector(0, 0.97014, -0.24254)')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then n = vector(0, 0.97014, -0.24254)')


# @when(u'm ← s.material')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When m ← s.material')


# @then(u'm = material()')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then m = material()')


# @given(u'm ← material()')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given m ← material()')


# @given(u'm.ambient ← 1')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given m.ambient ← 1')


# @when(u's.material ← m')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When s.material ← m')


# @then(u's.material = m')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then s.material = m')


# @given(u's ← glass_sphere()')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given s ← glass_sphere()')


# @then(u's.material.transparency = 1.0')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then s.material.transparency = 1.0')


# @then(u's.material.refractive_index = 1.5')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then s.material.refractive_index = 1.5')