l1 = []
for i in range(5):
    l1.append(i)
print(l1)


list1 = []
print(list1)

t1 = ()
print(t1)
print(type(t1))

t2 = 1,2,3,4
print(t2)
print(type(t2))

t3 = 1,2,
print(t3)
print(type(t3))

t4 = (1,)#In Python, a single-element tuple must have a comma like (1,). Without the comma (1) is treated as an integer because the comma defines the tuple.
print(t4)
print(type(t4))

l1 = [9,8,7,6]
print(l1[0])

t1 = (9,8,7,6)
print(t1[-1])

print(l1[2])
l1.insert(2,5)
print(l1)

l1.remove(5)
print(l1)

print(l1.pop(0))
print(l1)

l1 = [0,1,2,3,4,5,6]
print(l1[0:3])

print(l1[-2:])
print(l1[::-1])
print(l1[-1::-1])

print(l1[2:6])

l2 = [10,20,30,40,50]
l2.extend([1,2,3])
print(l2)

print(l2.count(10))
print(l2.index(40))

out = sorted(l2)
print(out)#[1, 2, 3, 10, 20, 30, 40, 50] {l2.sort()}
l2.sort(reverse = True)
print(l2)#[50, 40, 30, 20, 10, 3, 2, 1]

print(sorted([2,4,6,1,2,4]))

str1 = "GHANEEBI"
print(str1.upper())

str1 = "My name is winteck"

d1 = {}
for i in str1:
    if i != "":
        if i in d1:
            d1[i] += 1
        else:
            d1[i]=1

print(d1)

list1 = []
for num in range(2,30):#3
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        list1.append(num)

print(list1)



str1 = "My name is winteck and my country name is india"
list1 = str1.split()
print(list1)#['My', 'name', 'is', 'winteck', 'and', 'my', 'country', 'name', 'is', 'india']

dict1 = {}
for i in list1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)#{'My': 1, 'name': 2, 'is': 2, 'winteck': 1, 'and': 1, 'my': 1, 'country': 1, 'india': 1}

lar1 = ""
lar2 = ""
for word in list1:
    if len(word) > len(lar1):
        lar1 = word
    if len(word) > len(lar2) and word != lar1:
        lar2 = word
print(lar1)
print(lar2)

list1 = [10,20,1,2,5,3]

tot = 0
for i in list1:
    tot += i
print(tot)

list1 = [3,5,-1,9,7,6,1,2]
target = 8
seen = set()
for num in list1:
    rem = target -num
    
    if rem in seen:
        print(f"sum of {rem},{num} is {target}")
    seen.add(num)

list1 = [1,3,5,7,2,4,6]
for i in range(len(list1)-1):
    list1.remove(list1[i])
    list1.append(list1[i]**2)

print(list1)

