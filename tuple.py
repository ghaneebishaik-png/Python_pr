"""Tuple methods
1.Concatination and repetition
2.Index and sclicing
3.

"""
data1=("1","2","3")
data2=("a","b","c")
print(data1+data2)
print(data1*2)

print(data1.index("2"))
print(data1[1::])

#print(data1.insert(1,"4"))

t=(10,)

print(t)
t1=1,2,3
a,b,c=t1
print(a,b,c)
print(len(data1))