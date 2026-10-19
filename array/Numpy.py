from numpy import*
val = array([1,2,3,4.5,'a'])
for x in val:
    print(x,end=" ")

    #o/p:- 1 2 3 4.5 a 


 #typecasting
print('/n')
from numpy import*
val = array([1,2,3],float)
for x in val:
    print(x,end=" ")  # O/p: 1.0 2.0 3.0 