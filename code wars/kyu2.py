conversation=[
"John:The man behind me is Peter.",
"Peter:There is 1 people in front of me.",
"Tom:There are 2 people behind me.",
"Peter:The man behind me is Tom."
]


def name (talk):
    ls = [x.split(":") for x in talk]
    names = []
    [names.append(i[0]) for i in ls]
    return names

def claimed_places(talk):
    temp =[]
    places = []
    for i in talk:
        ls = i.split(" ")
        for x in ls:
            if x[:-2] == "1" or x[:-2] == "2":
                places.append(x)
                ls = []
            if x[:-1] in name(talk):
                temp.append(x[:-1])
            if x == "behind" or x == "front":
                temp.append(x)
            if len(temp) ==2:
                places.append("_".join(temp))
                temp = [] 

    return places

def lier (talk):
    bad_man = None
    for i in claimed_places(talk):
        if "_" in i:
            ls = i.split("_")[1]
    if name(talk).index(ls) != claimed_places(talk)[name(talk).index(ls)]:
        bad_man = ls
            
            
    return bad_man      
print(lier(conversation))

print(name(conversation))
print(claimed_places(conversation))