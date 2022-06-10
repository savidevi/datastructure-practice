class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.h=None
    def print_list(self):
        temp=self.h
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def countno(self):
        temp=self.h
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        return count
    def mergingpoint(self,first,second,m,n):

        if m>n:
            for i in range(m-n):
                first=first.next
        else:
            for i in range(n-m):
                second=second.next
        while first.data!=second.data:
            first=first.next
            second=second.next
        return first.data
l1=linked_list()
l2=linked_list()
l2.h=Node(3)
l1.h=Node(1)
a1=Node(2)
a3=Node(6)
a4=Node(7)
a5=Node(8)
a6=Node(9)
a7=Node(4)

l1.h.next=a1
a1.next=a6
a6.next=a3
a3.next=a4
a4.next=a5
l2.h.next=a7
a7.next=a3
a3.next=a4
a4.next=a5
l1.print_list()
l2.print_list()
m=l1.countno()
n=l2.countno()

l3=linked_list()
print(l3.mergingpoint(l1.h,l2.h,m,n))
