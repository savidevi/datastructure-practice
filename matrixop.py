li=[[1,2,3,4,17,21],
    [7,8,9,5,18,22],
    [13,14,15,6,19,23],
    [10,11,12,16,20,24]]
sr=0
sc=0
er=len(li)#column length
ec=len(li[0])#row length
print(ec)

while sr<=er-1 and sc<=ec-1:
    for i in range(sc,ec):
        print(li[sr][i],end=",")
    for i in range(sr+1,er):
        print(li[i][ec-1],end=",")
    if sr!=er:
        for i in reversed(range(sc,ec-1)):
            print(li[er-1][i],end=",")
    if sc!=ec:
        for i in reversed(range(sr+1,er-1)):
            print(li[i][sc],end=",")
    sr+=1
    sc+=1
    er-=1
    ec-=1