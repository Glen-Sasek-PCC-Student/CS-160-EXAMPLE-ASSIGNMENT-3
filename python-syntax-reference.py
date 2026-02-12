"""
F-STRING SYNOPSIS
F-strings (formatted string literals) are a Python feature for embedding 
expressions inside string literals using curly braces {}.
Introduced in Python 3.6+
"""

# ============================================================================
# BASIC SYNTAX
# ============================================================================
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."
print(message)  # Hello, Alice! You are 30 years old.


# ============================================================================
# EXPRESSIONS
# ============================================================================
# Any valid Python expression can go inside the braces
x = 10
y = 20

print(f"Sum: {x + y}")                    # Sum: 30
print(f"Product: {x * y}")                # Product: 200
print(f"Upper case: {name.upper()}")      # Upper case: ALICE
print(f"Length: {len(name)}")             # Length: 5


# ============================================================================
# FORMAT SPECIFIERS
# ============================================================================
# Control how values are displayed using format spec syntax

# Floating point precision
price = 19.567
print(f"Price: ${price:.2f}")             # Price: $19.57

# Integer padding
num = 42
print(f"Padded: {num:05d}")               # Padded: 00042

# Percentage formatting
ratio = 0.75
print(f"Success: {ratio:.1%}")            # Success: 75.0%

# Alignment
text = "Python"
print(f"Left align:   '{text:<10}'")      # Left align:   'Python    '
print(f"Right align:  '{text:>10}'")      # Right align:   '    Python'
print(f"Center align: '{text:^10}'")      # Center align:  '  Python  '


# ============================================================================
# DEBUG MODE (Python 3.8+)
# ============================================================================
# Use = to show expression and value
x = 42
print(f"{x=}")                            # x=42

# Works with expressions too
print(f"{x + 5=}")                        # x + 5=47


# ============================================================================
# ADVANTAGES OVER OTHER METHODS
# ============================================================================

# vs. .format() method
user = "Bob"
score = 95

# Old way
print("User: {}, Score: {}".format(user, score))
# New way (cleaner)
print(f"User: {user}, Score: {score}")


# vs. % formatting
# Old way
print("Hello %s, age %d" % ("Charlie", 25))
# New way (more readable)
print(f"Hello {name}, age {age}")


# ============================================================================
# KEY FEATURES SUMMARY
# ============================================================================
"""
1. READABLE: Variables appear directly in context
2. FAST: More performant than .format() or % formatting
3. FLEXIBLE: Supports complex expressions and format specs
4. INTUITIVE: Easy to understand and write
5. POWERFUL: Can include function calls, conditionals, and calculations
"""


# ============================================================================
# ARRAY/LIST SYNOPSIS
# ============================================================================
"""
ARRAYS IN PYTHON
In Python, the primary data structure for collections is the LIST.
Lists are ordered, mutable (changeable), and can hold items of different types.
"""

# ============================================================================
# CREATING LISTS
# ============================================================================
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
from_range = list(range(5))              # [0, 1, 2, 3, 4]

print(fruits)                             # ['apple', 'banana', 'cherry']
print(from_range)                         # [0, 1, 2, 3, 4]


# ============================================================================
# ACCESSING ELEMENTS
# ============================================================================
# Indexing (0-based)
first = fruits[0]                         # "apple"
last = fruits[-1]                         # "cherry" (last element)
second_from_end = fruits[-2]              # "banana"

print(f"First fruit: {first}")
print(f"Last fruit: {last}")


# ============================================================================
# MODIFYING LISTS
# ============================================================================
# Change an element
fruits[1] = "blueberry"                   # ['apple', 'blueberry', 'cherry']

# Add elements
fruits.append("date")                     # Adds to end
fruits.insert(0, "avocado")               # Inserts at index 0

# Remove elements
fruits.remove("blueberry")                # Removes first occurrence
removed = fruits.pop()                    # Removes and returns last element
del fruits[0]                             # Deletes element at index 0

