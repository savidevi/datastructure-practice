class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SLinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      printval = self.head
      while printval != None:
         print (printval.data,end="")
         printval = printval.next
      print()
   def reverse(self):
        newhead = None
        temp= Node()
        temp=self.head
        while  temp!=None  :
            next=temp.next
            temp.next= newhead
            newhead = temp
            temp=next
            self.head=newhead



   def listcom(self):
       printval1 = self.head
       while printval1 != None:
           print(printval1.data, end="")
           printval1 = printval1.next

           if(printval1.data==printval1.next.data):
               print(printval1.next.data,end="")

               break


       print()

list = SLinkedList()
#temp=Node()
list.head = Node("t")
e2 = Node("b")
e3 = Node("c")
e4 = Node("c")
e5 = Node("b")
e6 = Node("a")
list.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6

list.listprint()
list.reverse()
list.listprint()
list.listcom()
'''


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None :
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev

        


    # Function to insert a new node at the beginning
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        print(new_node.data)


    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print( temp.data,end="  ")
            temp = temp.next
    def palindrom(self):
        if new_node.data==current.next.data:
            print(new_node.data)


# Driver code
llist = LinkedList()
llist.add('t')
llist.add('r')
llist.add('c')
llist.add('c')
llist.add('b')
llist.add('a')

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
#llist.palindrom()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)'''