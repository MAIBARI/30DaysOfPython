#Exercises - Module 3

# Declare variables
age = 30  # Example age
height = 5.9  # Example height in feet
complex_number = 2 + 3j  # Example complex number

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_of_triangle = 0.5 * base * height
print(f"The area of the triangle is {area_of_triangle}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).gle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_of_triangle = a + b + c
print(f"The perimeter of the triangle is {perimeter_of_triangle}")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print(f"The area of the rectangle is {area_of_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_of_rectangle}")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius of the circle: "))
pi = 3.14
area_of_circle = pi * radius**2
circumference_of_circle = 2 * pi * radius
print(f"The area of the circle is {area_of_circle}")
print(f"The circumference of the circle is {circumference_of_circle}")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print(f"Slope: {slope}, x-intercept: {x_intercept}, y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Slope between points: {slope_points}, Euclidean distance: {euclidean_distance}")

# Compare the slopes in tasks 8 and 9.
print(f"Comparison of slopes: {slope} vs {slope_points}")

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-10, 11):  # Testing different x values
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y is 0 when x = {x}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len("python") != len("dragon"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

# There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
length_python = len("python")
length_python_float = float(length_python)
length_python_str = str(length_python_float)
print(f"Length of 'python' as float: {length_python_float}, as string: {length_python_str}")

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python
num = int(input("Enter a number to check if it is even: "))
print(f"The number {num} is even: {num % 2 == 0}")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))
print(int(float('9.8')) == 10)

# Check if int('9.8') is equal to 10
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
print(f"Your weekly earning is {weekly_earning}")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
# Calculate weekly earning
weekly_earning = hours * rate_per_hour
# Display the result
print(f"Your weekly earning is {weekly_earning}")


#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = int(input("Enter number of years you have lived: "))
# Assume there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds in a minute
seconds_in_a_year = 365 * 24 * 60 * 60
# Calculate the total seconds the person has lived
total_seconds_lived = years_lived * seconds_in_a_year
# Display the result
print(f"You have lived for {total_seconds_lived} seconds.")

# Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
