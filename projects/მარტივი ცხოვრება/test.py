numbers = [
    15, 27, 31, 29, 34, 36, 37, 40, 41, 42, 
    46, 42, 45, 47, 47, 47, 47, 47, 48, 52, 
    55, 55, 55, 57, 57
]

numbers_no_duplicates = list(dict.fromkeys(numbers))

print(numbers_no_duplicates)