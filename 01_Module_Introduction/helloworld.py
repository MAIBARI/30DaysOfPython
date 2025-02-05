#Exercise: Level 1

# Question 1: Check the python version you are using
# Solution:
import sys
print(sys.version)

# Question 2: Open the python interactive shell and do the following operations. The operands are 3 and 4.
#addition(+)
#subtraction(-)
#multiplication(*)
#modulus(%)
#division(/)
#exponential(**)
#floor division operator(//)
# Solution:
a = 3
b = 4

# Addition
print(a + b)  # 7

# Subtraction
print(a - b)  # -1

# Multiplication
print(a * b)  # 12

# Modulus
print(a % b)  # 3

# Division
print(a / b)  # 0.75

# Exponential
print(a ** b)  # 81

# Floor Division
print(a // b)  # 0

# Question 3: Write strings on the python interactive shell. The strings are the following:
#Your name
#Your family name
#Your country
#I am enjoying 30 days of python

#Solutions
#Variable declaration
my_name = "Mustapha Ashiru Bari"
my_family_name = "Bari"
my_country = "Nigeria"
text = "I am enjoying 30 days of Python"

# Outputs
print(my_name)           # Mustapha Ashiru Bari
print(my_family_name)    # Bari
print(my_country)        # Nigeria
print(text)           # I am enjoying 30 days of Python


# Question 4: Check the data types of the following data:
# - 10
# - 9.8
# - 3.14
# - 4 - 4j
# - ['Asabeneh', 'Python', 'Finland']
# - "Your name", "Your family name", "Your country"

#Solution
print(type(10))                               # <class 'int'>
print(type(9.8))                              # <class 'float'>
print(type(3.14))                             # <class 'float'>
print(type(4 - 4j))                           # <class 'complex'>
print(type(['Asabeneh', 'Python', 'Finland'])) # <class 'list'>
print(type('Your name'))                      # <class 'str'>
print(type('Your family name'))               # <class 'str'>
print(type('Your country'))                   # <class 'str'>



#Exercise: Level 2
# Question 1: Create a folder named `day_1` inside the `30DaysOfPython` folder.

# Question 2: Inside the `day_1` folder, create a Python file named `helloworld.py` and 
# repeat the solutions for Level 1, Questions 1–4.

# Question 3: Use print() for all outputs in the Python file.

# Question 4: Navigate to the directory where your file is saved and run it using:
# python helloworld.py


#Exercise: Level 3
# Question 1: Write examples for the following Python data types:
# - Numbers (Integer, Float, Complex)
# - String
# - Boolean
# - List
# - Tuple
# - Set
# - Dictionary


#Solution

# Numbers
integer_example = 3
float_example = 3.142
complex_example = 4 * 4j

# String
string_example = "Bismillahirrahmanirrahim, Astaghfirullah"

# Boolean
boolean_example = True

# List
list_example = ['Books', 7, 'Biro']

# Tuple
tuple_example = ('one', 'two', 'three')

# Set
set_example = {1, 5, 9}

# Dictionary
dictionary_example = {'python': 300, 'days': 30}

# Outputs
print(integer_example)
print(float_example)
print(complex_example)
print(string_example)
print(boolean_example)
print(list_example)
print(tuple_example)
print(set_example)
print(dictionary_example)

# Question 2: Find an Euclidean distance between (2, 3) and (10, 8).
# Solution:
import numpy as np

# Points
point_1 = [2, 3]
point_2 = [10, 8]

# Calculate Euclidean distance
distance = np.sqrt((point_2[0] - point_1[0])**2 + (point_2[1] - point_1[1])**2)

# Output
print("Euclidean Distance =", distance)  # Euclidean Distance = 9.433981132056603