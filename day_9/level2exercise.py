# Exercise 1: evens_and_odds
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of evens are {evens}. The number of odds are {odds}."

print(evens_and_odds(100))

# Exercise 2: factorial
import math

def factorial(n):
    if n == 0:
        return 1
    return math.factorial(n)

num = int(input("Enter a number to find its factorial: "))
print("Factorial:", factorial(num))

# Exercise 3: is_empty
def is_empty(param):
    return not param

test_param = input("Enter something to check if it's empty: ")
print("Is empty?", is_empty(test_param))

# Exercise 4: Statistical calculations
from collections import Counter

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    return sorted_lst[mid]

def calculate_mode(lst):
    freq = Counter(lst)
    max_count = max(freq.values())
    mode = [key for key, count in freq.items() if count == max_count]
    return mode

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    variance = calculate_variance(lst)
    return math.sqrt(variance)

numbers = list(map(float, input("Enter numbers separated by space: ").split()))
print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers))
