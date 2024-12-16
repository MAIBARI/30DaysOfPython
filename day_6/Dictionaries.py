# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Rex'
dog['color'] = 'brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'Machine Learning'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# 4. Get the length of the student dictionary
student_length = len(student)
print("Student dictionary length:", student_length)

# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
skills_type = type(skills)
print("Data type of skills:", skills_type)

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Data Science')
student['skills'].append('AI')
print("Updated skills:", student['skills'])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Student dictionary keys:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("Student dictionary values:", values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary items:", student_items)

# 10. Delete one of the items in the dictionary
del student['address']
print("Student dictionary after deleting address:", student)

# 11. Delete the student dictionary
del student
