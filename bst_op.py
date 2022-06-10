class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,val):
    if root==None:
        root=Node(val)

    if val < root.data:
        root.left=insert(root.left,val)
    if val > root.data:
        root.right=insert(root.right, val)
    return root
def search_element(root,val):
    if root==None:
        return
    if root.data==val:
        return True
    if val<root.data and root.left!=None:
        return search_element(root.left,val)
    if val>root.data and root.right!=None:
        return search_element(root.right,val)

def delete_element(root,val):
    if root==None:
        return 0
    if val<=root.data:
        if root.left.data==val:
            root.left=root.left.left
            root=root.right
        else:
            delete_element(root.left,val)
    if val>=root.data:
        if root.right.data==val:
            root.right=root.right.right
            root=root.right
        else:
            delete_element(root.right,val)



def preorder(root):
    if root == None:
        return
    print(root.data,end=" ")

    preorder(root.left)

    preorder(root.right)
root = None
root=insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

insert(root,90)
preorder(root)
insert(root,6)
#insert(root,9)
print()
#preorder(root)
print(search_element(root,20))
delete_element(root,60)
preorder(root)

