#insert and append
import array as arr
val = arr.array('i',[1,2,3,4,5,6,7,8,9])   

#insert
val.insert(1,50)
for i in range(0,len(val)):
    print(val[i], end=" ")       #1 50 2 3 4 5 6 7 8 9 


#Append
print('\n')    
val.append(100)
for i in range(0,len(val)):
    print(val[i], end=" ")    #o/p:- 1 50 2 3 4 5 6 7 8 9 100 

#overwriting (updating)
print("\n")
val[2]=200 
for i in range(0,len(val)):
    print(val[i], end=" ")      #O/P:- 1 50 200 3 4 5 6 7 8 9 100 

#pop
print('\n')
val.pop(3)    
for i in range(0,len(val)):
    print(val[i], end=" ")    #o/p :- 1 50 200 4 5 6 7 8 9 100  (removing an element)

                   #OR
print('\n')
val.pop()    
for i in range(0,len(val)):
    print(val[i], end=" ")           #o/p:- 1 50 200 4 5 6 7 8 9   (removes last element)      


#Remove
print('\n')
val.remove(4)
for i in range(0,len(val)):
    print(val[i], end=" ")          #O/P:-1 50 200 5 6 7 8 9 



    