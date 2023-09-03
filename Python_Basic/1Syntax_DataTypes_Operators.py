# Syntax of python/Data Type/Operators:
''' all the keywords in small letter except
True,False,None .. in capital letter '''

x=2
y=3
res=x+y
print(res)
#--------------------------------
a, b, c = 5, 3.2, 'Hello'
print(a+b) # if a+b+c it will give error, so use  a+b, c
print(a+b,"\n"+c) # under line
#--------------------------------
PI=10 # (Final)like java
#--------------------------------
check=True
#--------------------------------
name=None # null
#--------------------------------
num_string = '12'
num_int=10

print((int(num_string))+num_int) # casting
#--------------------------------
x = 5
y = 10
z="ahmad"

print('The value of x is {} and y is {} {}'.format(x,y,z))
#--------------------------------
num_string = '12'
num_int=10

print((int(num_string))+num_int) # casting
#--------------------------------
# an operator type:

'''
Operator	Operation	Example
+	Addition	5 + 2 = 7
-	Subtraction	4 - 2 = 2
*	Multiplication	2 * 3 = 6
/	Division	4 / 2 = 2
//	Floor Division	10 // 3 = 3
%	Modulo	5 % 2 = 1
**	Power	4 ** 2 = 16
'''
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

#--------------------------------
# an Assignment Operators
'''
=	Assignment Operator	a = 7
+=	Addition Assignment	a += 1 # a = a + 1
-=	Subtraction Assignment	a -= 3 # a = a - 3
*=	Multiplication Assignment	a *= 4 # a = a * 4
/=	Division Assignment	a /= 3 # a = a / 3
%=	Remainder Assignment	a %= 10 # a = a % 10
**=	Exponent Assignment	a **= 10 # a = a ** 10
'''

# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15
#--------------------------------
# an

'''
==	Is Equal To	3 == 5 gives us False
!=	Not Equal To	3 != 5 gives us True
>	Greater Than	3 > 5 gives us False
<	Less Than	3 < 5 gives us True
>=	Greater Than or Equal To	3 >= 5 give us False
<=	Less Than or Equal To	3 <= 5 gives us True
'''

a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)
#--------------------------------
# an Logical Operators

'''
Operator	Example	Meaning
and	a and b	Logical AND:

					True only if both the operands are True
or	a or b	Logical OR:

					True if at least one of the operands is True
not	not a	Logical NOT:

					True if the operand is False and vice-versa.
'''

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False
#--------------------------------
# an Bitwise operators

'''
Operator	Meaning	Example
&	Bitwise AND	x & y = 0 (0000 0000)
|	Bitwise OR	x | y = 14 (0000 1110)
~	Bitwise NOT	~x = -11 (1111 0101)
^	Bitwise XOR	x ^ y = 14 (0000 1110)
>>	Bitwise right shift	x >> 2 = 2 (0000 0010)
<<	Bitwise left shift	x << 2 = 40 (0010 1000)
'''
#--------------------------------
# an Special operators
'''
Operator	Meaning	Example
is	True if the operands are identical (refer to the same object)	x is True
is not	True if the operands are not identical (do not refer to the same object)	x is not True
in	True if value/variable is found in the sequence	5 in x
not in	True if value/variable is not found in the sequence	5 not in x
'''

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False
#================================
# if elif else 
number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')