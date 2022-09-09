# try...except...finally

a = 10
b = 2

try:
    print(f"Result {a / b}")
except ZeroDivisionError:
    print("Division by 0")
finally:
    print("This always runs, no matter what")

"""
Output:

Result 5.0
This always runs, no matter what

"""


"""
Using try..except...finally

Take two numbers: 
a = 0
b = 2
Increment a by 1 and Decrease b by 1,
Catch ZeroDivisionError

"""
# --------------------------------------------------------------------------
# If in a try block, with a continue statement, the finally will always run
# ⭐ Use Case:
"""
That means that if you need to make sure that you close a file or close the database connection, for some reason, you will maybe rollback back a transaction or do something when the after you're done trying to deal with whatever it is in that particular loop iteration, then you're assured that the
finally will run, whether you had an exception or not.
"""
# ---------------------------------------------------------------------------
a = 0
b = 2

while a < 4:
    print("---------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(f"{a}, {b}: Zero division error")
        continue
    finally:
        print(f"{a}, {b}: This always executes")

    # if continue is there, this line will not be reached
    print(f"{a}, {b}: Main Loop")

"""
Output:

---------------
1, 1: This always executes
1, 1: Main Loop
---------------
2, 0: Zero division error
2, 0: This always executes
---------------
3, -1: This always executes
3, -1: Main Loop
---------------
4, -2: This always executes
4, -2: Main Loop
"""

# ---------------------------------
# Using break instead of continue
# ---------------------------------
a = 0
b = 2

while a < 4:
    print("---------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(f"{a}, {b}: Zero division error")
        break
    finally:
        print(f"{a}, {b}: This always executes")

    # if break is there, this line will not be reached
    print(f"{a}, {b}: Main Loop")

"""
Output:

---------------
1, 1: This always executes
1, 1: Main Loop
---------------
2, 0: Zero division error
2, 0: This always executes
"""

# ---------------------------------------
# Using break, else with no divison error
# ----------------------------------------
a = 0
b = 10

while a < 4:
    print("---------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(f"{a}, {b}: Zero division error")
        break
    finally:
        print(f"{a}, {b}: This always executes")

    # if break is there, this line will not be reached
    print(f"{a}, {b}: Main Loop")

else:
    print("Successful code execution: No Zero Divison Error")

"""
Output:

---------------
1, 9: This always executes
1, 9: Main Loop
---------------
2, 8: This always executes
2, 8: Main Loop
---------------
3, 7: This always executes
3, 7: Main Loop
---------------
4, 6: This always executes
4, 6: Main Loop
Successful code execution: No Zero Divison Error
"""
