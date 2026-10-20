class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class SLL:
    def __init__(self,head=None):
        self.head=head   # head assign in object (self is an object)

    def insertAtEnd(self,value):
        temp=Node(value)
        if(self.head != None):
            a=self.head
            while(a.next != None):
                a = a.next
            a.next = temp
        else:
            self.head = temp 

    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head 
        self.head = temp   


    def insertInMid(self,value,x):
        temp=Node(value)
        a = self.head

        while(a.next != None):
            if(a.data == x):
                temp.next = a.next
                a.next = temp
            a = a.next    




    def print(self):
        a = self.head
        while(a.next != None):
            print(a.data) 
            a = a.next 
        print(a.data)    

list = SLL()
            
list.insertAtEnd(10)
list.insertAtEnd(20)
list.insertAtEnd(30)
list.insertAtBeg(5)
list.insertInMid(19,20)
list.print()





                

                
