def solution(array_a, array_b):
    a3=[]
    sum = 0
    for i in range (len(array_a)):
        a3.append(abs(array_a[i]-array_b[i]))
        sum += (a3[i] **2)
    return (sum / len(array_a))
print(solution([1,2,3],[4,5,6]))