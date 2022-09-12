"""
⭐ VARIABLES ARE Just Memory References

"""
"""



my_var_1 = 10                                                    

                                                               __MEMORY__
                                reference           0x1000    |__________|
                     my_var_1 ----------------->    0x1001    |____10____|   
                                 0x1001             0x1002    |__________|   
                                                    0x1003    |__________|    
                                reference           0x1004    |__________|   
                     my_var_2 ----------------->    0x1005    |__friend__|    <------ MEMORY HEAP
                                 0x1005             0x1006    |__________|   
                                                    0x1007    |__________|   
                                                    0x1008    |__________|   
                                                    0x0009    |__________|  
my_var_2 = "friend"                                    
                                                       

my_var_1 references the object at 0x1001
my_var_2 references the object at 0x1005


"""
"""
To find the memory address referenced by a variable using id() function
This will return a base-10 number. We can convert this base-10 number to hexadecimal
by using the hex() function

Example 

a = 10
print(hex(id(a)))

"""

my_var = 10

print(id(my_var))  # 2174681416208
print(hex(id(my_var)))  # 0x1ccce560210 # <----Memory address

greet = "hello"
print(id(greet))  # 1579142527856
print(hex(id(greet)))  # 0x16fac3abb70 # <---- Memory address
