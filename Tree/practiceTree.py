class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def insert(root,value):
    if (root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root :
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.data

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.data  

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)      

root = insert(None,75)

root = insert(root,34)        
root = insert(root,45)        
root = insert(root,62)        
root = insert(root,22)        
root = insert(root,96)        
root = insert(root,82)        
root = insert(root,105)  
root = insert(root,98)  
root = insert(root,25)  

inorder(root)
print()
preorder(root)
print()
postorder(root)
print()

print("min",find_min(root))
print("max",find_max(root))

print("Left nodes:", count(root.left))
print("Right nodes:", count(root.right))

