# Level 1

# Exercise 1: Age check for driving
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Exercise 2: Compare my_age and your_age
my_age = 25  # Example age
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"You are {age_difference} year younger than me.")
    else:
        print(f"You are {age_difference} years younger than me.")
elif my_age < your_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"I am {age_difference} year younger than you.")
    else:
        print(f"I am {age_difference} years younger than you.")
else:
    print("We are the same age.")

# Exercise 3: Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Level 2

# Exercise 1: Grade assignment
score = int(input("Enter the student's score: "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 89:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
else:
    print("Grade: F")

# Exercise 2: Season check
month = input("Enter the month: ").lower()
if month in ['september', 'october', 'november']:
    print("The season is Autumn.")
elif month in ['december', 'january', 'february']:
    print("The season is Winter.")
elif month in ['march', 'april', 'may']:
    print("The season is Spring.")
elif month in ['june', 'july', 'august']:
    print("The season is Summer.")
else:
    print("Invalid month input.")

# Exercise 3: Add fruit to list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the fruit to check: ").lower()
if fruit not in fruits:
    fruits.append(fruit)
    print("Updated fruit list:", fruits)
else:
    print("That fruit already exists in the list.")


# Level 3

# Exercise 1: Check middle skill
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    middle_skill = person['skills'][len(person['skills']) // 2]
    print(f"The middle skill is: {middle_skill}")

# Exercise 2: Check if Python skill exists
if 'skills' in person and 'Python' in person['skills']:
    print("Python skill exists in the skills list.")

# Exercise 3: Identify job title based on skills
if 'skills' in person:
    skills = person['skills']
    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer.")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer.")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# Exercise 4: Check marital status and location
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
