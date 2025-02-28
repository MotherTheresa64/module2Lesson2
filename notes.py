# Notes/Examples related to Tuples

# -------------------------> 1. What is a Tuple?
"""
Tuple is a collection of items which is ordered, unchangeable, and heterogeneous. 
(Mix of different data types). Tuples are written with round brackets.
"""

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)  # Output: ('apple', 'banana', 'cherry')


# -------------------------> 2. Why Use Tuples?
"""
- Faster: Tuples are generally faster than lists because they are immutable.
- Safer: Tuples are immutable, preventing accidental changes.
- Dictionary keys: Tuples can be used as keys in a dictionary, while lists can't.
- Function arguments: Tuples are often used as arguments in functions and methods.
"""


# -------------------------> 3. Creating Tuples

# Tuple with mixed data types (using parentheses)
tuple1 = (10, "Python", 3.14)

# Tuple without parentheses (called Tuple Packing)
tuple2 = 10, "Python", 3.14

# Tuple with a single element (comma is necessary)
tuple3 = (10,)

# Empty Tuple
tuple4 = ()

# Output example of a tuple
print(tuple1)  # Output: (10, 'Python', 3.14)
print(tuple2)  # Output: (10, 'Python', 3.14)
print(tuple3)  # Output: (10,)
print(tuple4)  # Output: ()


# -------------------------> 4. Tuple Manipulation

# Accessing elements by index
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana


# -------------------------> 5. Slicing Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)


# -------------------------> 6. Looping over Tuples
my_tuple = (1, 2, 3, 4, 5)
for num in my_tuple:
    print(num)
# Output: 
# 1
# 2
# 3
# 4
# 5


# -------------------------> 7. Tuple Immutability
"""
Tuples are immutable. Once a tuple is created, its elements cannot be modified.
Trying to modify an element will raise an error. However, you can assign a new tuple to a variable.
"""

my_tuple = (10, 20, 30)
my_tuple = (40, 50, 60)  # This is valid since we're creating a new tuple


# -------------------------> 8. Packing and Unpacking Tuples

# Packing a tuple
my_tuple = 3, 4.6, "dog"

person_info = "Alice", 30, "Developer"
print(person_info)  # Output: ('Alice', 30, 'Developer')

# Unpacking a tuple into individual variables
name, age, profession = person_info
print(name)       # Output: Alice
print(age)        # Output: 30
print(profession) # Output: Developer


# -------------------------> 9. Extended Unpacking
"""
In Python, we can use the * operator to unpack values of a tuple into another tuple.
"""

numbers = (1, 2, 3, 4, 5)

# Unpacking with *rest to capture all but the first element
first, *rest = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

# Unpacking with *start to capture all but the last element
*start, last = numbers
print(start)  # Output: [1, 2, 3, 4]
print(last)   # Output: 5


# -------------------------> 10. Ignoring Values with Underscore (_)
"""
If you don't need all values in a tuple, you can use the underscore (_) to ignore them.
"""

person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info  # Ignore age and location

print(name)       # Output: Eve
print(profession) # Output: Artist


# -------------------------> 11. Tuple Packing and Unpacking in Functions
"""
Tuples can be used to return multiple values from a function. The caller can unpack these values.
"""

def get_user_info():
    return "Bob", 29, "Engineer"

# Unpacking the returned tuple
name, age, profession = get_user_info()
print(name)  # Output: Bob


# -------------------------> 12. Passing Multiple Values with Unpacking
"""
You can unpack a tuple while passing it as arguments to a function.
"""

def display_info(name, age, profession):
    print(f"{name} is {age} years old and works as a {profession}.")

info_tuple = ("Charlie", 28, "Designer")

# Unpacking the tuple when calling the function
display_info(*info_tuple)  
# Output: Charlie is 28 years old and works as a Designer.


# -------------------------> 13. Tuple Methods

# .count() method
"""
The .count() method returns the number of times a specified value appears in the tuple.
"""
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3

# .index() method
"""
The .index() method returns the index of the first occurrence of the specified value.
"""
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2
