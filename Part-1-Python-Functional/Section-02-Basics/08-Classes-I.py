# --------------------
# Classes in Python
# --------------------

# -----------------------
# Example 1: Basic Class
# -----------------------
class RectangleOne:
    def __init__(self, width, height):
        self.width = width
        self.height = height


r1 = RectangleOne(10, 20)
print(r1.width)  # 10

r1.width = 100
print(r1.width)  # 100

# --------------------------
# Example 2: Adding Methods
# --------------------------
class RectangleTwo:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r2 = RectangleTwo(25, 50)
print(r2.area())  # 1250
print(r2.perimeter())  # 150

print(str(r2))  # <__main__.RectangleTwo object at 0x00000231D2C0FDF0>
print(hex(id(r2)))  # 0x231d2c0fdf0

# ----------------------------------------------
# Example 3: Modifying Built-in Dunder Methods
# ----------------------------------------------

# __str__, __repr__

"""
As far as __repr__ vs __str__ will be covered in an OOP part of this series, not in Part 1.

But basically they do very similar things. Both are used to create string representations of the object. When you use a print statement for example, it will use __str__ (if it is present, otherwise it will fall back to __repr__ if available). __repr__ is used more for debugging and development - it normally includes more information than what the __str__ representation would.

For example, you might have a Person class, and your __str__ representation might just be the name of the person. But your __repr__ representation might include more information including anything relevant to a developer - often we have __repr__ return a string that could be run through eval to create a new instance of the class with the same initial state.

For example:

__str__ --> "John Cleese"

__repr__ --> Person(first='John', last='Cleese', age='42', ssn='xxxx')


"""


class RectangleThree:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # Modifying built-in dunder method: Display human readble format
    def __str__(self):
        return f"Rectange with width: {self.width} and height: {self.height}"

    # # Modifying built-in dunder method: Display Official String Representation of the object
    def __repr__(self):
        return f"RectangeThree({self.width}, {self.height})"


r3 = RectangleThree(35, 60)

print(str(r3))  # Rectange with width: 35 and height: 60
print(r3)  # Rectange with width: 35 and height: 60
print(r3.__str__())  # Rectange with width: 35 and height: 60

print(r3.__repr__())  # RectangeThree(35, 60)

# --------------------------
# Comparing Two instances
# --------------------------
r5 = RectangleThree(10, 20)
r6 = RectangleThree(10, 20)

print(r5 is not r6)  # True
print(r5 == r6)  # False ⭐

# -------------------------------------------------------------
# Example 4: Redefining __eq__() Built-in Comparison Method
# -------------------------------------------------------------
class RectangleFour:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle with width: {self.width} and height: {self.height}"

    def __repr__(self):
        return f"RectangleFour({self.width}, {self.height})"

    # Modifying Comparison method
    # self: The first original instance, other: Any other instance
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


r7 = RectangleFour(40, 50)
r8 = RectangleFour(40, 50)

print(r7 is not r8)  # True: They are different objects at diff memory locations
print(r7 == r8)  # True 🌟🌟: In terms of values, they are same

# print(r7 == 100)  # ❌ AttributeError: 'int' object has no attribute 'width'


# -----------------------------------------------------------------------
# Example 5: Redefining __eq__() Built-in Comparison Method: Refactored
# -----------------------------------------------------------------------
class RectangleFive:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle with width: {self.width} and height: {self.height}"

    def __repr__(self):
        return f"RectangleFive({self.width}, {self.height})"

    # Modifying Comparison method
    # self: The first original instance, other: Any other instance
    def __eq__(self, other):
        # Making sure that the "other" is the instance of RectangleFive, only then return
        if isinstance(other, RectangleFive):
            return self.width == other.width and self.height == other.height
        else:
            return False


r9 = RectangleFive(45, 55)
r10 = RectangleFive(45, 55)

print(r9 is not r10)  # True: They are different objects at diff memory locations
print(r9 == r10)  # True 🌟🌟: In terms of values, they are same

print(r9 == 100)  # False : Now it runs as expected ✔✔
