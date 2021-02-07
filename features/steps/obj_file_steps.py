from behave import *
from parser import parse_obj_file
from tuple import point

@given(u'gibberish ← a file containing')
def step_impl(context):
    context.gibberish = context.text


@when(u'parser ← parse_obj_file(gibberish)')
def step_impl(context):
    context.parser = parse_obj_file(context.gibberish)


@then(u'parser should have ignored 5 lines')
def step_impl(context):
    assert context.parser.ignored == 5


@given(u'file ← a file containing')
def step_impl(context):
    context.file = context.text


@when(u'parser ← parse_obj_file(file)')
def step_impl(context):
    context.parser = parse_obj_file(context.file)


@then(u'parser.vertices[1] = point(-1, 1, 0)')
def step_impl(context):
    context.parser.vertices[1] = point(-1, 1, 0)


@then(u'parser.vertices[2] = point(-1, 0.5, 0)')
def step_impl(context):
    context.parser.vertices[2] = point(-1, 0.5, 0)


@then(u'parser.vertices[3] = point(1, 0, 0)')
def step_impl(context):
    context.parser.vertices[3] = point(1, 0, 0)


@then(u'parser.vertices[4] = point(1, 1, 0)')
def step_impl(context):
    context.parser.vertices[4] = point(1, 1, 0)


@when(u'g ← parser.default_group')
def step_impl(context):
    context.g = context.parser.default_group


@when(u't1 ← first child of g')
def step_impl(context):
    context.t1 = context.g[0]


@when(u't2 ← second child of g')
def step_impl(context):
    context.t2 = context.g[1]


@then(u't1.p1 = parser.vertices[1]')
def step_impl(context):
    assert context.t1.p1 == context.parser.vertices[1]


@then(u't1.p2 = parser.vertices[2]')
def step_impl(context):
    assert context.t1.p2 == context.parser.vertices[2]


@then(u't1.p3 = parser.vertices[3]')
def step_impl(context):
    assert context.t1.p3 == context.parser.vertices[3]


@then(u't2.p1 = parser.vertices[1]')
def step_impl(context):
    assert context.t2.p1 == context.parser.vertices[1]


@then(u't2.p2 = parser.vertices[3]')
def step_impl(context):
    assert context.t2.p2 == context.parser.vertices[3]


@then(u't2.p3 = parser.vertices[4]')
def step_impl(context):
    assert context.t2.p3 == context.parser.vertices[4]