from src.functions import calorie_requirement

def testCalorieRequirement()->None:
    assert calorie_requirement(1750.0, 1.70) == 2975
    assert calorie_requirement(1342.3, 1.73) == 2322.179
    assert calorie_requirement(1439, 1.43) == 2057.77