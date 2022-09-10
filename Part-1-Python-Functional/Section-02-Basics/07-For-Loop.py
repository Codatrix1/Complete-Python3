# --------------
# The For Loop
# --------------

# In JavaScript
# for (i = 0; i < 5; i++) {....}

# In Python, an iterable is an object that is capable of returing values one at a time

# The above can be written in Python, using while

i = 0
while i < 5:
    print(i)
    i += 1
i = None


# Example 1: This is not the same as the for loop written in JS.
# This here, is closest to the while loop written with Python
# ⭐ Its using an ITERABLE, not a collection
for i in range(5):
    print(i)


# Example 2: LIST
for i in ["apple", "orange", "mango"]:
    print(i)

# Example 2: STRING
for char in "morty":
    print(char)

# Example 3: TUPLE
for i in ("z", 455, 678, 90, "x", "y"):
    print(i)

# Example 4: Tuples
for i in [("hello", "there"), (12, 45), (89, 90)]:
    print(i)

"""
('hello', 'there')
(12, 45)
(89, 90)
"""

# Example 6: Tuples
for i, j in [("hello", "there"), (12, 45), (89, 90)]:
    print(i, j)

"""
hello there
12 45
89 90
"""

# -------------------------
# With Break and Continue
# -------------------------

for i in range(5):
    if i == 3:
        continue
    print(i)

"""
0
1
2
4
"""

for i in range(5):
    if i == 3:
        break
    print(i)

"""
0
1
2
"""

# -----------------------------
# Using Break and Else together
# -----------------------------

for i in range(1, 6):
    print(i)
    if i % 6 == 0:
        print("Multiple of 6 found")
        break
else:
    print("No multiples of 6 found")
"""
1
2
3
4
5
No multiples of 6 found
"""

for i in range(1, 7):
    print(i)
    if i % 6 == 0:
        print("Multiple of 6 found")
        break
else:
    print("No multiples of 6 found")

"""
1
2
3
4
5
6
Multiple of 6 found
"""

# ---------------------------------------
# try, except, finally with the For Loop
# ----------------------------------------

for i in range(5):
    print("---------------")
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print("Division by 0")
        continue
    finally:
        print("This always runs")
    print(i)

"""
---------------
This always runs
0
---------------
This always runs
1
---------------
This always runs
2
---------------
Division by 0
This always runs
---------------
This always runs
4
"""

# ---------------------------------------
# Standard ways to iterate an iterable object: like Strings, List, Tuples
# They also are indexable
# ❓ Note: Sets and Dicts have no indexing: They work a bit different: Will See later
# ----------------------------------------

# Typical for loop
greet = "Hello"
for char in greet:
    print(char)

# ------------------
# Indexing through
# ------------------

# Method 1
greet = "there"
i = 0
for eachChar in greet:
    print(eachChar, i)
    i += 1

"""
t 0
h 1
e 2
r 3
e 4
"""

# Method 2: Better way
greet = "there"
for idx in range(len(greet)):
    print(idx, greet[idx])

"""
t 0
h 1
e 2
r 3
e 4
"""

# Method 3: Even better way : enumerate()
greet = "hello"
for idx, eachChar in enumerate(greet):
    print(idx, eachChar)

"""
0 h
1 e
2 l
3 l
4 o
"""
