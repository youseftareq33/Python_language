# 1) str: returns a string representation of the object.
class ConvertString:
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return str(self.num)
    
my_num=ConvertString(20)
num_string=str(my_num)
   
print(num_string+" in string format")



num=int.__str__(10)
#-----------------------------------------------

# 2) len: returns the length of the object.
class MyName:
    def __init__(self, my_name):
        self.my_name=my_name

    def __len__(self):
        return len(self.my_name)


name=MyName("Ahmad")
length=len(name)

print(length)


length=str.__len__("Ahmad")
#-----------------------------------------------

# 3) add: it's like + operator, used for built-in types like numbers and strings
num=10
num=num.__add__(5)
print(num)

#-----------------------------------------------

# 4) floor: round number to the nearest down

num=float.__floor__(2.58)

#-----------------------------------------------

# 5) dir: return all magic methods inherited by a class.
list_of_attributes=int.__dir__(int)
print(list_of_attributes)