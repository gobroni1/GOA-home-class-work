list1 = []
for i in range (10):
    list1.append(i)
print(len(list1))

num1 = int(input("num1 pls "))
num2 = int(input("num2 pls "))

for i in range (num1, num2):
    list1.append(i)
print(list1)
print(len(list1))