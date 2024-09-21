text = "111111222222222"
ls =[]
speed1 = 0
speed2 = 0

for i in range (len(text)):
    ls.append(text[i])
for i in ls:
    if i == "2":
        speed2 += 1
    elif i == "1":
        speed1+=1
print(speed1, speed2)
print((speed1*7.5) + (9*12.5))