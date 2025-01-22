def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_unique(lst):
    return len(lst) == len(set(lst))

def all_same_type(lst):
    return all(isinstance(x, type(lst[0])) for x in lst)

def is_valid_variable(var):
    import keyword
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True

def most_spoken_languages(n=10):
    languages = [
        "English", "Mandarin Chinese", "Hindi", "Spanish", "French",
        "Standard Arabic", "Bengali", "Russian", "Portuguese", "Urdu",
        "Indonesian", "German", "Japanese", "Swahili", "Marathi",
        "Telugu", "Turkish", "Tamil", "Vietnamese", "Korean"
    ]
    return languages[:n]

def most_populated_countries(n=10):
    countries = [
        "China", "India", "United States", "Indonesia", "Pakistan",
        "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico",
        "Japan", "Ethiopia", "Philippines", "Egypt", "Vietnam",
        "DR Congo", "Turkey", "Iran", "Germany", "Thailand"
    ]
    return countries[:n]