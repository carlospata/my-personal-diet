from typing import List
import pytest
from src.functions import calories_division

tests: List[dict] = [
    { "res": calories_division(2500.65), "expected_res": (1500.39,625.1625,375.0975)},
    { "res": calories_division(3000.0), "expected_res": (1800,750,450)},
    { "res": calories_division(1897.2), "expected_res": (1138.32,474.3,284.58)},
    { "res": calories_division(3567.81), "expected_res": (2140.686,891.9525,535.1715)} 
]

# enables parametrization of arguments for a test function
@pytest.mark.parametrize("test", tests)
def test_generic(test: dict) -> None:
    # arrange
    # act
    res = test["res"]
    # assert
    assert res == test["expected_res"]