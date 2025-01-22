import math
from collections import Counter

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(29))

# 2. Write a function which checks if all items are unique in the list.
def are_items_unique(lst):
    return len(lst) == len(set(lst))

print(are_items_unique([1, 2, 3, 4, 5])) 

# 3. Write a function which checks if all the items of the list are of the same data type.
def are_items_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

print(are_items_same_type([1, 2, 3, 4])) 

# 4. Write a function which checks if provided variable is a valid python variable.
def is_valid_variable(var):
    import keyword
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True

print(is_valid_variable("variable_name"))  

# 5. Create a function called the most_spoken_languages in the world.
from countries_data import countries_data

def most_spoken_languages(n):
    language_count = Counter()
    for country in countries_data:
        language_count.update(country["languages"])
    return language_count.most_common(n)

print(most_spoken_languages(10)) 

# 6. Create a function called the most_populated_countries.
def most_populated_countries(n):
    sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:n]

print(most_populated_countries(10))  