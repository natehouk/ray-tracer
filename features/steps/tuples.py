from behave import *
import T

@given(u'a ← tuple(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    context.a = T.T(4.3, -4.2, 3.1, 1.0)


@then(u'a.x = 4.3')
def step_impl(context):
    assert context.a.x is 4.3


@then(u'a.y = -4.2')
def step_impl(context):
    assert context.a.y is -4.2


@then(u'a.z = 3.1')
def step_impl(context):
    assert context.a.z is 3.1


@then(u'a.w = 1.0')
def step_impl(context):
    assert context.a.w is 1.0


@then(u'a is a point')
def step_impl(context):
    assert context.a.is_point() is True


@then(u'a is not a vector')
def step_impl(context):
    assert context.a.is_vector() is not True


@given(u'a ← tuple(4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
    context.a = T.T(4.3, -4.2, 3.1, 0.0)


@then(u'a.w = 0.0')
def step_impl(context):
    assert context.a.w is 0.0


@then(u'a is not a point')
def step_impl(context):
    assert context.a.is_point() is not True


@then(u'a is a vector')
def step_impl(context):
    assert context.a.is_vector() is True