from typing import List
import pytest
from src.functions import basal_metabolism

tests: List[dict] = [
    { "res": basal_metabolism("M",20,55), "expected_res": 1520.5},
    { "res": basal_metabolism("M",40,55), "expected_res": 1517},
    { "res": basal_metabolism("M",60,55), "expected_res": 1354.5},
    { "res": basal_metabolism("M",80,55), "expected_res": 1281},

    { "res": basal_metabolism("F",20,55), "expected_res": 1304.5},
    { "res": basal_metabolism("F",40,55), "expected_res": 1307.5},
    { "res": basal_metabolism("F",60,55), "expected_res": 1194},
    { "res": basal_metabolism("F",80,55), "expected_res": 1163}   
]

# enables parametrization of arguments for a test function
@pytest.mark.parametrize("test", tests)
def test_generic(test: dict) -> None:
    # arrange
    # act
    res = test["res"]
    # assert
    assert res == test["expected_res"]
