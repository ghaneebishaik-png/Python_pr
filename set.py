"""Set Methods
1. Set has no order and doesn't support duplicates
2.no indexing, no sclicing, no + and no *
3.add(Mutable)
4.update
5.remove
6.copy and clear
7.issubset
8.pop()
"""
data1={"india","uk","japan"}
data2={"1","2","3"}

data1.add("Aus")
print(data1)
data2.update(data1)
print(data2)

data1.remove("japan")
print(data1)

out=data1.copy()
print(data1)
print(out)

out.clear()
print(out)

print(data1.issubset(data2))
print(data2.issubset(data1))

print(data1)
print(data2)

data2.pop()
print(data2)