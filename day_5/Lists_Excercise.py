# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
sample_list = [1, 2, 3, 4, 5, 6, 7]

# Find the length of your list
length_of_list = len(sample_list)

# Get the first item, the middle item, and the last item of the list
first_item = sample_list[0]
middle_item = sample_list[len(sample_list) // 2]
last_item = sample_list[-1]

# Declare a list called mixed_data_types
mixed_data_types = ["John Doe", 30, 5.8, "Single", "123 Main St"]

# Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list
print(it_companies)

# Print the number of companies in the list
number_of_companies = len(it_companies)
print(number_of_companies)

# Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(first_company, middle_company, last_company)

# Print the list after modifying one of the companies
it_companies[1] = "Alphabet"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Netflix")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Tesla")
print(it_companies)

# Change one of the it_companies names to uppercase (excluding IBM)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#; '
joined_companies = "#; ".join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list
company_exists = "Google" in it_companies
print(company_exists)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# Slice out the middle IT company or companies from the list
middle_start = len(it_companies) // 2
middle_slice = it_companies[middle_start:middle_start+1] if len(it_companies) % 2 != 0 else it_companies[middle_start-1:middle_start+1]
print(middle_slice)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 != 0:
    it_companies.pop(middle_index)
else:
    del it_companies[middle_index-1:middle_index+1]
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
joined_list = front_end + back_end
print(joined_list)

# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux
full_stack = joined_list[:]
redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print(full_stack)


#Exercise Level 2 solutions
# Given data
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorting the list
ages.sort()
print("Sorted ages:", ages)

# Finding the min and max age
min_age = min(ages)
max_age = max(ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Adding the min and max age again to the list
ages.append(min_age)
ages.append(max_age)

# Finding the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median_age = ages[n//2]
print("Median age:", median_age)

# Finding the average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# Finding the range of the ages
age_range = max_age - min_age
print("Age range:", age_range)

# Comparing min - average and max - average using abs()
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Min diff from average:", min_diff)
print("Max diff from average:", max_diff)

# Countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries)

# Finding the middle country(ies)
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index-1:middle_index+1]
else:
    middle_countries = countries[middle_index]
print("Middle countries):", middle_countries)

# Dividing the countries list into two equal parts
half_1 = countries[:middle_index + 1]
half_2 = countries[middle_index + 1:]
print("First half of countries:", half_1)
print("Second half of countries:", half_2)

# Unpacking the first three countries
first_three, *scandic_countries = countries
print("First three countries:", first_three)

# Results
(min_age, max_age, ages, median_age, average_age, age_range, min_diff, max_diff, middle_countries, half_1, half_2, first_three, scandic_countries)
print("Scandic countries:", scandic_countries)
