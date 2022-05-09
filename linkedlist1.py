class Node:
    def __init__(self,data=None):
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

    def enter_sorted(self,data):
        node=Node(data)
        if self.h==None or self.h.data>node.data:
            node.next=self.h
            self.h=node
            return
        temp=self.h
        while temp.next!=None and temp.next.data<node.data:
            temp=temp.next
        node.next=temp.next
        temp.next=node
    def merge_sort(self,first,second):
        if first==None or second==None:
            return
        while first!=None and second!=None:
            self.enter_sorted(first.data)
            first=first.next
            self.enter_sorted(second.data)
            second=second.next
        while first!=None:
            self.enter_sorted(first.data)
            first=first.next
        while second!=None:
            self.enter_sorted(second.data)
            second=second.next


    def reverse(self):
        newhead = None
        temp = self.h
        while temp != None:
            next = temp.next
            temp.next = newhead
            newhead = temp
            temp = next
            self.h = newhead


    def print_list(self):
        temp=self.h
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()


l1=linked_list()
l2=linked_list()
l3=linked_list()
list=[1,4,6,7]
list1=[2,3,5,8,9,10,11,12]
for i in list:
    l1.enter_sorted(i)
for i in list1:
    l2.enter_sorted(i)

l1.print_list()
l2.print_list()
#l1.reverse()
l3.merge_sort(l1.h,l2.h)
l3.print_list()