print(fruits)


# ============================================================================
# SLICING
# ============================================================================
items = [10, 20, 30, 40, 50]
subset = items[1:4]                       # [20, 30, 40] (index 1-3)
first_three = items[:3]                   # [10, 20, 30]
from_index_2 = items[2:]                  # [30, 40, 50]
every_other = items[::2]                  # [10, 30, 50]
reversed_list = items[::-1]               # [50, 40, 30, 20, 10]

print(f"Subset: {subset}")
print(f"Reversed: {reversed_list}")


# ============================================================================
# COMMON LIST METHODS
# ============================================================================
nums = [3, 1, 4, 1, 5, 9]

nums.sort()                               # Sorts in place: [1, 1, 3, 4, 5, 9]
sorted_nums = sorted(nums)                # Returns sorted copy
reversed_nums = list(reversed(nums))      # Returns reversed copy
count = nums.count(1)                     # Count occurrences: 2
index = nums.index(4)                     # Find first index of value
nums.extend([2, 6])                       # Add multiple items
length = len(nums)                        # Get length

print(f"Sorted: {sorted_nums}")
print(f"Count of 1s: {count}")
print(f"Length: {length}")


# ============================================================================
# ITERATION
# ============================================================================
# For loop with items
colors = ["red", "green", "blue"]
for color in colors:
    print(f"Color: {color}")

# For loop with index
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

# Enumerate (index and value)
for i, color in enumerate(colors):
    print(f"Index {i}: {color}")


# ============================================================================
# LIST COMPREHENSIONS
# ============================================================================
# Create lists efficiently with compact syntax

squares = [x**2 for x in range(1, 6)]     # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
upper = [word.upper() for word in ["hello", "world"]]  # ['HELLO', 'WORLD']

print(f"Squares: {squares}")
print(f"Evens: {evens}")
print(f"Upper: {upper}")


# ============================================================================
# KEY FEATURES SUMMARY
# ============================================================================
"""
LISTS (Python's "Arrays"):
1. ORDERED: Elements have positions (index 0, 1, 2, ...)
2. MUTABLE: Can add, remove, or modify elements
3. FLEXIBLE: Can hold different data types
4. INDEXED: Access elements by position
5. SLICEABLE: Extract subsets with slice notation
6. ITERABLE: Loop through elements easily
7. METHODS: Built-in methods for common operations
"""


# ============================================================================
# FUNCTION SYNOPSIS
# ============================================================================
"""
FUNCTIONS IN PYTHON
Functions are reusable blocks of code that perform specific tasks.
They help organize code, reduce repetition, and improve readability.
"""

# ============================================================================
# BASIC FUNCTION DEFINITION
# ============================================================================
def greet():
    """Simple function with no parameters."""
    print("Hello, World!")

greet()  # Call the function


def add(a, b):
    """Function that takes two parameters and returns a result."""
    return a + b

result = add(5, 3)                        # result = 8
print(f"Sum: {result}")


# ============================================================================
# PARAMETERS AND ARGUMENTS
# ============================================================================
# Positional arguments
def describe(name, age):
    return f"{name} is {age} years old"

print(describe("Alice", 30))               # Alice is 30 years old


# Default parameters
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_person("Bob"))                 # Hello, Bob!
print(greet_person("Bob", "Hi"))           # Hi, Bob!


# Keyword arguments (order doesn't matter)
def create_profile(name, age, city):
    return f"{name}, {age}, from {city}"

print(create_profile(age=25, name="Charlie", city="NYC"))


