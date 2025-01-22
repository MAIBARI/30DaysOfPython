import math

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Sum:", add_two_numbers(num1, num2))   

# 2. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return math.pi * r * r

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area_of_circle(radius))   

# 3. Write a function called add_all_nums.
def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    else:
        return "All arguments must be numbers."

numbers = input("Enter numbers separated by space: ").split()
numbers = [float(num) for num in numbers]
print("Sum of numbers:", add_all_nums(*numbers))   

# 4. Write a function which converts °C to °F.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", convert_celsius_to_fahrenheit(celsius))   

# 5. Write a function called check_season.
def check_season(month):
    seasons = {
        "Winter": ["December", "January", "February"],
        "Spring": ["March", "April", "May"],
        "Summer": ["June", "July", "August"],
        "Autumn": ["September", "October", "November"]
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Invalid month"

month = input("Enter a month: ")
print("Season:", check_season(month))   

# 6. Write a function called calculate_slope.
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined."
    return (y2 - y1) / (x2 - x1)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
print("Slope:", calculate_slope(x1, y1, x2, y2))   

# 7. Write a function which calculates the solution set of a quadratic equation.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
print("Solutions:", solve_quadratic_eqn(a, b, c))   

# 8. Declare a function named print_list.
def print_list(lst):
    for item in lst:
        print(item)

items = input("Enter items separated by space: ").split()
print_list(items)   

# 9. Declare a function named reverse_list.
def reverse_list(array):
    reversed_array = []
    for i in range(len(array) - 1, -1, -1):
        reversed_array.append(array[i])
    return reversed_array

array = input("Enter elements separated by space: ").split()
print("Reversed list:", reverse_list(array))   

# 10. Declare a function named capitalize_list_items.
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

items = input("Enter items separated by space: ").split()
print("Capitalized list:", capitalize_list_items(items))   

# 11. Declare a function named add_item.
def add_item(lst, item):
    lst.append(item)
    return lst

items = input("Enter items separated by space: ").split()
item_to_add = input("Enter item to add: ")
print("Updated list:", add_item(items, item_to_add))   

# 12. Declare a function named remove_item.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

items = input("Enter items separated by space: ").split()
item_to_remove = input("Enter item to remove: ")
print("Updated list:", remove_item(items, item_to_remove))   

# 13. Declare a function named sum_of_numbers.
def sum_of_numbers(n):
    return sum(range(1, n + 1))

n = int(input("Enter a number: "))
print("Sum of numbers:", sum_of_numbers(n))   

# 14. Declare a function named sum_of_odds.
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

n = int(input("Enter a number: "))
print("Sum of odd numbers:", sum_of_odds(n))   

# 15. Declare a function named sum_of_even.
def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

n = int(input("Enter a number: "))
print("Sum of even numbers:", sum_of_even(n))   
