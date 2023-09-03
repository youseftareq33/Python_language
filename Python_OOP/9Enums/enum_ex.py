# Enumeration: are used to define a finite list of distinct, named constants that have a
# specific meaning or purpose within a program. 

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)         # Output: Color.RED
print(Color.GREEN.value)  # Output: 2


for color in Color:
    print(color)
# Output:
# Color.RED
# Color.GREEN
# Color.BLUE
