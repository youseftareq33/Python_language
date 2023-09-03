from Person import Person

class American(Person):
    def __init__(self, name, income):
        super().__init__(name, income)

    def eat(self):
        print(self.get_name() +" eat Burger")

    def speak(self):
        print(self.get_name() +" speak english")