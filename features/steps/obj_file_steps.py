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