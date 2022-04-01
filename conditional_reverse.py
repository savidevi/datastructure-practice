class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.h=None
    def insert(self,data):
        node=Node(data)
        if self.h==None or self.h.data>data :
            node.next = self.h
            self.h=node
            return
        temp=self.h
        while temp.next!=None and temp.next.data<data:
            temp=temp.next
        node.next = temp.next
        temp.next=node
    def printlist(self):
        temp=self.h
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next

    def reverse(self):
        newhead=None

        if self.h==None or self.h.next==None:
            temp=self.h
        temp=self.h
        while temp!=None:
            next = temp.next
            temp.next = newhead
            newhead = temp
            temp = next
            self.h = newhead
    def enter_list(self,list):
        for data in list:
            self.insert(data)
    def printconlist(self):
        print()
        temp=self.h
        while temp!=None:
            m=1
            n=1
            while temp!=None and m<=2:
                print(temp.data,end=" ")
                temp=temp.next
                m+=1
            newhead=None
            while temp!=None and n<=3:
                next=temp.next
                temp.next=newhead
                newhead=temp
                temp=next
                self.h=newhead
                n+=1
            self.printlist()



l1=linked_list()
l1.enter_list([1,3,5,7,9,2,4,6,8])
l1.printlist()
#l1.reverse()
l1.printconlist()