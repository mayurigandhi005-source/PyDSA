# An e-commerce company maintains product IDs in a BST to enable efficient
# product searching.
# Tasks:
# 1. Create a BST using product IDs.
# Insert the following product IDs:
# 150, 100, 200, 75, 125, 175, 250, 60, 90, 110.
# 2. Display product IDs in ascending order.
# 3. Search for product ID 175 exists.
# 4. Delete product ID 100.
# 5. Display the BST using inorder, preorder, and postorder traversals.
# 6. Find the minimum and maximum product IDs.

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

def search(root,value):
    if root is None:
        return False
    if root.data == value:
        return True
    if root.data > value:
        return search (root.left,value)
    return search(root.right,value)


def delete_node(root, key):
    if root is None:
        return None
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        min_right = find_min(root.right)
        root.data = min_right
        root.right = delete_node(root.right, min_right)
    return root    

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



root = insert(None,150)  # create node

root = insert(root,100)        
root = insert(root,200)        
root = insert(root,75)        
root = insert(root,125)        
root = insert(root,175)        
root = insert(root,250)        
root = insert(root,60)  
root = insert(root,90)  
root = insert(root,110)

print("product IDs in ascending order")
inorder(root)
print()

if search(root,175):
    print("\n Product ID 175 exist")
else:
    print("\n not exist")    

root = delete_node(root,100)    
print("product id after deleting ")
inorder(root)
print()

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


