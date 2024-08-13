import math

def isPP(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        j = round(math.log(n, i))
        if i ** j == n:
            return [i, j]
    return None
print(isPP(9))