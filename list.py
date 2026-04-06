"""LIST METHODS
1.+ and *
2.index and sclicing
3.insert and extend
4.append
5.pop
6.remove
7.copy and clear
8.count
"""
data1=["1","4","2","3"]
data2=["india","uk","japan"]
print(data1+data2)
print(data1*6)

print(data1.index("2"))
print(data1[2:3])

print(data2.insert(2,"US"))
print(data2)

data1.extend(data2)
print(data1)
data1.append("5")
print(data1)

print(data1.pop())
print(data1)

out=data1.copy()
print(out)

print(out.remove("US"))
print(out)

out.clear()
print(out)

data1.extend(["1","1","2"])
print(data1)

print(data1.count("1"))