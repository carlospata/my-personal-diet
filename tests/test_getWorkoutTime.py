from src.functions import getWorkoutTime

def testWorkoutTime()->None:
    assert getWorkoutTime(16) == 180
    assert getWorkoutTime(23) == 240
    assert getWorkoutTime(26) == 300