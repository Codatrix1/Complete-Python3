# While Loop - Repeat the code block as long as the given condition is true
counter = 0

while counter < 5:
    print(counter)
    counter += 1

# -------------------------------------
# Running the while loop atleast once
# -------------------------------------

counter = 5

while True:
    print(f"Result: {counter}")
    if counter >= 5:
        break
        print("Something")

# -------------------------------------
# Question:
# Ask to input for the name:
# It has to be 2 char minimum, should be printable
# and must be alpha numeric
# -------------------------------------
min_length = 2
name = input("Please enter your name: ")

while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")

print(f"Hello, {name}")

# -------------
# Refactored
# -------------

min_length = 2

while True:
    name = input("Enter your name again: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print(f"Welcome {name}! Here and back again")

# -------------------------------------
# ⭐ Continue Statement
# -------------------------------------

num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)

"""
1
3
5
7
9
"""

# ----------------------------------------------
# ⭐ Using else with the while loop, with break
# ----------------------------------------------
"""
Find the given number in the list. 
If the list does not have the number, add number to list
"""

# Using only while

my_list = [1, 3, 5]
val = 10

found = False  # Flag
idx = 0

while idx < len(my_list):
    if my_list[idx] == val:
        found = True  # Flag
        break
    idx += 1

if not found:
    my_list.append(val)

print(my_list)

# ----------------------------
# Better way: Using while else
# ----------------------------

l = [1, 2, 3, 4, 6, 7, 10]
val = int(input("Enter a number to include in the list: "))
idx = 0

while idx < len(l):
    if l[idx] == val:
        print(f"Oops! {val} is already in the list")
        break
    idx += 1
else:
    l.append(val)
    print(f"{val} was added to the list")

print(l)

"""
l = [1, 2, 3, 4, 6, 7, 10]
val = int(input("Enter a number to include in the list: "))

if val in l:
    print(f"Oops! {val} is already in the list")
else:
    l.append(val)
    print(f"{val} was added to the list")

print(l)
"""
