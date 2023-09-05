def primeNumber(number):
    check_primeNum=True

    if number==1:
        check_primeNum=False
    elif number>=2:
        for i in range(2,number):
            if number%i==0 and i!=number:
                check_primeNum=False
                break
    
    return check_primeNum


for i in range(1,100):
    print(i,primeNumber(i))        
