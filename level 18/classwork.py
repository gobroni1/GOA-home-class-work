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


list_1 = []
starting_n = int(input("starting num pls:"))
ending_n = int(input("ending num pls:"))

for i in range (starting_n, ending_n):
    list_1.append(i)
print(list_1)
print(max(list_1))
print(min(list_1))
print(sum(list_1))