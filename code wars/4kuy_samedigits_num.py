def next_bigger(n):
    # Convert the number to a list of its digits
    digits = list(str(n))
    
    # Find the pivot point (rightmost digit that is smaller than the digit next to it)
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            break
    else:
        return -1  # If no such pivot is found, return -1 (no bigger number possible)

    # Find the smallest digit on the right of the pivot that is larger than the pivot digit
    for j in range(len(digits) - 1, i, -1):
        if digits[j] > digits[i]:
            break

    # Swap the pivot digit with this smallest larger digit
    digits[i], digits[j] = digits[j], digits[i]

    # Sort the digits to the right of the pivot in ascending order
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    # Convert the list of digits back to a number
    return int(''.join(digits))
print(next_bigger(123))