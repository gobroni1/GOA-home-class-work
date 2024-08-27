def hamming(a,b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff +=1 
    return diff