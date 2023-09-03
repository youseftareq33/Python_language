class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Player(Person):
    def __init__(self, name, age,team):
        super().__init__(name, age)
        self.team=team
    
    def printData(self):
        print("name: "+self.name+"\n"+"age: ",self.age,"\n"+"team: "+self.team)
    
p=Player("MSalah",31,"LiverPool")

p.printData()