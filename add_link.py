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

    def print_list(self):
        temp = self.h
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def add(self,):