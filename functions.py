<<<<<<< HEAD
def laf(minutes : int,gender : char)->float:
    if gender == "M":
        if minutes >= 0 and minutes <=100 :
            return 1,47
        elif minutes >= 100 and minutes <=280:
            return 1,70
        elif minutes >280:
            return 2,1
    else:
        if minutes >= 0 and minutes <=100 :
            return 1,42
        elif minutes >= 100 and minutes <=280:
            return 1,56
        elif minutes >280:
            return 1,73

    return 0.0






=======
def basalMetabolism(gender:str,age:int,weight:float) -> float:
    res = float(0.0)
    if gender == "F":
       if (age <= 29):
          res = 14,7 * weight + 496
       elif (age > 29 and age <= 59):
          res = 8,7 * weight + 829  
       elif (age > 59 and age <= 74):
          res = 9,2 * weight + 688
       else:
          res = 9,8 * weight + 624
    else:
       if (age <= 29):
          res = 15,3 * weight + 679
       elif (age > 29 and age <= 59):
          res = 11,6 * weight + 879  
       elif (age > 59 and age <= 74):
          res = 11,9 * weight + 700
       else:
          res = 8,4 * weight + 819
    
    return res
>>>>>>> 9c798a2076340ce14e915df749e389940df239c1
