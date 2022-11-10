def basal_metabolism(gender:str, age:int, weight:int) -> float:
    if gender == "M":
       if (age <= 29):
          return 15.3 * weight + 679
       
       if (age > 29 and age <= 59):
          return 11.6 * weight + 879  
       
       if (age > 59 and age <= 74):
          return 11.9 * weight + 700
       
       return 8.4 * weight + 819
    else:
       if (age <= 29):
          return 14.7 * weight + 496
       
       if (age > 29 and age <= 59):
          return 8.7 * weight + 829  
       
       if (age > 59 and age <= 74):
          return 9.2 * weight + 688
       
       return 9.8 * weight + 624

def laf(minutes: int, gender: str) -> float:
    if gender == "M":
        if minutes >= 0 and minutes <=100 :
            return 1.47
        
        if minutes >= 100 and minutes <=280:
            return 1.70
        
        if minutes > 280:
            return 2.1
    else:
        if minutes >= 0 and minutes <=100 :
            return 1.42
        
        if minutes >= 100 and minutes <=280:
            return 1.56
        
        if minutes >280:
            return 1.73

    return 0.0

def calorie_requirement(basalMetabolism_: float, laf_: float) -> float:
    return basalMetabolism_*laf_

def bmi(weight: int, height: int)->float:
    height_m = height / 100.0 # convert cm to m 
    value = weight / pow(height_m,2)
    return value

from typing import Tuple
def calories_division(calorie_requirement: float) -> Tuple[float,float,float] :
    carbohydrates = (calorie_requirement * 60) / 100
    fats = (calorie_requirement * 25) / 100
    proteins = (calorie_requirement * 15) / 100

    return carbohydrates, fats, proteins

def getWorkoutTime(bmi_: float) -> int:
    if bmi_ < 18 :
        return 180
    
    if bmi_ >= 18 and bmi_ <= 25:
        return 240
    
    return 300



