# not like java and c(differnt parameter) it's  same parameter, diferrent contant
class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b=0):
        return a + b
    
    def add(self, *args):
        return sum(args)


calc = Calculator()
res1 = calc.add(2)      
res2 = calc.add(2,3)  
res3 = calc.add(2, 3, 4)

