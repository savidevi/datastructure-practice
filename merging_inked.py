class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list():
    def __init__(self):
        self.h=None
    def insert_data(self,val):
        node=Node(val)
        if self.h==None:
            self.h=node
            return
        temp=self.h
        while temp.next!=None:
            temp=temp.next
        temp.next=node
    def merge(self,first,second):
        if first==None and second==None:
            return
        while first!=None and second!=None:
            if first.data<second.data:
                self.insert_data(first.data)
                first=first.next
            else:
                self.insert_data(second.data)
                second = second.next
        while first!=None:
            self.insert_data(first.data)
            first=first.next
        while second!=None:
            self.insert_data(second.data)
            second=second.next
    def print_list(self):
        if self.h==None:
            return
        temp=self.h
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
l1=linked_list()
l2=linked_list()
l3=linked_list()
list=[2,4,6,8]
list2=[1,3,5,7,9,10,12]
for i in list:
    l1.insert_data(i)
for i in list2:
    l2.insert_data(i)
l1.print_list()
print()
l2.print_list()
print()
l3.merge(l1.h,l2.h)
l3.print_list()