class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert_value(root,val):
    if root==None:
        root=val
    if val<root.data:
        if root.left==None:
            root.left=Node(val)
        else:
            insert_value(root.left,val)
    if val>root.data:
        if root.right==None:
            root.right=Node(val)
        else:
            insert_value(root.right,val)
def delete(root,val) :
    if root==None:
        return 0
    if val<=root.data:
        if root.left.data==val:
            root.left=root.left.left
            root=root.right
        else:
            delete(root.left,val)
    if val>=root.data:
        if root.right.data==val:
            root.right=root.right.right
        else:
            delete(root.right,val)
def inorder(root):
    if root==None:
        return 0
    print(root.data,end=" ")
    inorder(root.left)
    inorder(root.right)
root=Node(5)
root.left=Node(3)
root.right=Node(12)
root.left.left=Node(1)
root.left.right=Node(4)
root.right.left=Node(8)
root.right.right=Node(15)

inorder(root)
#insert_value(root,6)
print()
delete(root,3)
inorder(root)