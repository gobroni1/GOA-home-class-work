
def solution(n, m):
    result = []
    for i in range (n,m):
        
        for j in range (n,m+2,2):
            if i == j**2:
                result.append(i)
    return sorted(result)
                
print(solution(2,20))
    
    
#1
#2
#3
#4
#5
#6
#7
#8
