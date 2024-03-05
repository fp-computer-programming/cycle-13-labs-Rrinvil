def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string

def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

def find_maximum(numbers):
    max_num = max(numbers)
    return max_num

def remove_duplicates(lst):
    unique_lst = list(set(lst))
    return unique_lst

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def capitalize_words(words):
    capitalized_words = [word.capitalize() for word in words]
    return capitalized_words

def find_index(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def replace_string_occurrences(string, old, new):
    replaced_string = string.replace(old, new)
    return replaced_string
