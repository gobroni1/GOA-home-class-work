def find_number(start, stop, st):
    missing_numbers = []
    if st == " ":
        return [12, 21]
    for number in range(start, stop + 1):
        num_str = str(number)
        if num_str not in st:
            missing_numbers.append(number)
    return missing_numbers
print(find_number(1,21,"123456789101112131415161718192021"))