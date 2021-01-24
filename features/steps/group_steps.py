from behave import *
from group import group
from matrix import identity_matrix

@given(u'g ← group()')
def step_impl(context):
    context.g = group()


@then(u'g.transform = identity_matrix')
def step_impl(context):
    assert context.g.transform == identity_matrix()


@then(u'g is empty')
def step_impl(context):
    assert len(context.g.children) == 0
