# If Conditional
my_num = 6

if my_num < 5:
    print("my_num < 5")
else:
    print("my_num >= 5")

# Nested If Conditional
other_num = 8

if other_num < 5:
    print("other_num < 5")
else:
    if other_num < 10:
        print("5 <= other_num < 10 ")
    else:
        print("my_num > 10")

# Else If Conditional
other_num = 17

if other_num < 5:
    print("other_num < 5")
elif other_num < 10:
    print("5 <= other_num < 10")
elif other_num < 15:
    print("10 <= other_num < 15")
elif other_num < 20:
    print("15 <= other_num < 20")
else:
    print("other_num >= 20")


# ---------------------------------
# X if (condition is true) else Y
# ---------------------------------

a = 3

# Example 1
if a < 5:
    b = "a < 5"
else:
    b = "a >= 5"

print(b)

# Example 2
b = "a < 5" if a < 5 else "a >= 5"
print(b)


# Example 3
a = 25

print("a < 5" if a < 5 else "a >= 5")
