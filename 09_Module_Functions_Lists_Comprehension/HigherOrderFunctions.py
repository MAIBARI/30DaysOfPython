from functools import reduce
from operator import itemgetter

# Data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# 1. Explain the difference between map, filter, and reduce:
#    - map: Applies a given function to each item in an iterable and returns a map object (iterable).
#    - filter: Filters items from an iterable based on a function returning True or False.
#    - reduce: Applies a rolling computation to the items of an iterable, reducing them to a single value.

# 2. Explain the difference between higher-order function, closure, and decorator:
#    - Higher-order function: A function that takes another function as an argument or returns one.
#    - Closure: A function that retains access to its enclosing scope, even after the outer function has finished execution.
#    - Decorator: A design pattern in Python used to extend the functionality of a function without modifying it.

# 3. Define a call function before map, filter, or reduce:
def square(x):
    return x ** 2

# 4. Use for loop to print each country in the countries list
for country in countries:
    print(country)

# 5. Use for loop to print each name in the names list
for name in names:
    print(name)

# 6. Use for loop to print each number in the numbers list
for number in numbers:
    print(number)

# Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase
countries_uppercase = list(map(str.upper, countries))
print("Uppercase countries:", countries_uppercase)

# 2. Use map to create a new list by changing each number to its square
numbers_squared = list(map(square, numbers))
print("Squared numbers:", numbers_squared)

# 3. Use map to change each name to uppercase
names_uppercase = list(map(str.upper, names))
print("Uppercase names:", names_uppercase)

# 4. Use filter to filter out countries containing 'land'
countries_with_land = list(filter(lambda x: 'land' in x, countries))
print("Countries with 'land':", countries_with_land)

# 5. Use filter to filter out countries having exactly six characters
countries_six_chars = list(filter(lambda x: len(x) == 6, countries))
print("Countries with exactly six characters:", countries_six_chars)

# 6. Use filter to filter out countries containing six letters or more
countries_six_or_more = list(filter(lambda x: len(x) >= 6, countries))
print("Countries with six or more characters:", countries_six_or_more)

# 7. Use filter to filter out countries starting with 'E'
countries_starting_e = list(filter(lambda x: x.startswith('E'), countries))
print("Countries starting with 'E':", countries_starting_e)

# 8. Chain two or more list iterators
chained_result = reduce(lambda x, y: x + y, filter(lambda z: z > 5, map(lambda x: x * 2, numbers)))
print("Chained result:", chained_result)

# 9. Declare get_string_lists function
def get_string_lists(lst):
    return [x for x in lst if isinstance(x, str)]

print("String list:", get_string_lists([1, 'two', 3, 'four']))

# 10. Use reduce to sum all numbers
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

# 11. Use reduce to concatenate all countries
countries_sentence = f"{reduce(lambda x, y: x + ', ' + y, countries[:-1])}, and {countries[-1]} are north European countries"
print("Countries sentence:", countries_sentence)

# 12. Declare categorize_countries
def categorize_countries(pattern):
    return [country for country in countries if pattern in country]

print("Countries with 'land':", categorize_countries('land'))

# 13. Create a function returning a dictionary with starting letters of countries
def country_initials_count():
    return {char: sum(1 for country in countries if country.startswith(char)) for char in set(c[0] for c in countries)}

print("Country initials count:", country_initials_count())

# 14. Declare get_first_ten_countries
def get_first_ten_countries():
    return countries[:10]

print("First ten countries:", get_first_ten_countries())

# 15. Declare get_last_ten_countries
def get_last_ten_countries():
    return countries[-10:]

print("Last ten countries:", get_last_ten_countries())

# Exercises: Level 3

from countries_data import countries_data

# 1. Sort countries by name, by capital, by population
sorted_by_name = sorted(countries_data, key=itemgetter('name'))
sorted_by_capital = sorted(countries_data, key=itemgetter('capital'))
sorted_by_population = sorted(countries_data, key=itemgetter('population'), reverse=True)

print("Countries sorted by name:", [country['name'] for country in sorted_by_name[:10]])
print("Countries sorted by capital:", [country['capital'] for country in sorted_by_capital[:10]])
print("Countries sorted by population:", [(country['name'], country['population']) for country in sorted_by_population[:10]])

# 2. Sort out the ten most spoken languages
language_count = {}
for country in countries_data:
    for language in country['languages']:
        language_count[language] = language_count.get(language, 0) + 1

most_spoken_languages = sorted(language_count.items(), key=itemgetter(1), reverse=True)[:10]
print("Most spoken languages:", most_spoken_languages)

# 3. Sort out the ten most populated countries
print("Ten most populated countries:", [(country['name'], country['population']) for country in sorted_by_population[:10]])
