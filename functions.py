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






