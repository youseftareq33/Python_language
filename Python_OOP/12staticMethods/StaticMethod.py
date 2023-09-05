# The static method is:

# similar to python class methods.
# method can be called without an object for that class.
# cannot modify the state of an object as they are not bound to it.
# we don’t need the self to be passed as the first argument.



# ex:

# Using @staticmethod
class Calculator:

    @staticmethod
    def addNumbers(x,y):
        return x+y
    @staticmethod
    def subNumbers(x,y):
        return x-y
    
res=Calculator.addNumbers(5,10)
print(res)

# Using staticmethod()
class Calculator2:

    def addNumbers(x,y):
        return x+y

    def subNumbers(x,y):
        return x-y
    
# create addNumbers static method
Calculator2.addNumbers = staticmethod(Calculator2.addNumbers)

res=Calculator2.addNumbers(5,20)
print(res)