def next_bigger (n):
    m = n 
    num = str(n)
    list1= list(num)
    while True:
        m += 1
        if sorted(list(str(m))) == sorted(list1):
            return m
    return -1
        
print(next_bigger(756))