import array as arr
val = arr.array('i',[1,2,3,4,5,6,7,8,9])
for i in range(0,6):
    print(val[i],end = " ")    # O/P :- 1 2 3 4 5 6

    #OR

print('\n')
for x in val:           # enhanced for loop (takes each element from val, one by one)
    print(x,end=" ")    # o/p :- 1 2 3 4 5 6 7 8 9


    #OR
print('\n')
for i in range(0,len(val)):
    print(val[i],end=" ")    #O/P:- 1 2 3 4 5 6 7 8 9

    #type
print('\n')
print(val.typecode)    # O/P:- i


# reverse
val.reverse()
for i in range(0,len(val)):
    print(val[i], end=" ")   #o/p:- 9,8,7,6,5,4,3,2,1


