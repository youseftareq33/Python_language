# return multiple values in python functions
def get_data():
    id=10
    name="Ahmad"

    return id,name

id,name=get_data()

print(id)
print(name)

print("--------------------------------------")
# how to do type hinting with multiple values
def get_data() -> tuple[int, str]:
    id = 10
    name = "Ahmad"
    return id, name

tuple_data=get_data()
print(tuple_data)
print("--------------------------------------")
# how to do type hinting with list, set, tuple, dictionary

#list:
def sum_of_list_num(numbers: list[int]) -> int:
    res=0
    for num in numbers:
        res+=num

    return res

list_numbers=[1,2,3]
print(sum(list_numbers))


#set:
def sum_of_set_num(numbers: set[int]) -> int:
    res=0
    for num in numbers:
        res+=num

    return res

set_numbers={1,2,3}
print(sum_of_set_num(set_numbers))

#tuple:
def sum_of_tuple_num(numbers: tuple[int]) -> int:
    res=0
    for i in range(0,len(numbers)):
        res+=numbers[i]

    return res

tuble_numbers=(1,2,3)
print(sum_of_tuple_num(tuble_numbers))

#dictionary:
def sum_of_dict_values(numbers: dict[str, int]) -> int:
    res= 0
    for key in numbers:
        res += numbers[key]
    return res

dict_numbers = {"one": 1, "two": 2, "three": 3}
print(sum_of_dict_values(dict_numbers))

print("--------------------------------------")
# how to do type hinting with default values
def sum(num1: int=5,num2: int=10)->int:
    return num1+num2

print(sum())