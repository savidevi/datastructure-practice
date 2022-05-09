class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.h=None
    def find_mid(self):
        h1 = self.h
        h2 = self.h
        while h1 != None and h2 != None:
            h1 = h1.next
            h2 = h2.next.next
        return h1
    def reverse(self,m):
        newhead=None
        temp=self.h
        while temp!=m:
            next=temp.next
            temp.next=newhead
            newhead=temp
            temp=next
            self.h=newhead
        return self.h

    def palindrom(self):
        m=self.find_mid()
        r=self.reverse(m)
        print(m.data,r.data)
        while  m!=None:
            print(r.data)
            print(m.data)
            if r.data!=m.data :
                return False

            r = r.next
            m = m.next
        return True


l1=linked_list()
l1.h = Node("a")
e2 = Node("b")
e3 = Node("c")
e4 = Node("c")
e5 = Node("b")
e6 = Node("a")
l1.h.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
print(l1.palindrom())
