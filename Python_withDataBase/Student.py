class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def print_Data(self):
        print("id: " + str(self.id) + "\n" + "name: " + self.name)
