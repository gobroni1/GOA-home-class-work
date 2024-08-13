def move_zeros(lst):
    s_t = []
    # Create a new list for non-zero elements
    new_lst = []
    
    for i in lst:
        if i == 0:
            s_t.append(i)
        else:
            new_lst.append(i)
    
    # Extend the original list with zeros
    new_lst.extend(s_t)
    return new_lst

# Test the function
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
