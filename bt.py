class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next=None

root = Node(5)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(10)
root.right.left = Node(8)
root.right.right = Node(20)
root.right.left.right = Node(9)

'''def preorder(root):
    if root==None:
        return
    print(root.data,end=",")
    preorder(root.left)
    preorder(root.right)
def find_leafnode(root):
    if root==None:
        return
    if root.left==None or root.right==None:
        print(root.data, end=" ")
    find_leafnode(root.left)
    find_leafnode(root.right)

'''


def search(root, val):
    if root == None:
        return False
    if root.data == val:
        print(val)
        return True
    return search(root.left, val) or search(root.right, val)

def root_to_leaf_path(root,a,index):
    if root==None:
        return
    a.insert(index,root.data)
    if (root.left == None and root.right == None ):
        print()
        for i in a[:index+1]:
            print(i,end=" ")
        return
    root_to_leaf_path(root.left, a, index + 1)
    root_to_leaf_path(root.right, a, index + 1)


def ancestor(root, val):
    if root == None:
        return False
    if root.data == val:
        return True
    if ancestor(root.left, val) or  ancestor(root.right, val):
        print(root.data,end=" ")
        return True
    return False

def level_traverse(root):
    if root!=None:
        queue=[root]

    while queue:
        node=queue.pop(0)
        print(node.data,end=" ")
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)


def each_level_traverse(root):
    if root != None:
        queue = [None]
        queue.append(root)
    while queue:
        node = queue.pop(0)
        if node!=None:
            print(node.data, end=" ")

            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)
        else:

            print()
            if queue:
                queue.append(None)

def front_view(root):
    if root != None:
        queue=[None]
        queue.append(root)

    while queue:
        node = queue.pop(0)
        if node != None:

            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)

        else:
            print()
            if queue:
                queue.append(None)
        if (node == None)  and len(queue)!=0:
                print(queue[0].data, end=" ")

def back_view(root):
    if root != None:
        queue = [None]
        queue.append(root)
    while queue:
        node = queue.pop(0)
        if node != None:

            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)

        else:
            print()
            if queue:
                queue.append(None)
        if (node != None) and queue[0] == None:
            print(node.data, end=" ")

'''preorder(root)
print("leaf node:")
find_leafnode(root)
print("leaf path:")
a=[]
root_to_leaf_path(root,a,0)
print()'''
#print(search(root, 12))
#print()
#ancestor(root,9)
#print()
#level_traverse(root)
#print()

each_level_traverse(root)
print()
back_view(root)
front_view(root)