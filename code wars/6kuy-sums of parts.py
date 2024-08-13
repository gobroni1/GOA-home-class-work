def parts_sums(ls):
    ls2=[]
    f=sum(ls)
    for i in range (len(ls)):
        for x in range(i):
            print(i)
            ls2.append(sum(ls))
    return ls2
print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))

#faster code from internet 
def parts_sums(ls):
    sums = [sum(ls)]
    for i in ls:
        sums.append(sums[-1]-i)
    return sums