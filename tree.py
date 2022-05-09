class binary_tree:
    def __init__(self, key):
        self.key= key
        self.left = None
        self.right = None

    def add_value(self, val):

        if self.key == None:
            self.key =val
            return
        if val < self.key:
            if self.left == None:
                self.left = binary_tree(val)
            else:
                self.left.add_value(val)
        else:
            if self.right == None:
                self.right = binary_tree(val)
            else:
                self.right.add_value(val)

    def preorder(self):
        if self.key == None:
            return
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.key == None:
            return
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()


    def postorder(self):
        if self.key == None:
            return
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()
        print(self.key, end=" ")

    def printLeafNodes(self):
        if self.key == None:
            return
        if self.left == None and self.right == None:
            print(self.key,end=" ")
            return
        if self.left!=None:
            self.left.printLeafNodes()
        if self.right!=None:
            self.right.printLeafNodes()
    def heightoftree(self):
        global x
        global y
        if self.key == None:
            return None
        if self.left!=None :
            x += 1
            self.left.heightoftree()

        if self.right!=None:
            y+=1
            self.right.heightoftree()
        return max(x,y)
    def get_level(self,val):
        global x,y
        if self.key==val:
            print(x)
        if val < self.key:
            if self.left!=None:
                x += 1
                self.left.get_level(val)
        else:
            if self.right!=None:
                x+= 1
                self.right.get_level(val)

        if self.key == None:
             return -1
    def ancestors(self,val):
        if self.key==val:
            print(self.key)
            return
        if val<self.key:
            print(self.key,end=" ")

            if self.left!=None:
                self.left.ancestors(val)
        else:
            print(self.key,end=" ")
            if self.right!=None:
                self.right.ancestors(val)



b = binary_tree(None)
l1=[5,3,1,4,8,7,9,10,20]
for i in l1:
    b.add_value(i)
print("pre")
b.preorder()
print("in")
b.inorder()
print()
print("post")
b.postorder()
print()
print("leafnode")
b.printLeafNodes()
print()
global x
x=0
global y
y=0
height=b.heightoftree()
print("height:",height)
print("level")
b.get_level(4)
print()
print("ancestor")
b.ancestors(20)
