#BDD-фреймворк
from behave import *
from adapter import RoundPeg
from adapter import RoundHole
from adapter import SquarePeg
from adapter import SquarePegAdapter


@given('size of round peg - radius "{peg_size}" and size of round hole - "{hole_radius}"')
def step(context, peg_size, hole_radius):
    context.round_peg = RoundPeg(int(peg_size))
    context.hole = RoundHole(int(hole_radius))


@given('size of square peg - width "{peg_size}" and size of round hole - "{hole_radius}"')
def step(context, peg_size, hole_radius):
    context.square_peg = SquarePeg(int(peg_size))
    context.hole = RoundHole(int(hole_radius))


@then('peg and hole compatible')
def step(context):
    assert context.hole.fits(context.round_peg) == f"Деталь подходит. " \
                                                      f"Радиус детали: {context.round_peg.get_radius()}, " \
                                                      f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"


@then('peg and hole incompatible')
def step(context):
    assert context.hole.fits(context.round_peg) == f"Деталь не подходит. " \
                                                      f"Радиус детали: {context.round_peg.get_radius()}, " \
                                                      f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"


@then('the square peg is not comparable to the round hole')
def step(context):
    f = 0
    try:
        context.hole.fits(context.square_peg)
    except AttributeError:
        f = 1
    finally:
        assert f == 1, "Тест не пройден"


@then('peg and hole compatible after conversion via adapter')
def step(context):
    context.adapter = SquarePegAdapter(context.square_peg)
    assert context.hole.fits(context.adapter) == f"Деталь подходит. " \
                                                 f"Радиус детали: {context.adapter.get_radius()}, " \
                                                 f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"


@then('peg and hole incompatible after conversion via adapter')
def step(context):
    context.adapter = SquarePegAdapter(context.square_peg)
    assert context.hole.fits(context.adapter) == f"Деталь не подходит. " \
                                                 f"Радиус детали: {context.adapter.get_radius()}, " \
                                                 f"радиус отверстия {context.hole.get_radius()}", \
        "Тест не пройден"
