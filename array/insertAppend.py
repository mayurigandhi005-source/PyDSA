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
    
       