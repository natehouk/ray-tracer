from behave import *
from canvas import canvas, write_pixel, pixel_at, canvas_to_ppm
from tuple import color

@given(u'c ← canvas(10, 20)')
def step_impl(context):
    context.c = canvas(10, 20)


@then(u'c.width = 10')
def step_impl(context):
    context.c.width = 10


@then(u'c.height = 20')
def step_impl(context):
    context.c.height = 20


@then(u'every pixel of c is color(0, 0, 0)')
def step_impl(context):
    for i in range(0, context.c.width):
        for j in range(0, context.c.height):
            assert context.c.canvas[i][j] == color(0, 0, 0)


@given(u'red ← color(1, 0, 0)')
def step_impl(context):
    context.red = color(1, 0, 0)


@when(u'write_pixel(c, 2, 3, red)')
def step_impl(context):
    write_pixel(context.c, 2, 3, context.red)


@then(u'pixel_at(c, 2, 3) = red')
def step_impl(context):
    assert pixel_at(context.c, 2, 3) == context.red


@given(u'c ← canvas(5, 3)')
def step_impl(context):
    context.c = canvas(5, 3)


@when(u'ppm ← canvas_to_ppm(c)')
def step_impl(context):
    context.ppm = canvas_to_ppm(context.c)
    

@then(u'lines 1-3 of ppm are')
def step_impl(context):
    assert context.ppm.header == "P3\n5 3\n255"


@given(u'c1 ← color(1.5, 0, 0)')
def step_impl(context):
    context.c1 = color(1.5, 0, 0)


@given(u'c2 ← color(0, 0.5, 0)')
def step_impl(context):
    context.c2 = color(0, 0.5, 0)


@given(u'c3 ← color(-0.5, 0, 1)')
def step_impl(context):
    context.c3 = color(-0.5, 0, 1)


@when(u'write_pixel(c, 0, 0, c1)')
def step_impl(context):
    write_pixel(context.c, 0, 0, context.c1)


@when(u'write_pixel(c, 2, 1, c2)')
def step_impl(context):
    write_pixel(context.c, 2, 1, context.c2)


@when(u'write_pixel(c, 4, 2, c3)')
def step_impl(context):
    write_pixel(context.c, 4, 2, context.c3)


@then(u'lines 4-6 of ppm are')
def step_impl(context):
    assert context.ppm.body ==  "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"


@given(u'c ← canvas(10, 2)')
def step_impl(context):
    context.c = canvas(10, 2)


@when(u'every pixel of c is set to color(1, 0.8, 0.6)')
def step_impl(context):
    for i in range(0, context.c.width):
        for j in range(0, context.c.height):
            context.c.canvas[i][j] = color(1, 0.8, 0.6)


@then(u'lines 4-7 of ppm are')
def step_impl(context):
    assert context.ppm.body == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153\n255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204\n153 255 204 153 255 204 153 255 204 153 255 204 153"


@then(u'ppm ends with a newline character')
def step_impl(context):
    assert str(context.ppm).endswith("\n")