import array as arr
val = arr.array('i',[1,2,3,4,5,6,7,8,9])   

#slicing

# print('\n')
# val=val[2:5]
# for i in range(0,len(val)):
#     print(val[i], end=" ")         #O/P:- 3 4 5 

#        #OR

# print('\n')
# val=val[2:-3]
# for i in range(0,len(val)):
#     print(val[i], end=" ")  # o/p: 3 4 5 6  (removes last 3 elements)


         #OR    
# reverse
print('\n')
val=val[::-1]
for i in range(0,len(val)):
    print(val[i], end=" ")         # o/p 9 8 7 6 5 4 3 2 1 