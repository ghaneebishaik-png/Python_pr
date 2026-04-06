"""
list1=[]
for i in range(10):
    list1.append(i)
print(list1)

"""

dict1={"a":10,"b":20,"c":88,"d":15}
#out={"b":20,"c":88}
d={}

for i,j in dict1.items():
    if j>15:
        d[i]=j
print(d)

l1=[1,2,3]
l2=[3,4,5]

print(list(zip(l1,l2)))