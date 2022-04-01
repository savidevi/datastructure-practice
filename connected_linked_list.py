class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.h=None
    def insert(self,data):
        node=Node(data)

        if self.h==None:
            self.h=node
            return
        temp=self.h
        while temp.next!=None:
            temp=temp.next
        temp.next=node
    def printlist(self):
        temp=self.h
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def find_common(self,first,second):
        cntfirst=l1.count()
        cntsecond=l2.count()

        if cntfirst > cntsecond:
            first=first.next

        else:
            second=second.next

        if first==None or second==None:
            print("no intersection")
        while first.next!=None and second.next!=None:

            if first.next.data==second.next.data:
                print("intersection point: ",first.next.data)
                break
            first=first.next
            second=second.next

    def count(self):
        cnt=0
        temp=self.h
        while temp!= None:
            cnt+=1
            temp= temp.next
        return cnt
l1=linked_list()
l2=linked_list()
l3=linked_list()

common=Node(4)
common1=Node(5)
common2=Node(6)
common3=Node(7)


l1.insert(2)
l1.insert(1)
l1.insert(3)
l1.insert(common.data)
l1.insert(common1.data)
l1.insert(common2.data)
l1.insert(common3.data)
l2.insert(7)
l2.insert(8)
l2.insert(common.data)
l2.insert(common1.data)
l2.insert(common2.data)
l2.insert(common3.data)

l1.printlist()
l2.printlist()


l3.find_common(l1.h,l2.h)