# 🧠📓Engage & Apply: Tuple Exploration ---------------------------------------------------->

# 1. Create a Tuple with different data types
my_tuple = (42, "hello", 3.14, True)

# 2. Access and Print Elements
print("First element:", my_tuple[0])  # Output: 42
print("Last element:", my_tuple[-1])  # Output: True

# 3. Attempt to Modify the Tuple (This will raise an error)
try:
    my_tuple[1] = "world"  # Trying to change the second element
except TypeError as e:
    print(f"Error: {e}")
# Explanation: Tuples are immutable, so modifying them will raise a TypeError.


# 🧠📓 My Version: Tuple Exploration ---------------------------------------------------->

# 1. Create a Tuple with different data types (integer, string, float, boolean)
my_tuple = (25, "Python3", 2.718, False)

# 2. Access and Print Elements (Second and Last)
print("Second element:", my_tuple[1])  # Output: Python3
print("Last element:", my_tuple[-1])   # Output: False

# 3. Attempt to Modify the Tuple (This will raise an error)
try:
    my_tuple[2] = 1.23  # Trying to change the third element
except TypeError as e:
    print(f"Error: {e}")

# Explanation: Tuples are immutable, so modifying them will raise a TypeError.




# 👾💻Final Challenge: Tuple Mastery ---------------------------------------------------->
# 1. Create a Tuple
my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")

# 2. Access and Print Elements
print("Third element:", my_tuple[2])  # Output: 3.14
print("Fifth element:", my_tuple[4])  # Output: 5

# 3. Slice the Tuple
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)  # Output: ('Python', 3.14, 'Code', 5)

# 4. Count Occurrences
count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)  # Output: 1

# 5. Unpack the Tuple
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)  # Output: 10 Python 3.14 Code 5 Immutable

# 6. Concatenate Tuples
new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)  # Output: (10, 'Python', 3.14, 'Code', 5, 'Immutable', 'New', 'Tuple')

# 👾💻 My Version: Tuple Mastery ---------------------------------------------------->

# 1. Create a Tuple with at least 6 elements (mix of integers, strings, floats)
my_tuple = (15, "Data", 1.618, "Science", 10, "Immutable")

# 2. Access and Print Elements (First and Fourth)
print("First element:", my_tuple[0])  # Output: 15
print("Fourth element:", my_tuple[3])  # Output: Science

# 3. Slice the Tuple (Extract elements from 3rd to 6th position)
sliced_tuple = my_tuple[2:6]
print("Sliced tuple:", sliced_tuple)  # Output: (1.618, 'Science', 10, 'Immutable')

# 4. Count Occurrences of 'Science'
count_science = my_tuple.count("Science")
print("Count of 'Science':", count_science)  # Output: 1

# 5. Unpack the Tuple into individual variables
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)  # Output: 15 Data 1.618 Science 10 Immutable

# 6. Concatenate Tuples (Add new elements)
new_tuple = my_tuple + ("New", "Challenge")
print("Concatenated tuple:", new_tuple)  # Output: (15, 'Data', 1.618, 'Science', 10, 'Immutable', 'New', 'Challenge')
