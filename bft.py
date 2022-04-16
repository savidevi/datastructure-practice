from audioop import reverse


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

def bfs(root):
    if root!=None:
        queue=[root]
    while queue:
        node = queue.pop(0)
        print(node.data,end=" ")
        if node.left!=None:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
def traverse(root):
    if root!=None:
        queue=[root]
    while queue:
        level=len(queue)

        for i in range(level):
            node = queue.pop(0)
            print(node.data,end=" ")
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
        print()

def reversee(root):
    if root != None:
        queue = [root]
    while queue:
        level = len(queue)
        l = []
        for i in range(level):
            node = queue.pop(0)
            l.append(node.data)
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
        print(l)
def last_element(root):
    if root!=None:
        queue=[root]
    while queue:
        level=len(queue)
        for i in range(level):
            node=queue.pop(0)
            last=node.data
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
        print(last)
def first_element(root):
    if root!=None:
        queue=[root]
    while queue:
        level = len(queue)
        l = []
        for i in range(level):
            node=queue.pop(0)
            l.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(l[0])
bfs(root)
print()
traverse(root)
print()
last_element(root)
first_element(root)