# Sets Exercises: Level 1

# Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
length_of_it_companies = len(it_companies)
print("Length of it_companies set:", length_of_it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("it_companies after adding Twitter:", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'Pinterest'])
print("it_companies after adding multiple companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
print("it_companies after removing Twitter:", it_companies)

# What is the difference between remove and discard
# remove() raises a KeyError if the item is not found in the set, while discard() does not raise any error.
it_companies.discard('LinkedIn')  # no error even if LinkedIn does not exist
print("it_companies after discard operation:", it_companies)

# Sets Exercises: Level 2

# Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union_ab = A.union(B)
print("Union of A and B:", union_ab)

# Find A intersection B
intersection_ab = A.intersection(B)
print("Intersection of A and B:", intersection_ab)

# Is A subset of B
is_a_subset_b = A.issubset(B)
print("Is A a subset of B?", is_a_subset_b)

# Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_disjoint)

# Join A with B and B with A
join_a_b = A | B
join_b_a = B | A
print("A joined with B:", join_a_b)
print("B joined with A:", join_b_a)

# What is the symmetric difference between A and B
symmetric_diff_ab = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff_ab)

# Delete the sets completely
del A, B
print("Sets A and B are deleted.")

# Sets Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))

# Explain the difference between the following data types: string, list, tuple, and set
# String: A sequence of characters, immutable.
# List: An ordered collection of items, mutable.
# Tuple: An ordered collection of items, immutable.
# Set: An unordered collection of unique items, mutable.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
unique_words = set(words)
print("Unique words in the sentence:", unique_words)
print("Number of unique words:", len(unique_words))
