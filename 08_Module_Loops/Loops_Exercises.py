
#Exercises Level 1

#1. Iterate 0 to 10 using for loop, do the same using while loop.
# Using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
# Using for loop
for i in range(10, -1, -1):
    print(i)

# Using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1
    
#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print('#' * i)
    
#4. Use nested loops to create an 8x8 pattern of #:
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
    
#5. Print multiplication pattern:
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 101, 2):
    print(i)

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101, 2):
    print(i)
    
#Exercises Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
    total_sum += i
print(f"The sum of all numbers is {total_sum}")

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"The sum of all evens is {sum_evens}")
print(f"The sum of all odds is {sum_odds}")

#Exercises Level 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# Access the list from countries.py
from countries import countries

# Filter countries containing "land"
land_countries = [country for country in countries if "land" in country.lower()]
print("Countries containing 'land':", land_countries)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

# Reverse using a loop
reversed_fruits = []
for fruit in reversed(fruits):
    reversed_fruits.append(fruit)

print("Reversed fruits:", reversed_fruits)

#3. Go to the data folder and use the countries_data.py file.
#i. What are the total number of languages in the data
# Access the list from countries_data.py
from countries_data import countries_data

# Find the total number of unique languages
unique_languages = set()
for country in countries_data:
    unique_languages.update(country['languages'])

print(f"Total number of languages: {len(unique_languages)}")

#ii. Find the ten most spoken languages from the data
from collections import Counter
from countries_data import countries_data

# Count occurrences of each language
language_counts = Counter()
for country in countries_data:
    language_counts.update(country['languages'])

# Get the 10 most spoken languages
most_spoken_languages = language_counts.most_common(10)
print("10 most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

#iii. Find the 10 most populated countries in the world
from countries_data import countries_data

# Sort countries by population and select the top 10
most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

# Display the results
print("10 most populated countries:")
for country in most_populated:
    print(f"{country['name']}: {country['population']}")
