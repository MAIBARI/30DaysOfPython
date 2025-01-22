# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [n for n in numbers if n <= 0]
print("Negative and zero:", negative_and_zero)

# 2. Flatten the following list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("Flattened list:", flattened_list)

# 3. Create the list of tuples using list comprehension
tuples_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of tuples:", tuples_list)

# 4. Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [
    [country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist
]
print("Flattened countries:", flattened_countries)

# 5. Change the following list to a list of dictionaries
countries_dict = [
    {'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist
]
print("List of dictionaries:", countries_dict)

# 6. Change the list of lists to a list of concatenated strings
names = [[('Mustapha', 'Ashiru')], [('Bari', 'Sani')], [('Khadija', 'Ismail')], [('Abba', 'Sani')]]
concatenated_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print("Concatenated names:", concatenated_names)

# 7. Lambda function to solve slope or y-intercept of linear functions
# Formula: y = mx + b
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else "Undefined"
y_intercept = lambda m, x1, y1: y1 - m * x1

# Example usage
x1, y1, x2, y2 = 1, 2, 3, 6
m = slope(x1, y1, x2, y2)
b = y_intercept(m, x1, y1)
print(f"Slope: {m}, Y-intercept: {b}")
