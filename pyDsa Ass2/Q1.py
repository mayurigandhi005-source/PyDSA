# Q. 1 Create a Stack with following operations
# 1. Push
# 2. Pop
# 3. Display
# 4. Reverse String using Stack
# 5. Reverse Stack using another

stack = []

def push(value):
    stack.append(value)
    print("Pushed:", value)

def pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
        value = stack.pop()
        print("Popped:", value)        

def display():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("Stack contains:", stack)   

def reverse_str(string):
    
    char_stack = []
    
    
    for ch in string:
        char_stack.append(ch)

    
    reverse = ""
    while len(char_stack) > 0:
        reverse = reverse + char_stack.pop()
        
    print("Reverse string:", reverse)        


push(10)
push(20)
push(30)

print("Current Stack:", stack)    

pop()
print("After Pop Stack:", stack)

display()


reverse_str("hello")