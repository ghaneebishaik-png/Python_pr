#lambda fuction
#fuc_out = lambda arguments:expression

add = lambda x,y:x*y
out=add(10,3)
print(out)

l1=['a','b','c','d']
func1=lambda x:x+'%'
for i in l1:
    print(func1(i))

even = lambda x : x%2==0
print(even(12))

#filter(function,sequence)
print(tuple(filter(lambda x:x%2==0,[1,2,30,4])))
import re
l2=['abc','abc123','1234']
print(list(filter(lambda x:re.search("\d",x),l2)))

l3=[10,20,30,40,50]#out should be[40,50]
print(list(filter(lambda x : x>30,l3)))

#List contains space and special character

l3 = ['12 34','str1','1234','12&34']#out should be ['12 34','12&34']
print(list(filter(lambda x:re.search("\s|\W",x),l3)))

#map 
#map(function,sequence)
print(list(map(lambda x:x**2,[1,2,3,4])))


l4=['sda','sdb','sdc']#out should be['/dev/sda','/dev/sdb','/dev/sdc']

print(list(map(lambda x:'/dev/'+x,l4)))

#ex2
l6=['a','b','c','d']
print(list(map(lambda x:x+'*',l6)))


#reduce
from functools import reduce
l5=[1,2,3,4]
print(reduce(lambda x,y:x+y,l5))#1+2=3,3+3=6,6+4=10


results = ["PASS", "FAIL", "PASS", "FAIL"]#How do you count failures using functional programming?
count=0
print(len(reduce(map(lambda x:x=='FAIL',results))))