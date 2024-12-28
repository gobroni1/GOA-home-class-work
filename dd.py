data = [27, 27, 27, 29, 30, 31, 34, 36, 37, 40, 41, 42, 42, 46, 47, 47, 47, 47, 47, 48, 53, 55, 55, 55, 55, 55, 56, 56, 57, 57]

#

ls = [2,2,2,1,1,1,3,1,1,2,3,1,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2]

ls2 = []

d1 = 0
d2 = 0
d3 = 0

for i in range(len(ls)):
    if ls[i] == 2:
        d2+= 1
        ls2.append([data[i],ls[i]])
    elif ls[i] == 1:
        d1+= 1
        ls2.append([data[i],ls[i]])
    elif ls[i] == 3:
        d3+=1
        ls2.append([data[i],ls[i]])

print(d1,d2,d3)
# print(ls2)

# ls=[2,2,2,1,1,1,3,1,1,2,3,1,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2]
# for i in range(len(ls)):
#     print(f"group{data[i]} - speed{ls[i]}")
# #

s1 = 0
s2= 0
s3 = 0

s1g = [33, 32, 31, 30, 29, 37, 42, 43, 44, 45, 51, 52, 53, 54, 57, 36]
s2g = [27, 40, 39, 38, 46, 47, 48, 55, 56]
s3g = [34, 5, 6, 14, 15, 16, 41, 49, 50]



for i in data:
    if i in s1g:
        s1 += 1
        
    elif i in s2g:
        s2+= 1
        
    elif i in s3g:
        s3+= 1 
        
    else:
        print(i)
        
# print(s1,s2,s3,len(data))       