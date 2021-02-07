from behave import *
from parser import parse_obj_file

@given(u'gibberish ← a file containing')
def step_impl(context):
    context.gibberish = context.text


@when(u'parser ← parse_obj_file(gibberish)')
def step_impl(context):
    context.parser = parse_obj_file(context.gibberish)


@then(u'parser should have ignored 5 lines')
def step_impl(context):
    assert context.parser == 5