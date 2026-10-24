class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Lqueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

que=Lqueue()
que.enqueue(Node(23))                            
que.enqueue(Node(63))                            
que.enqueue(Node(78))                            
que.enqueue(Node(93))                            
que.enqueue(Node(24))  
que.print()                          
        