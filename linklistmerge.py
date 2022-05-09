class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linked_list:
    def __init__(self):
        self.h=None
    def insert_in_begining(self,data):
        node=Node(data,self.h)
        self.h=node
    def insert(self,data):
        node=Node(data,None)
        if self.h is None or self.h.data > node.data:
            node.next=self.h
            self.h=node
            return
        temp=self.h
        while temp.next!=None and temp.next.data<node.data:
            temp=temp.next
        node.next=temp.next
        temp.next=node
    def printlist(self):
        current=self.h
        while current!=None:
            print(current.data, end=",")
            current=current.next
        print()
    def insert_list(self,data_list):
        self.h=None
        for data in data_list:
            self.insert(data)
    def merge(self,first,second):
        if first==None or second==None:
            return None
        while first!=None and second!=None:
            self.insert(first.data)
            first=first.next
            self.insert(second.data)
            second =second.next
        while first!=None:
            self.insert(first.data)
            first=first.next
        while second!=None:
            self.insert(second.data)
            second=second.next
    def size(self):
        cnt=0
        list=self.h
        while(list!=None):
            cnt+=1
            list=list.next
        return cnt
l1=linked_list()
l1.insert_list([2,0,5,4])
l1.printlist()
l2=linked_list()
l2.insert_list([1,3,8,9,7])
l2.printlist()
l3=linked_list()
#l3.insert_in_begining(3)
#l3.insert_in_begining(4)
l3.merge(l1.h,l2.h)
l3.printlist()
l1.size()
