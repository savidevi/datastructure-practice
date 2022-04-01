class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.h=None
    def number(self,number):
        n=number
        while n>0:
            a = n % 10
            b = node(a)
            if self.h==None:
                self.h=b
            else:
                current=self.h
                while current.next!=None:
                    current=current.next
                current.next=b
            n = int(n//10)
    def add(self,l1,l2):
        ad=0
        carry=0
        while l1!=None and l2!=None:
            ad=l1.data+l2.data+carry

            if ad >= 10:
                carry=1
                ad=ad%10
                sum = node(ad)

                if self.h == None:
                    self.h = sum
                else:
                    current = self.h
                    while current.next != None:
                        current = current.next
                    current.next = sum
            else:
                carry=0
                sum=node(ad)
                if self.h == None:
                    self.h = sum
                else:
                    current = self.h
                    while current.next != None:
                        current = current.next
                    current.next = sum
            l1=l1.next
            l2=l2.next
        while l1!=None:
            current=current.next
            if carry==1:
                l1.data+=1
            current.next=l1
            l1=l1.next
        while l2!=None:
            current=current.next
            if carry==1:
                l2.data+=1
            current.next=l2
            l2=l2.next

    def insert(self,data):
        Node=node(data)
        if self.h is None:
            self.h=Node
            return
        temp=self.h
        while temp.next!=None:
            temp=temp.next
        temp.next=Node

    def printlist(self):
        print_list = self.h
        while print_list != None:
            print(print_list.data, end=" ")
            print_list = print_list.next
        print()
    def reverse(self):
        newhead = None
        temp = self.h
        while temp != None:
            next = temp.next
            temp.next = newhead
            newhead = temp
            temp = next
            self.h = newhead
li = linkedlist()
li.insert(1)
li.insert(2)
li.printlist()
first=linkedlist()
second=linkedlist()
sum=linkedlist()
first.number(234)
#first.reverse()
#first.printlist()
second.number(1968)
first.printlist()
second.printlist()
#second.printlist()
sum.add(first.h,second.h)
sum.printlist()
#sum.reverse()
#sum.printlist()