# Variable-length arguments *args
def sum_all(*numbers):
    """Accepts any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))              # 15


# Keyword arguments **kwargs
def print_info(**info):
    """Accepts keyword arguments as a dictionary."""
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Diana", age=28, city="LA")


# ============================================================================
# RETURN VALUES
# ============================================================================
def get_coordinates():
    """Return multiple values as a tuple."""
    return 10, 20

x, y = get_coordinates()                   # Tuple unpacking
print(f"Coordinates: ({x}, {y})")

def divide(a, b):
    """Return None or early exit."""
    if b == 0:
        return                             # Returns None
    return a / b

result = divide(10, 2)                     # 5.0
result = divide(10, 0)                     # None


# ============================================================================
# DOCSTRINGS
# ============================================================================
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle (length * width)
    """
    return length * width

print(calculate_area(5, 10))               # 50
print(calculate_area.__doc__)             # Display docstring


# ============================================================================
# VARIABLE SCOPE
# ============================================================================
global_var = "I'm global"

def demo_scope():
    local_var = "I'm local"               # Only exists inside function
    print(global_var)                      # Can access global variable
    print(local_var)

demo_scope()
# print(local_var)                         # ERROR: local_var not defined here

def modify_global():
    global global_var                      # Declare intent to modify global
    global_var = "Modified globally"

modify_global()
print(global_var)                          # Modified globally


# ============================================================================
# LAMBDA FUNCTIONS (Anonymous Functions)
# ============================================================================
# Short, one-line functions

square = lambda x: x ** 2
print(square(5))                           # 25

# Useful with map, filter, sorted
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

print(f"Doubled: {doubled}")
print(f"Evens: {evens}")

# Sort by custom key
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
sorted_students = sorted(students, key=lambda x: x[1])  # Sort by grade
print(sorted_students)


# ============================================================================
# NESTED FUNCTIONS
# ============================================================================
def outer(x):
    """Outer function."""
    def inner(y):
        """Inner function has access to outer variables."""
        return x + y
    return inner

add_5 = outer(5)                           # Returns inner function with x=5
print(add_5(3))                            # Calls inner(3) = 5 + 3 = 8


# ============================================================================
# KEY FEATURES SUMMARY
# ============================================================================
"""
FUNCTIONS:
1. REUSABLE: Define once, use many times
2. ORGANIZED: Group related code
3. PARAMETERIZED: Pass data via arguments
4. FLEXIBLE: Positional, default, *args, **kwargs
5. DOCUMENTED: Use docstrings to explain purpose
6. SCOPED: Local and global variable management
7. RETURNABLE: Can return one or multiple values
8. COMPOSABLE: Functions can call other functions
"""


# ============================================================================
# OPERATOR SYNOPSIS
# ============================================================================
"""
OPERATORS IN PYTHON
Operators are symbols used to perform operations on values and variables.
They perform arithmetic, comparison, logical, assignment, and bitwise operations.
"""

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================
# Perform mathematical calculations

a = 10
b = 3

addition = a + b                           # 13
subtraction = a - b                        # 7
multiplication = a * b                     # 30
division = a / b                           # 3.3333... (float)
floor_division = a // b                    # 3 (integer division)
modulo = a % b                             # 1 (remainder)
exponent = a ** b                          # 1000 (10^3)

print(f"Addition: {addition}")
print(f"Floor Division: {floor_division}")
print(f"Modulo: {modulo}")
print(f"Exponent: {exponent}")


# ============================================================================
# COMPARISON OPERATORS
# ============================================================================
# Compare two values and return True/False

x = 5
y = 10

print(f"{x} == {y}: {x == y}")              # False (equal to)
print(f"{x} != {y}: {x != y}")              # True (not equal to)
print(f"{x} < {y}: {x < y}")               # True (less than)
print(f"{x} > {y}: {x > y}")               # False (greater than)
print(f"{x} <= {y}: {x <= y}")             # True (less than or equal)
print(f"{x} >= {y}: {x >= y}")             # False (greater than or equal)


# ============================================================================
# LOGICAL OPERATORS
# ============================================================================
# Combine or negate boolean values

is_student = True
has_scholarship = False

result = is_student and has_scholarship    # False (both must be True)
result = is_student or has_scholarship     # True (at least one must be True)
result = not is_student                    # False (negates the value)

