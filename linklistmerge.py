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
        if self.h is None:
            self.h=Node(data,None)
            return
        temp=self.h
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(data,None)
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
    def merge(self,l1,l2):
        while l1!=None and l2!=None:
            
            self.insert(l1.data)
            l1=l1.next
            self.insert(l2.data)
            l2 = l2.next

                #self.h=l2
                    #l2=l2.next

    def size(self):
        cnt=0
        list=self.h
        while(list!=None):
            cnt+=1
            list=list.next
        print(cnt)
l1=linked_list()
l1.insert_list([0,2,4,5])
l1.printlist()
l2=linked_list()
l2.insert_list([1,3,8,9])
l2.printlist()
l3=linked_list()
#l3.insert_in_begining(3)
#l3.insert_in_begining(4)
l3.merge(l1.h,l2.h)
l3.printlist()
l1.size()
