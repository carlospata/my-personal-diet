from typing import List
import pytest
from src.functions import laf

tests : List[dict] = [
    {"res" : laf(90,"M"), "expected_res" : 1.47},
    {"res" : laf(110,"M"), "expected_res" : 1.70},
    {"res" : laf(300, "M"), "expected_res" : 2.1},
    {"res" : laf(70, "F"), "expected_res" : 1.42},
    {"res" : laf(110, "F"), "expected_res" : 1.56},
    {"res" : laf(300, "F"), "expected_res" : 1.73},
    {"res" : laf(-23, "M"), "expected_res" : 0.0},
    {"res" : laf(-10, "F"), "expected_res" : 0.0},
]

# enables parametrization of arguments for a test function
@pytest.mark.parametrize("test", tests)
def test_generic(test: dict) -> None:
    # arrange
    # act
    res = test["res"]
    # assert
    assert res == test["expected_res"]