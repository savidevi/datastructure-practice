def find_unique(list):
    res=0
    for i in range(len(list)):
        res =res^list[i]
    return res
list=[5,5,5,4,3,2,3,2,6,6]
print(find_unique)