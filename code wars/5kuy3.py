def first_non_repeating_letter(s):
    # Convert the string to lowercase for case-insensitive comparison
    lower_s = s.lower()
    
    # Dictionary to store character counts
    count = {}
    
    # Count occurrences of each character in a case-insensitive manner
    for char in lower_s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    # Find the first character in the original string that is not repeated
    for char in s:
        if count[char.lower()] == 1:
            return char
    
    # Return an empty string if no non-repeating character is found
    return ""