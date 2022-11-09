def basal_metabolism(gender:str, age:int, weight:int) -> float:
    res = float(0.0)
    if gender == "M":
       if (age <= 29):
          res = 15.3 * weight + 679
       elif (age > 29 and age <= 59):
          res = 11.6 * weight + 879  
       elif (age > 59 and age <= 74):
          res = 11.9 * weight + 700
       else:
          res = 8.4 * weight + 819
    else:
       if (age <= 29):
          res = 14.7 * weight + 496
       elif (age > 29 and age <= 59):
          res = 8.7 * weight + 829  
       elif (age > 59 and age <= 74):
          res = 9.2 * weight + 688
       else:
          res = 9.8 * weight + 624
    return res

def laf(minutes : int,gender : str)->float:
    if gender == "M":
        if minutes >= 0 and minutes <=100 :
            return 1.47
        elif minutes >= 100 and minutes <=280:
            return 1.70
        elif minutes >280:
            return 2.1
    else:
        if minutes >= 0 and minutes <=100 :
            return 1.42
        elif minutes >= 100 and minutes <=280:
            return 1.56
        elif minutes >280:
            return 1.73

    return 0.0

def calorie_requirement( basalMetabolism_ : float,laf_ : float)->float:
    return basalMetabolism_*laf_

def bmi(weight: int, height: int)->float:
    height_m = height / 100.0
    value = weight / pow(height_m,2)
    return value

from typing import Tuple
def calories_division(calorie_requirement: float) -> Tuple[float,float,float] :
    carbohydrates = (calorie_requirement * 60) / 100
    fats = (calorie_requirement * 25) / 100
    proteins = (calorie_requirement * 15) / 100

    return carbohydrates, fats, proteins

def getWorkoutTime(bmi_ :float)->int:
    minutes = int(0)
    if bmi_ < 18 :
        minutes = 180
    elif bmi_ >= 18 and bmi_ <= 25:
        minutes = 240
    else:
        minutes = 300

    return minutes




