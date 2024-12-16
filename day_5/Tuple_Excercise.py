# Tuple Exercises: Level 1

# Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Sarah', 'Amina')
brothers = ('Mustapha', 'Ahmed')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings:", siblings)

# How many siblings do you have?
num_siblings = len(siblings)
print("Number of siblings:", num_siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Ali', 'Fatimah')
print("Family members:", family_members)

# Tuple Exercises: Level 2

# Unpack siblings and parents from family_members
siblings_unpacked, parents_unpacked = family_members[:-2], family_members[-2:]
print("Siblings:", siblings_unpacked)
print("Parents:", parents_unpacked)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'potato', 'spinach')
animal_products = ('milk', 'eggs', 'cheese')

food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[len(food_stuff_tp) // 2] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[len(food_stuff_tp) // 2 - 1: len(food_stuff_tp) // 2 + 1]
print("Middle item(s):", middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp
print("Food stuff tuple deleted.")

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is 'Estonia' a nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is 'Iceland' a nordic country?", is_iceland_nordic)