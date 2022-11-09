from typing import List
import pytest
from src.functions import bmi

tests: List[dict] = [
    { "res": bmi(55,173), "expected_res": 18.376825152861773},
    { "res": bmi(70,165), "expected_res": 25.71166207529844},
    { "res": bmi(90,190), "expected_res": 24.930747922437675},
    { "res": bmi(110,150), "expected_res": 48.888888888888886},
]

# enables parametrization of arguments for a test function
@pytest.mark.parametrize("test", tests)
def test_generic(test: dict) -> None:
    # arrange
    # act
    res = test["res"]
    # assert
    assert res == test["expected_res"]
