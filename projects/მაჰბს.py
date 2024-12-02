def join2 (arr, filler):
    res = ""
    for i in arr: 
        res += i
        res += filler
    return res[:-2]

print(join2(["Banana", "Orange", "Apple", "Mango"], "-"))