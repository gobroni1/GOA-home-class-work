from itertools import permutations

def unique_permutations(s):
    # Generate all permutations of the string
    perms = permutations(s)
    
    # Convert permutations to a set to remove duplicates and then to a sorted list
    unique_perms = sorted(set(''.join(p) for p in perms))
    
    return unique_perms