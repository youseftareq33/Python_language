def fibonacci(number):
    if(number==0):
        return 1
    elif(number==1):
        return 1
    
    return fibonacci(number-1)+fibonacci(number-2)

print(fibonacci(5))
