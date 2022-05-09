class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.h=None

    def insert(self,data):
        node=Node(data)
        if self.h==None:
            self.h=node
            return
        temp=self.h
        while temp.next !=None:
            temp=temp.next
        temp.next=node

    def print_list(self):
        if self.h==None:
            return
        temp=self.h
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next

    def reverse(self):
        newhead = None
        temp = self.h
        while temp != None:
            next = temp.next
            temp.next = newhead
            newhead = temp
            temp = next
            self.h = newhead

    def printconlist(self):
        print()
        temp = self.h
        while temp != None:
            m = 1
            n = 1
            while temp != None and m <= 2:
                print(temp.data, end=" ")
                temp = temp.next
                m += 1
            newhead = None
            while temp != None and n <= 3:
                next = temp.next
                temp.next = newhead
                newhead = temp
                temp = next
                self.h = newhead
                n += 1
            self.print_list()

l1=Linked_list()
list=[1,2,3,4,5,6,7,8,9]
for i in list:
    l1.insert(i)
l1.print_list()
l1.printconlist()


