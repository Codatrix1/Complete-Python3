# -----------------------------------------------------------------------
# Example 6: __eq__() with __lt__
# -----------------------------------------------------------------------
class RectangleSix:
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
        return f"RectangleSix({self.width}, {self.height})"

    # Modifying Comparison method
    # self: The first original instance, other: Any other instance
    def __eq__(self, other):
        # Making sure that the "other" is the instance of RectangleSix, only then return
        if isinstance(other, RectangleSix):
            return self.width == other.width and self.height == other.height
        else:
            return False

    # Modifying Comparison method: ⭐ Based on Perimeter
    # self: The first original instance, other: Any other instance
    def __lt__(self, other):
        # Making sure that the "other" is the instance of RectangleSix, only then compare
        if isinstance(other, RectangleSix):
            return self.perimeter() < other.perimeter()
        else:
            return NotImplemented


r1 = RectangleSix(10, 20)
r2 = RectangleSix(25, 35)

print(r1 < r2)  # True
print(
    r1 > r2
)  # False : Pythons flips the value and checks even though __gt__ is not undefined
# print(r1 <= r2) # ❌Error: Undefined method: Can be fixed automatically using functools module

# --------------------------------------------------------------------------------------
# Example 7: Setting Pseudoprivate properties, setter, getter methods, Monkey Patching
# ---------------------------------------------------------------------------------------
"""
Monkey patching just means modifying the functionality of objects at "run-time".

Although most custom classes are created declaratively (using the class keyword), you can also modify classes, and objects in general, using a programmatic approach when your code is running.

For example, you can create a class this way:

class Person:
    def __init__(self, name):
        self.name = name
And then you can modify this Person class, programmatically, for example:

Person.say_hello = lambda self: f"hello {self.name}!"

Now, instances of Person will have a method say_hello that was added at run-time (monkey patched):

p = Person('Alex')
p.say_hello()
You can do this because Python is inherently a dynamic language - but be careful with overusing something like this - it can lead to difficult to understand code. Also, you can monkey patch your own custom classes, but Python does not support doing the same with built-in types.
"""


class RectangleSeven:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    def __str__(self):
        return f"Rectangle with width: {self._width} and height: {self._height}"

    def __repr__(self):
        return f"RectangleSeven({self._width}, {self._height})"

    # Modifying Comparison method
    # self: The first original instance, other: Any other instance
    def __eq__(self, other):
        # Making sure that the "other" is the instance of RectangleSeven, only then return
        if isinstance(other, RectangleSeven):
            return self._width == other._width and self._height == other._height
        else:
            return False


r1 = RectangleSeven(25, 35)

# print(r1.width)  # ❌ Error

# ❓ 🐵 Monkey Patching: Adding a property "width" to "r1" at runtime
r1.width = -100

print(r1.width)  # -100
print(r1._width)  # 25

print(repr(r1))  # RectangleSeven(25, 35)
print(r1.get_width())  # 25

# r1.set_width(-10)  # ❌ ValueError: Width must be positive

r1.set_width(100)
print(r1.get_width())  # 100

# --------------------------------------------------------------------------------------------------------
# Example 8: Setting Pseudoprivate properties, with decorators for setter and getters
# To achieve backward compatibility
# 🐛 Pythonic Code: Do not set setters or getters or even private properties if not absolutely necessary
#                   Since Python has to run a method to get those values, instead of directly accessing them.
# --------------------------------------------------------------------------------------------------------


class RectangleEight:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Official Representation
    def __repr__(self):
        return f"RectangleEight({self.width}, {self.height})"

    # Custom string representation
    def __str__(self):
        return f"Rectangle with width: {self._width} and height: {self._height}"

    # To achieve backward compatibility: getters and setters
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width has to be positive")
        else:
            self._width = width

    # To achieve backward compatibility: getters and setters
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height has to be positive")
        else:
            self._height = height

    # Modifying Comparison method
    # self: The first original instance, other: Any other instance
    def __eq__(self, other):
        # Making sure that the "other" is the instance of RectangleEight, only then return
        if isinstance(other, RectangleEight):
            return self.width == other.width and self.height == other.height
        else:
            return False


r1 = RectangleEight(25, 35)
print(r1)
# r1.width = -100 # ValueError: Width has to be positive
# r1.height = -200  # ValueError: Height has to be positive

r1.width = 80
r1.height = 90

print(r1.width)  # 80
print(r1.height)  # 90

print(r1._width)  # 80
print(r1._height)  # 90


print(repr(r1))  # RectangleEight(80, 90)
print(str(r1))  # Rectangle with width: 80 and height: 90

# r2 = RectangleEight(
#     -25, 35
# )  # ValueError: Width has to be positive: Achieved through setters and getters

# r2 = RectangleEight(
#     25, -35
# )  # ValueError: Height has to be positive: Achieved through setters and getters
