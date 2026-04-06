# Program practicing

s=""
if not s:#Empty string
    print("string is empty")
else:
    print("string is not empty")


s="Ghaniaaa"
print(s[::-1])#Reverse a string

print(s.count("a"))
#Count number of char
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1
print(d)#{'G': 1, 'h': 1, 'a': 4, 'n': 1, 'i': 1}

#reverse a list without using reverse()

list1=["a","b","c"]

#out=list1.reverse()
print(list1[::-1])#['c', 'b', 'a']
print(list1)#['a', 'b', 'c']

rev=[]
for i in range(len(list1)-1,-1,-1):
    rev.append(list1[i])
print(rev)#['c', 'b', 'a']


#Remove duplicates from a list

lst2=[1,2,1,3,3,2,2,4,1]

#print(list(set(lst2))) #[1, 2, 3, 4]
out=set(lst2)
print(list(out))#[1, 2, 3, 4]

#Find largest number in a list
lst3=[10,30,91,50,30,66]
#for i in range(len(lst3)):
print(max(lst3))

tu=('a','b','c','a','b','c')
#print(tu.add('e'))
#tu[0]=10
print(tu)

li=[1,2,3]

print(tuple(li))

#####Set
#find a common element
s1={1,2,3,4}
s2={2,4,9,8}
print(s1 & s2)
print(s1 ^ s2)
print(s1 != s2)
print(s1 == s2)

# Dictionary - Key exist or not
d={"name":"QA","exp":5}
if "exp1" in d:
    print("The key is existing")
else:
    print("The key doesn't exists")

d1={"a":10,"b":20,"c":0}
print(dict(sorted(d1.items())))#######################

print(bool(0))
print(bool(-1))
print(bool(1))
print(5>3)