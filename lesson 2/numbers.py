# Python Data Types
# Primitive
    # Number: int, float, complex
    # String: str
    # Boolean: bool
    # None

# Container
    # list
    # tuple
    # set
    # dictionary


print(type(4))  # int
print(type(5.7))  # float
print(type(3 + 2j))  # complex

# Arifmetik amallar: +, -, *, /, //, **, %
print("10 // 3 = ", 10 // 3)  # 3
print("10 % 3 = ", 10 % 3)  # 1
print(divmod(10, 3))
# a = 10 // 3
# b = 10 % 3
a, b = divmod(10, 3)  # built-in function
print("a =", a)
print("b =", b)

print(pow(5, 2))  # 25 # built-in function

from math import sqrt  # square root

# import math

x = sqrt(16)
print(x)

print(pow(16, 0.5))
print(16**0.5)

print("-----------------------------------------")

# Comparison operators
# >, <, >=, <=, ==
print(5 > 8)  # False
print(8 > 2)  # True
print(5 == 5)  # True
print("-----------------------------------------")

a = 3
print(a) # 3
a += 6
print(a) # 9

a -= 5
print(a) # 4

# a++ Not Allowed in Python
a += 1
