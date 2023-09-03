from Palestinian import Palestinian
from American import American

palestinian=Palestinian("Ahmad",1200)

palestinian.eat()
palestinian.speak()

print("------------------------------------")
american=American("joe",5000)

american.eat()
american.speak()

print("------------------------------------")


print(palestinian.calculate_income(palestinian.get_income()))
print(american.calculate_income(american.get_income(),50))



