# Day 2: 30 Days of python programming

# Declare variables
first_name = "Mustapha"
last_name = "Bari"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Kano"
age = 32
year = 2024
is_married = True
is_true = True
is_light_on = True

# Declare multiple variables on one line
x, y, z = 5, 10, 15

# Check the data types of all variables using type()
print("Data Types:")
print("First Name:", type(first_name))
print("Last Name:", type(last_name))
print("Full Name:", type(full_name))
print("Country:", type(country))
print("City:", type(city))
print("Age:", type(age))
print("Year:", type(year))
print("Is Married:", type(is_married))
print("Is True:", type(is_true))
print("Is Light On:", type(is_light_on))
print("Multiple Variables (x, y, z):", type(x), type(y), type(z))

# Using len() to find the length of the first name
print("\n Length of First Name:", len(first_name))

# Compare the length of the first name and last name
if len(first_name) > len(last_name):
    print("First name is longer.")
elif len(first_name) < len(last_name):
    print("Last name is longer.")
else:
    print("First name and last name are of equal length.")

# Declare numbers
num_one = 5
num_two = 4

# Perform arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Print arithmetic results
print("\nArithmetic Results:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Circle calculations
radius = 30
pi = 3.141592653589793
area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

print("\nCircle Calculations:")
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# User input for radius and calculate area
user_radius = float(input("\nEnter the radius of the circle: "))
user_area_of_circle = pi * user_radius**2
print("Area of Circle with user input radius:", user_area_of_circle)

# Collect user input
first_name_input = input("\nEnter your first name: ")
last_name_input = input("Enter your last name: ")
country_input = input("Enter your country: ")
age_input = input("Enter your age: ")

# Display user input
print("\nUser Input:")
print("First Name:", first_name_input)
print("Last Name:", last_name_input)
print("Country:", country_input)
print("Age:", age_input)

# Check Python reserved keywords
print("\nPython Reserved Keywords:")
help('keywords')
