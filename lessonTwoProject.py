# Lesson 2: Python Tuples - Engage & Apply + Final Challenge

# ===========================
# engage and apply ---------> Exercise 1 pre-provided
# ===========================

# Pre-provided Exercise: Create a tuple with multiple data types, access the first and last elements, 
# and attempt to modify the tuple to see the immutability error.

my_tuple = (42, "hello", 3.14, True)

# Access and print the first and last elements
print("First element:", my_tuple[0])   # Output: 42
print("Last element:", my_tuple[-1])   # Output: True

# Attempting to modify the tuple to see the immutability error
try:
    my_tuple[1] = "world"  # This should raise an error
except TypeError as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment

# ===========================
# engage and apply ---------> Exercise 1 My Version Created
# ===========================

# My Version: Create a tuple with different data types, 
# access the second and fourth elements, and attempt modification to see the immutability error.

my_tuple = (10, "Python", 3.14, "Code", False)

# Access and print the second and fourth elements
print("Second element:", my_tuple[1])  # Output: Python
print("Fourth element:", my_tuple[3])  # Output: Code

# Attempting to modify the tuple to see the immutability error
try:
    my_tuple[2] = "Changed"  # This should raise an error
except TypeError as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment

# ===========================
# final challenge ---------> pre-provided
# ===========================

# Pre-provided Final Challenge: Create a tuple with at least 6 elements of different data types, 
# access specific elements, slice, count occurrences, unpack, and concatenate tuples.

my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")

# Access and print the third and fifth elements
print("Third element:", my_tuple[2])  # Output: 3.14
print("Fifth element:", my_tuple[4])  # Output: 5

# Slice the tuple from the second to the fifth position
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)  # Output: ('Python', 3.14, 'Code', 5)

# Count occurrences of "Code"
count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)  # Output: 1

# Unpack the tuple into individual variables and print them
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)  # Output: 10 Python 3.14 Code 5 Immutable

# Concatenate the tuple with another tuple
new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)  # Output: (10, 'Python', 3.14, 'Code', 5, 'Immutable', 'New', 'Tuple')

# ===========================
# final challenge ---------> My Version Created
# ===========================

# My Version: Create a tuple with different data types, 
# access specific elements, slice, count occurrences, unpack, and concatenate tuples.

my_tuple = ("Alice", 30, 5.5, "Engineer", "New York", True)

# Access and print the second and sixth elements
print("Second element:", my_tuple[1])  # Output: 30
print("Sixth element:", my_tuple[5])  # Output: True

# Slice the tuple from the third to the sixth position
sliced_tuple = my_tuple[2:6]
print("Sliced tuple:", sliced_tuple)  # Output: (5.5, 'Engineer', 'New York', True)

# Count occurrences of "Engineer"
count_engineer = my_tuple.count("Engineer")
print("Count of 'Engineer':", count_engineer)  # Output: 1

# Unpack the tuple into individual variables and print them
name, age, height, profession, location, is_active = my_tuple
print(name, age, height, profession, location, is_active)  # Output: Alice 30 5.5 Engineer New York True

# Concatenate the tuple with another tuple
new_tuple = my_tuple + ("Python", 2025)
print("Concatenated tuple:", new_tuple)  # Output: ('Alice', 30, 5.5, 'Engineer', 'New York', True, 'Python', 2025)
