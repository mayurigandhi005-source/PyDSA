class Node:            
    def __init__(self,value):    # Runs when creating a new node
        self.left = None         # no left child at start
        self.right = None        # no right child at start
        self.data = value        # Stores the actual number in the node

def insert(root,value):          # Function to insert a value into the BST
    if (root == None):           # If the spot is empty
        return Node(value)       # Create a new node and return it
    
    if(root.data == value):      # If the value already exists
        return root              # Do not insert duplicates... return current node
    if(root.data > value):       # if new value is smaller than current node
        root.left = insert(root.left,value)     # insert in the left subtree and link it
    else:
        root.right = insert(root.right,value)   # insert in the right subtree and link it
    return root                             # return updated node

def inorder(root):                  # Left -> Root -> Right traversal
    if root:                        #if node is not None
        inorder(root.left)          # visit left subtree first
        print(root.data,end=" ")    
        inorder(root.right)         #visit right ST

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
    temp = root             # start from root using a temporary pointer
    while temp.left is not None:  #keep moving left while a temporary pointer

        temp = temp.left        # move to the left child
    return temp.data            #return value

def find_max(root):
    if root is None:
        return None
    temp = root
    while temp.right is not None:
        temp = temp.right
    return temp.data  

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)   # 1 (this node) + left count + right count     

root = insert(None,75)  # create node

root = insert(root,34)        
root = insert(root,45)        
root = insert(root,62)        
root = insert(root,22)        
root = insert(root,96)        
root = insert(root,82)        
root = insert(root,105)  
root = insert(root,98)  
root = insert(root,25)

print("\nInorder")
inorder(root)
print()

print("\npreorder")
preorder(root)
print()

print("\npostorder")
postorder(root)
print()

print("min",find_min(root))

print("max",find_max(root))

print("\nLeft nodes:", count(root.left))
print("\nRight nodes:", count(root.right))

