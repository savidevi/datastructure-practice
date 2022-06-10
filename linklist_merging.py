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
        temp = self.h
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def insert(self, data):
        node = Node(data)
        if self.h == None:
            self.h = node
            return
        temp = self.h
        while temp.next != None:
            temp = temp.next
        temp.next = node
    def merging(self,first,second, m,n):
        if first==None and second==None:
            return None

        while first != None and second != None:
            if first.data<second.data:
                self.insert(first.data)
                first=first.next
            else:
                self.insert(second.data)
                second=second.next
        while first!=None:
            self.insert(first.data)
            first = first.next
        while second!=None:
            self.insert(second.data)
            second = second.next


l1=linked_list()
l2=linked_list()
l2.h=Node(1)
l1.h=Node(2)
a1=Node(3)
a2=Node(4)
a3=Node(5)
a4=Node(6)
a5=Node(7)
a6=Node(8)
a7=Node(9)

l1.h.next=a1
a1.next=a3
a3.next=a5

l2.h.next=a2
a2.next=a4
a4.next=a6
a6.next=a7
l1.print_list()
l2.print_list()
m=l1.countno()
n=l2.countno()

l3=linked_list()
l3.merging(l1.h,l2.h,m,n)
l3.print_list()