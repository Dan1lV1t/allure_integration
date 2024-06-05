import pytest
import allure
from my_module import add


@allure.feature('Test....1111')
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (-1, -1, -2),
    (2.5, 3.5, 6.0)
])
@allure.feature('Test....2222')
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
