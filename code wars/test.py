text = "12 13.5 3.5 15 0 18 0 18 15 15 16.5 5 0 11 3 0 15 0.5 4 0 0 10 16 11 12"

ls = text.split(" ")
sum = 0
for i in ls:
    sum += float(i)
    
print(sum)