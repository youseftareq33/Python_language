# or we can called it dunder
# method that contain double underscore, and it's allow you to define custom behavior
# for specific operations that involve objects of your class. 

num=10

num=num.__add__(5)
print(num)

num=int.__str__(num)
print(num+" string format")