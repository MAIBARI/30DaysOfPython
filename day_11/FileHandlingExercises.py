import json
from collections import Counter
from typing import List, Tuple

# Exercise 1: Count number of lines and words in a text file
def count_lines_and_words(filename: str) -> Tuple[int, int]:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        word_count = sum(len(line.split()) for line in lines)
    return len(lines), word_count

# Example usage for Exercise 1
print("Obama's Speech - Lines and Words:", count_lines_and_words('./data/obama_speech.txt'))
print("Michelle's Speech - Lines and Words:", count_lines_and_words('./data/michelle_obama_speech.txt'))

# Exercise 2: Most spoken languages
def most_spoken_languages(filename: str, n: int) -> List[Tuple[int, str]]:
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    language_counter = Counter()
    for country in countries:
        for language in country['languages']:
            language_counter[language] += 1
    return language_counter.most_common(n)

# Example usage for Exercise 2
print("10 Most Spoken Languages:", most_spoken_languages('./data/countries_data.json', 10))
print("3 Most Spoken Languages:", most_spoken_languages('./data/countries_data.json', 3))

# Exercise 3: Most populated countries
def most_populated_countries(filename: str, n: int) -> List[dict]:
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:n]

# Example usage for Exercise 3
print("10 Most Populated Countries:", most_populated_countries('./data/countries_data.json', 10))
print("3 Most Populated Countries:", most_populated_countries('./data/countries_data.json', 3))

# Exercise 4: Extract all incoming email addresses
def extract_emails(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return list(set(email for email in text.split() if '@' in email))

# Example usage for Exercise 4
print("Extracted Emails:", extract_emails('./data/email_exchanges_big.txt'))

# Exercise 5: Find the most common words
def find_most_common_words(text_or_file: str, n: int) -> List[Tuple[int, str]]:
    if '\n' in text_or_file or ' ' in text_or_file:
        text = text_or_file
    else:
        with open(text_or_file, 'r', encoding='utf-8') as file:
            text = file.read()
    words = text.split()
    word_counter = Counter(words)
    return word_counter.most_common(n)

# Example usage for Exercise 5
print("Most Common Words in Sample:", find_most_common_words('./data/obama_speech.txt', 10))
print("Most Common Words in Sample (Top 5):", find_most_common_words('./data/obama_speech.txt', 5))

# Exercise 6: Check text similarity
def clean_text(text: str) -> str:
    return ''.join(char.lower() for char in text if char.isalnum() or char.isspace())

def remove_support_words(text: str, stop_words_file: str) -> str:
    with open(stop_words_file, 'r', encoding='utf-8') as file:
        stop_words = set(file.read().split())
    return ' '.join(word for word in text.split() if word not in stop_words)

def check_text_similarity(file1: str, file2: str, stop_words_file: str) -> float:
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1, text2 = clean_text(f1.read()), clean_text(f2.read())
    text1, text2 = remove_support_words(text1, stop_words_file), remove_support_words(text2, stop_words_file)
    words1, words2 = set(text1.split()), set(text2.split())
    similarity = len(words1 & words2) / len(words1 | words2)
    return similarity

# Example usage for Exercise 6
print("Text Similarity (Michelle vs Melina):", check_text_similarity('./data/michelle_obama_speech.txt', './data/melina_trump_speech.txt', './data/stop_words.txt'))

# Exercise 7: Most repeated words in "romeo_and_juliet.txt"
def most_repeated_words(filename: str, n: int) -> List[Tuple[int, str]]:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return find_most_common_words(text, n)

# Example usage for Exercise 7
print("Most Repeated Words in Romeo and Juliet:", most_repeated_words('./data/romeo_and_juliet.txt', 10))

# Exercise 8: Analyze hacker news CSV file
def analyze_hacker_news(filename: str) -> Tuple[int, int, int]:
    python_count, javascript_count, java_count = 0, 0, 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if 'python' in line.lower():
                python_count += 1
            if any(variant in line.lower() for variant in ['javascript', 'java script']):
                javascript_count += 1
            elif 'java' in line.lower() and 'javascript' not in line.lower():
                java_count += 1
    return python_count, javascript_count, java_count

# Example usage for Exercise 8
print("Hacker News Analysis:", analyze_hacker_news('./data/hacker_news.csv'))
