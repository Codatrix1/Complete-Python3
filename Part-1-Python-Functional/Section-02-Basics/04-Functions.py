# -------------------------------
# Built In Functions in Python
# -------------------------------
from math import sqrt
import math

print(sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793
print(math.exp(1))  # 2.718281828459045

my_list = [1, 3, 4, 5, 6, 7]
print(len(my_list))  # 6

# ------------
# Functions
# ------------

# Example 1
def func_one():
    return "running func_one"


print(func_one)  # <function func_one at 0x0000013017E2FC70>
print(func_one())  # running func_one

# Example 2
def func_two(a, b):
    return a * b


print(func_two(4, 6))  # 24
print(func_two([1, 2, 3], 3))  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(func_two("hello", "there"))  # ❌ Errors Out" Due to Polymorphism: OOP

# Example 3
# With Annotations: For documentation only if not using a type checker like mypy
def func_three(a: int, b: float):
    return a * b


print(func_three("Hello", 2))  # HelloHello

# ---------------------------
# Functions within functions
# ---------------------------

# -----
# ✔✔
# -----
def func_4():
    return func_5()


def func_5():
    return "Running func_5"


print(func_4())  # Running func_5

# ----------------
# ❌ ERRORS OUT
# ---------------
"""
def func_6():
    return func_7()


print(func_6())  # Error


def func_7():
    return "Running func_7"

"""

# -------------------
# Assigning Functions
# -------------------


def func_8():
    return func_9()


def func_9():
    return "Running func_9"


print(func_8())  # Running func_9

my_func = func_8
print(my_func())  # Running func_9


# ---------------------------
# Lambda Functions: Anonymous
# ---------------------------
# Can't have large code blocks
print(lambda x: x * 2)  # <function <lambda> at 0x000001F7E01000D0>

fn1 = lambda x: x**3
print(fn1(3))  # 27
