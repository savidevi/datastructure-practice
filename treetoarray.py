class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(5)
root.left=Node(3)
root.right=Node(10)
root.left.left=Node(1)
root.left.right=Node(4)
root.right.left=Node(8)
root.right.right=Node(20)
root.right.left.right=Node(9)
def tree_to_array(a,root,r):
    if root != None:
        queue = [root]
    while queue:
        node = queue.pop(0)
        a.insert(r,node.data)
        print(node.data, end=" ")
        if node.left != None:
            a.insert((2*r+1),node.left.data)
            queue.append(node.left)
        if node.right:
            a.insert((2 * r + 2), node.right.data)
            queue.append(node.right)
a=[]

tree_to_array(a,root,0)
print(a)
