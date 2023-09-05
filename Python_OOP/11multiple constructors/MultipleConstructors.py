# there are multiple way to do this:

# 1) default argument:
class Person:
    def __init__(self,name=None,age=0):
        self.name=name
        self.age=age

person1=Person()
person2=Person("Ahmad")
person3=Person(20)
person4=Person("Ahmad",20)

#------------------------------------------------------

# 2) Class Method:
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    # cls: refers to the class itself 
    # @classmethod: it's decorator make method a class method and have access to the class and its attributes.
    # decorator: function that extends or modifies the behavior of another function or method by wrapping it.
    @classmethod
    def from_parameter1(cls, name):
        return cls(name, 0)

    @classmethod
    def from_parameter2(cls, age):
        return cls(None, age)
 
person5 = Person.from_parameter1("Rami")
person6 = Person.from_parameter2(25)

 #------------------------------------------------------

# 3) Factory function:
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def from_parameter1(name):
        return Person(name, 0)
    
    def from_parameter2(age):
        return Person(None, age)