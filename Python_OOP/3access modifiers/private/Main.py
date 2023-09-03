from Number import Number

num = Number()

# give error cause we cannot access to it directly
print(num.__x)

# getter: print it's data
print(num.get_x()) 

# setter: set new value
num.set_x(20)
print(num.get_x())  
