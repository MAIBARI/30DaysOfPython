# Question 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
concatenated_string_1 = ['Thirty', 'Days', 'Of', 'Python']
concatenated_string_1 = ' '.join(concatenated_string_1)
print(concatenated_string_1)

# Question 2: Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.
concatenated_string_2 = ' '.join(['Coding', 'For', 'All'])
print(concatenated_string_2)

# Question 3: Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Question 4: Print the variable company using print().
print(company)

# Question 5: Print the length of the company string using len() method and print().
print(len(company))

# Question 6: Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Question 7: Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Question 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Question 9: Cut(slice) out the first word of Coding For All string.
print(company[7:])

# Question 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)

# Question 11: Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# Question 12: Change Python for Everyone to Python for All using the replace method or other methods.
string = "Python for Everyone"
print(string.replace("Everyone", "All"))

# Question 13: Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

# Question 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(", "))

# Question 15: What is the character at index 0 in the string Coding For All.
print(company[0])

# Question 16: What is the last index of the string Coding For All.
print(len(company) - 1)

# Question 17: What character is at index 10 in "Coding For All" string.
print(company[10])

# Question 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym1 = ''.join([word[0] for word in "Python For Everyone".split()])
print(acronym1)

# Question 19: Create an acronym or an abbreviation for the name 'Coding For All'.
acronym2 = ''.join([word[0] for word in company.split()])
print(acronym2)

# Question 20: Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# Question 21: Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# Question 22: Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = "Coding For All People"
print(string.rfind("l"))

# Question 23: Use index or find to find the position of the first occurrence of the word 'because' in the sentence.
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))

# Question 24: Use rindex to find the position of the last occurrence of the word because in the sentence.
print(sentence.rindex("because"))

# Question 25: Slice out the phrase 'because because because' in the sentence.
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[:start] + sentence[end:])

# Question 26: Find the position of the first occurrence of the word 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_because_index = sentence.find('because')
print("The position of the first occurrence of 'because':", first_because_index)

# Question 27: Slice out the phrase 'because because because'
# Find the start index of 'because because because'
start_index = sentence.find('because because because')

# Find the end index by adding the length of the phrase
end_index = start_index + len('because because because')

# Slice out the phrase
sliced_phrase = sentence[start_index:end_index]
print("Sliced phrase:", sliced_phrase)


# Question 28: Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# Question 29: Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# Question 30: Remove the left and right trailing spaces in the string '   Coding For All      '.
string = '   Coding For All      '
print(string.strip())

# Question 31: Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython, thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# Question 32: Join the list ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# Question 33: Use the new line escape sequence to separate the sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Question 34: Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# Question 35: Use string formatting to display the following.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Question 36: Make the following using string formatting methods.
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