print(f"True and False: {is_student and has_scholarship}")
print(f"True or False: {is_student or has_scholarship}")
print(f"not True: {not is_student}")

# Chaining comparisons
age = 25
is_adult = 18 <= age < 65                  # True
print(f"Is adult working age: {is_adult}")


# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================
# Assign and modify values

value = 5                                  # =   (assign)
value += 3                                 # +=  (add and assign) = 8
value -= 2                                 # -=  (subtract and assign) = 6
value *= 2                                 # *=  (multiply and assign) = 12
value /= 3                                 # /=  (divide and assign) = 4.0
value //= 2                                # //= (floor divide and assign) = 2.0
value %= 3                                 # %=  (modulo and assign) = 2.0
value **= 2                                # **= (exponent and assign) = 4.0

print(f"Final value: {value}")


# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================
# Check if a value exists in a sequence

fruits = ["apple", "banana", "cherry"]
search = "apple"

is_in = search in fruits                   # True
is_not_in = search not in fruits           # False

print(f"'apple' in fruits: {is_in}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# Works with strings
text = "Python"
print(f"'P' in 'Python': {'P' in text}")


# ============================================================================
# IDENTITY OPERATORS
# ============================================================================
# Check if two variables refer to the same object

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

is_same = list1 is list3                   # True (same object)
is_not_same = list1 is list2               # False (different objects, same content)

print(f"list1 is list3: {is_same}")
print(f"list1 is list2: {is_not_same}")
print(f"list1 == list2: {list1 == list2}")  # True (equal content)

# Checking for None
value = None
print(f"value is None: {value is None}")
print(f"value is not None: {value is not None}")


# ============================================================================
# BITWISE OPERATORS
# ============================================================================
# Operate on binary representations of integers

a = 12                                     # Binary: 1100
b = 10                                     # Binary: 1010

print(f"{a} & {b} = {a & b}")              # & (AND) = 8 (1000)
print(f"{a} | {b} = {a | b}")              # | (OR) = 14 (1110)
print(f"{a} ^ {b} = {a ^ b}")              # ^ (XOR) = 6 (0110)
print(f"~{a} = {~a}")                      # ~ (NOT) = -13
print(f"{a} << 1 = {a << 1}")              # << (Left shift) = 24
print(f"{a} >> 1 = {a >> 1}")              # >> (Right shift) = 6


# ============================================================================
# OPERATOR PRECEDENCE
# ============================================================================
"""
Order of evaluation (highest to lowest):
1. ** (Exponentiation)
2. +x, -x, ~x (Unary operators)
3. *, /, //, % (Multiplication, Division, etc.)
4. +, - (Addition, Subtraction)
5. <<, >> (Bitwise shifts)
6. & (Bitwise AND)
7. ^ (Bitwise XOR)
8. | (Bitwise OR)
9. ==, !=, <, >, <=, >= (Comparisons)
10. is, is not, in, not in (Identity, Membership)
11. not (Logical NOT)
12. and (Logical AND)
13. or (Logical OR)

Use parentheses to clarify/override precedence:
"""

result = 2 + 3 * 4                         # 14 (* before +)
result = (2 + 3) * 4                       # 20 (parentheses override)

print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")


# ============================================================================
# KEY FEATURES SUMMARY
# ============================================================================
"""
OPERATORS:
1. ARITHMETIC: +, -, *, /, //, %, **
2. COMPARISON: ==, !=, <, >, <=, >=
3. LOGICAL: and, or, not
4. ASSIGNMENT: =, +=, -=, *=, /=, //=, %=, **=
5. MEMBERSHIP: in, not in
6. IDENTITY: is, is not
7. BITWISE: &, |, ^, ~, <<, >>
8. PRECEDENCE: ** > *, /, //, % > +, - > comparisons > logical
9. CHAINING: Comparisons can be chained (a < b < c)
10. OVERLOADABLE: Custom classes can override operator behavior
"""


