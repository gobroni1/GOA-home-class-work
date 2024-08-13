def next_smaller(n):
    digits = list(str(n))
    length = len(digits)

    # Step 2: Find the first digit that is larger than the digit to its right
    for i in range(length - 2, -1, -1):
        if digits[i] > digits[i + 1]:
            break
    else:
        return -1  # No such digit is found, return -1

    # Step 3: Find the largest digit to the right that is smaller than digits[i]
    for j in range(length - 1, i, -1):
        if digits[j] < digits[i]:
            # Step 4: Swap these two digits
            digits[i], digits[j] = digits[j], digits[i]
            break

    # Step 5: Sort the digits to the right of i in descending order
    digits = digits[:i + 1] + sorted(digits[i + 1:], reverse=True)

    # Step 6: Ensure the result does not have a leading zero
    if digits[0] == '0':
        return -1

    # Step 7: Return the result as an integer
    result = int(''.join(digits))
    return result

