my_dict=dict()
i=1
my_dict['a']=i
my_dict['a']=i+1
my_dict['b']=1


print(my_dict)
def anagram(str,k):
    s,e=0,0
    j=0
    while e<len(str):
        sub_str=str[s:e+1]
        if e-s+1<k:
            e+=1
        elif e-s+1==k:
            for i in sub_str:
                if i in my_dict.keys():
                    d=my_dict.get(i)
                    j+=d
                    if j==5:
                        print(sub_str,end=" ")
            s+=1
            e+=1
            j=0

str='abaabbaabbaab'
anagram(str,3)