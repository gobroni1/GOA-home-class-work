def to_weird_case(words):
    list1 = words.lower().split(" ")
    list2 = []
    for word in list1:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()  
            else:
                new_word += word[i]  
        list2.append(new_word)
    return " ".join(list2)
print(to_weird_case("hello my name is who"))
