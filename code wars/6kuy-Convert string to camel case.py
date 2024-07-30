def narcissistic(n):
    n2 = str(n)
    ls = []
    total = 0
    while total < len(n2):
        ls.append(int(n2[total]) ** len(n2))
        total += 1
    if sum(ls) == n:
        return True
    else:
        return False

print(narcissistic(153))