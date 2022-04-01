def parentheses(s):
    b=')}]'
    c='({['
    list=[]
    for i in s[0:]:
        if i in c[0:]:
            list.append(i)
        elif i in b[0:]:
            cb=b.index(i)
            if list!=[] and c[cb]== list[len(list)-1]:
                list.pop()
            else:
                return False
    if list == []:
        return True
    else:
        return False
t=parentheses("{()}")
print(t)
