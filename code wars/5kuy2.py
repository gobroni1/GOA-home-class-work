def digitwise_addition(N, K):
    MOD = 10**9 + 7
    
    # Convert the number N to a list of digit counts
    digit_count = [0] * 10
    for digit in str(N):
        digit_count[int(digit)] += 1
    
    # Iterate K times to perform the digitwise addition
    for _ in range(K):
        new_digit_count = [0] * 10
        for digit in range(10):
            if digit == 9:
                new_digit_count[0] += digit_count[digit]
                new_digit_count[1] += digit_count[digit]
            else:
                new_digit_count[digit + 1] += digit_count[digit]
        digit_count = new_digit_count
    
    # Calculate the total number of digits
    total_digits = sum(digit_count)
    
    return total_digits % MOD