import pytest
from main import add, sub, mul, floor_div

def test_add():
    assert add(5, 3) == 8
    assert add(0, 0) == 0
    assert add(110, 80) == 190


def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(110, 80) == 30


def test_mul():
    assert mul(5, 3) == 15
    assert mul(0, 0) == 0
    assert mul(110, 80) == 8800


def test_div():
    assert floor_div(5, 3) == 1
    assert floor_div(5, 0) == "Error! Division by zero is not allowed."
    assert floor_div(110, 80) == 1
    assert floor_div(0,60) == 0
