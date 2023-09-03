from Person import Person

class Palestinian(Person):
    def __init__(self, name, income):
        super().__init__(name, income)

    def eat(self):
        print(self.get_name() + " eats msakhan")

    def speak(self):
        print(self.get_name() + " speaks Arabic")
