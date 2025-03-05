# Lesson 2: Introduction to Python Tuples

# Overview:
# In this lesson, we dive into Python tuples, which are ordered collections of elements. 
# Tuples are similar to lists, but the key difference is that tuples are immutable, meaning 
# once they are created, their values cannot be changed. Tuples are typically used when 
# you need to store a collection of items that should not change.

# Key Concepts:

# 1. **Creating a Tuple**:
# Tuples can be created in several ways:
# - Using parentheses () with comma-separated values:
my_tuple = (1, 2, 3)
# - Without parentheses (tuple packing):
tuple2 = 10, "Python", 3.14
# - Single-element tuples require a trailing comma:
single_element_tuple = (5,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
# - Using the tuple() constructor to convert other iterables:
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# 2. **Accessing Tuple Elements**:
# You can access elements by index, similar to lists. Indexing starts from 0.
print(my_tuple[0])  # Output: 1

# 3. **Tuple Immutability**:
# Since tuples are immutable, trying to modify elements will result in an error.
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10  # Error! Tuples cannot be modified.
except TypeError as e:
    print("Error:", e)

# 4. **Tuple Slicing**:
# Tuples can be sliced to obtain subsets:
print(my_tuple[1:3])  # Output: (2, 3)

# 5. **Packing and Unpacking Tuples**:
# Packing is when values are grouped into a tuple:
person_info = "Alice", 30, "Developer"
# Unpacking is when tuple values are assigned to variables:
name, age, profession = person_info

# 6. **Extended Unpacking**:
# Unpack parts of a tuple into a variable using *:
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]

# 7. **Ignoring Values with Underscore (_)**:
# If you're not interested in some values during unpacking, use _ as a placeholder:
person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info
print(name)       # Output: Eve
print(profession) # Output: Artist

# 8. **Tuple Methods**:
# .count() and .index() are useful methods for working with tuples:
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3
print(my_tuple.index(3))  # Output: 3

# Final Challenge:
# The final challenge reinforces your understanding of tuples by requiring you to create, 
# access, slice, count occurrences, unpack, and concatenate tuples.
