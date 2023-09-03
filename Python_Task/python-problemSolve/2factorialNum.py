def factNum(number):
    if number==0:
        return 1
    elif number==1:
        return 1
    
    return number*factNum(number-1)

print(factNum(10))