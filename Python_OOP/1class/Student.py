class Student:
    # if our class is empty we can use pass statement to avoid getting an error.

    #_init_ func: All classes have _init_ function, and it's always executed when the class is being initiated.
    
    #self: is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    #      we can change it's name to anything we want in case we put it the first parameter on _init func.
    def __init__(self,name,city):
        self.name=name
        self.city=city
        
    #_str_ func: use to print data
    def __str__(self):
        return "name: "+self.name+"\n"+"city: "+self.city

    # func of object
    def printData(self):
        print("name: " + self.name+"\n"+"city: "+self.city)


student1=Student("ahmad","jenin")
# this print using _str_ func
print(student1)

# or u can print it like this:
print(student1.name)

# print our spesific function
student1.printData()

print("-----------------------------------------------"+"\n")
#--------------------------
# access to variable inside object:

#1) we can set any variable on any value we want
student1.name="yousef"
print(student1)

#2) we can delete the object variable:
del student1.name
print(student1) # it give error cause it's dosen't find the name variable.

#3) and also, we can delete the object at all:
del student1
print(student1) # it give error cause it's dosen't find the the object.