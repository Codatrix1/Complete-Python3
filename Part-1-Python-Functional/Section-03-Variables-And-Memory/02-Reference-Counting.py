"""
Referene Counting -> By Python Memory Manager
Typically Used while debugging and checking Memory Leaks
"""

"""



my_var_1 = 10                                                                       Reference | Count
                                                          Memory Address            ----------|-------
                                                            __________                0x1003  |   2
                                reference                  |          |                       |  
                     my_var_1 ----------------->           |          |                       |  
                                 0x1003                    |          |   
                                                    0x1003 |    10    |
                                reference                  |          |   
                     my_var_2 ----------------->           |          |     
                                 0x1003                    |__________|            
                                                     
my_var_2 = my_var_1                                    
                                                       

my_var_1 references the object at 0x1003
my_var_2 references the object at 0x1003


"""

# ------------------------------
# Finding the Reference Counts:
# ------------------------------
import sys


a = [1, 2, 3, 4]

print(id(a))  # 2161351703488
print(sys.getrefcount(a))  # 2

# --------------------------------------------

import ctypes


def ref_count(mem_address: int):
    return ctypes.c_long.from_address(mem_address).value


def my_func(x):
    print("inside function:", ref_count(id(x)))


my_new_list = [67, 34, 89]

print("ref_count(my_new_list):", ref_count(id(my_new_list)))  # --> 1
my_func(my_new_list)  # --> 3

"""
when list "my_new_list" is created it is reference count 1.

when user defined function ref_count is called and argument is passed; it first establishes reference to its formal parameter 'my_new_list' (def ref_count(my_new_list)). Thats reference count 2.

Then the formal parameter 'my_new_list' establishes reference to list my_new_list. Thats reference count 3.

"""
# ---------------------------------------------

a = [14, 15, 16]
b = a
print(id(a))  # 2720033878720
print(ref_count(id(a)))  # 2

c = a
print(id(a))  # 2720033878720
print(ref_count(id(a)))  # 3

c = 12
print(id(a))  # 2720033878720
print(ref_count(id(a)))  # 2

b = None
print(id(a))  # 2720033878720
print(ref_count(id(a)))  # 1


a_id = id(a)
a = None
print(ref_count(a_id))  # 0
print(ref_count(a_id))  # 0
