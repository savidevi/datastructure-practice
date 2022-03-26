'''def is_anagram(s1,s2):
    return set(s1)&set(s2)

print(is_anagram("lies","sevil"))'''

'''def is_palindrom(phrase):
    return phrase[:-1] == phrase

print(is_palindrom("anna is anna"))'''


# reverse using recurision

'''def reverse(phrase):
    if len(phrase) <= 1:
        return phrase
    else:
        return reverse(phrase[1:])+phrase[0]


print(reverse("hello"))'''

ph1="bcabc"

ph=set(ph1)
print(ph)
a="".join(sorted(ph))
print(a)
'''for i in range(p):
    for st in ph1:
        if i==0:
            ph=st
            print(ph)'''
