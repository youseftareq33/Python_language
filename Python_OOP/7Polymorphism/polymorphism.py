class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"



def make_animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()



print("Dog says:", make_animal_speak(dog))    
print("Cat says:", make_animal_speak(cat))    

