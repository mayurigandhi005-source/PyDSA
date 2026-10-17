from array import *
arr=array('i',[])
n = int(input("Enter element : "))
for i in range(0,n):
    arr.append(int(input("enter next input: ")))


for x in arr:           # enhanced for loop (takes each element from val, one by one)
    print(x,end=" ")

    #O/P:
# Enter element : 4
# enter next input: 1
# enter next input: 2
# enter next input: 3
# enter next input: 4
# 1 2 3 4 