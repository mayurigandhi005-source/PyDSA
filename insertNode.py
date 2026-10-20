class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. append Linked List (Append)
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    #insert        

    def insert(self,new_node,pos):
        if pos < 1:
            new_node.next=self.head
            self.head=new_node
        else:
            p=1
            temp=self.head
            while p != pos - 1:
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node
        
    def print(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
                  
list1 = LinkedList()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print(" list:")
list1.print()
list1.insert(Node(25),3)

print("\ninsert")
list1.print()
