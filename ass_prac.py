'''a=[1,2,3]
b=[1,2,3]
print(a == b)#True because == look for the values [check content not memory]
print(a is b)#False because 'is' operator is look for object references , a and b are diff memory locations. Checks memory/idedntity

x=10
y=10

print(x == y)#True
print(x is y)#True python uses memory for small integers

#What is the result of following comparisions?
'''
#0-0000, 1-0001, 2-0010, 3-0011, 4-0100, 5-0101, 6-0110, 7-0111, 8-1000, 9-1001, 10-1010, 11-1011, 12-1100, 13-1101, 14-1110, 15=1111
print(7>=3 and 4<2)#False
print(10 % 3 + 2*5)# 1 + 10 =11
print(10/2)#5.0
print(10//2)#5
print(4 << 1)#Bit wise operator  4 shift onetime means 0100 means 2**4*0+2**3*1+2**2*0+2**1*0 = 8
print(12>>2)#12 with 2 right shifts so 12/2 = 6, 6/2 =3, 2 shifts done result is 3
print(2**4*0+2**3*1+2**2*0+2**1*0)

print(not(5>3 or 2<1))#False
print((3+5) * (2 ** 2)/4)#8.0

list1 = [1,2,4]
print(len(list1) != 3)#False
print(10 & 7)#1010 & 0111 = 0010==>2

# Given a = 5 and b = 3 what is the result of the expression a^b?

a = 5
b = 3
print(a^b)#5^3 = 0101 xor 0011 = 0110=6

list1 =[1,2,3,4]
'''print(max(list1))#4
print(min(list1))#1

print(list1.index(4))
print(list1.remove(4))
print(list1)'''

max_num = list1[0]#1
min_num = list1[0]#1

for num in list1:
    if num > max_num:#2>1
        max_num = num#2
    if num < min_num:#1<2
        min_num = num#2

# Second max
second_max = list1[0]#1
for num in list1:
    if num != max_num and num > second_max:#2!=2 and 1>1
        second_max = num

print("Max:", max_num)
print("Second Max:", second_max)
print("Min:", min_num)
######################
#str2 = "malayalam"
#Check whether a given string is a palindrome.
#	Count how many times each character appears in a string.

str2 = "malayalam"

pall_str = ""

for i in range(len(str2)-1,-1,-1):
    pall_str += str2[i]
if str2 != pall_str:
    print("No the given string is not a pallindrome")
        
else:
    print("Yes, the string is  pallindrome")
#print(pall_str)

dict2 = {}
for i in str2:
    if i not in dict2:
        dict2[i] = str2.count(i)

print(dict2)#{'m': 2, 'a': 4, 'l': 2, 'y': 1}
#########################################
str1 = "abc"
str2 = "cba"
#	Check if two strings are anagrams of each other.
#	Check whether one string is a rotation of another.

s1 = sorted(str1)
s2 = sorted(str2)
if s1 == s2:
    print("Yes-angram")
else:
    print("Not an anagram")

#Method 2
rev_ang = ""
for i in range(len(str1)-1,-1,-1):
    rev_ang += str1[i]
print(rev_ang)

if str2 == rev_ang:
    print("Yes=Anagram")
else:
    print("No anagram")

#Method 3
if str1 == str2[::-1]:
    print("Yes-Anagram")
else:
    print("Not anagram")

    
#######
d1 = {"a":1, "b":2}
d2 = {"b":4, "d":2}

#Merging 2 dict and finding key or value exists or not
d3 = {}
for key,value in d1.items():
    if key in d2:
        print("key exists, the key is", key)#key exists, the key is b
        d3[key]=d1[key]+d2[key]##{'b': 6}

    else:
        d3[key]=value

for key,value in d2.items():
    if key not in d3:
        d3[key]=value

print(d3)#{'a': 1, 'b': 6, 'd': 2}


for key, value in d1.items():
    if value in d2.values():
        print("Values are exists", value)#Values are exists 2


##Finding and common unique keys

unique_key = set(d1.keys()) ^ set(d2.keys())#{'a', 'd'} symmetric diff
print(unique_key)

common_key = set(d1.keys()) & set(d2.keys())
print(common_key)#{'b'}

########get(), setdefault() is use For finding/getting value using key from a dictionary. If we want to add key and value we can do it with setdefault but not from get()method

d1 = {"a":10,"b":20,"c":15}

print(d1.get("c"))#15

print(d1.setdefault("c"))#15

print(d1.get("d",30))#None {}
print(d1.setdefault("d",40))#{"d":40}
print(d1.setdefault("e"))#{"e":None}

print(d1)#{'a': 10, 'b': 20, 'c': 15, 'd': 40, 'e': None}
######################################################

l1 = ["a","b","c"]
l2 = [1,2,3]

d1 = {}
for i,j in zip(l1,l2):
    #print(i,j)
    d1[i]=j
print(d1)#{'a': 1, 'b': 2, 'c': 3}

print(l1+l2)#['a', 'b', 'c', 1, 2, 3]

#l1.extend(l2)
print(l1)#['a', 'b', 'c', 1, 2, 3]
##############

print(l1+l2)#['a', 'b', 'c', 1, 2, 3, 1, 2, 3]

merged_list = [x for x in l1]+[ y for y in l2]
print(merged_list)#['a', 'b', 'c', 1, 2, 3]

#####################################

str1 = "My name is winteck"

#1.Reverse the string with slicing
print(str1[::-1])#kcetniw si eman yM

#2.Reverse the string without using inbuild methods
rev_str = ""
for i in range(len(str1)-1,-1,-1):
    rev_str += ""+str1[i]

print(rev_str) #kcetniw si eman yM

#3.Reverse the string based on words. o/p::”winteck is name my”
#4.Convert above string to list
temp = str1.split()
print(temp)#['My', 'name', 'is', 'winteck']
rev_list = []

for i in range(len(temp)-1, -1, -1):
    rev_list.append(temp[i])
print(rev_list)#['winteck', 'is', 'name', 'My']

rev_word = " ".join(rev_list)
print(rev_word)#winteck is name My

#5.Create a dictionary with above string key = character, value = count of each character{"M":1, "y":1, "n":2, "a":1, "m":1,"e":2, "i":2, "s":1,"w":1,"t":1,"c":1,"k":1," ":3}

dict1 = {}
for i in str1:
    dict1[i]=str1.count(i)

print(dict1)#{'M': 1, 'y': 1, ' ': 3, 'n': 2, 'a': 1, 'm': 1, 'e': 2, 'i': 2, 's': 1, 'w': 1, 't': 1, 'c': 1, 'k': 1}

#Without built in module count find char and char count

str1 = "My name is winteck"
dict2 = {}

for i in str1:
    if i != "":
        if i in dict2:
            dict2[i] += 1
            
        else:
            dict2[i] = 1

print(dict2)#{'M': 1, 'y': 1, ' ': 3, 'n': 2, 'a': 1, 'm': 1, 'e': 2, 'i': 2, 's': 1, 'w': 1, 't': 1, 'c': 1, 'k': 1}

#6.Print max_repeated charecter in string

max_val = max(dict2.values())
print(max_val)#3

for k,v in dict2.items():
    if v == max_val:
        print("Max repeated charecter is", k,":",v)#Max repeated charecter is   : 3(key is space)

###Second methos for finding max repeated char

max_char = ""
max_count = 0

for key in dict2:
    if dict2[key] > max_count:
        max_count = dict2[key]
        max_char = key

print("Max repeated char is",max_char)#Max repeated char is @ #Space is defficult to recognise in the output so I put @ in space
print(max_count)#3

#7. Print second max repeated charecter in the string

fir_max = 0
sec_max = 0
fir_char = ""
sec_char = ""

for key in dict2:
    count = dict2[key]

    if count > fir_max:
        sec_max = fir_max
        sec_char = fir_char
        fir_max = count
        fir_char = key

    elif count > sec_max and sec_max != fir_max:
        sec_max = count
        sec_char = key
        
print(fir_max)#3
print(fir_char)#space

print(sec_max)#2
print(sec_char)#n
######################################################################
s = "(()())()"

#print(s.count("(")) Find the largest substring count
# print(s[:-2])

open_count = 0
close_count = 0
max_len = 0

for ch in s:
    if ch == '(':
        open_count += 1
    else:
        close_count += 1
    
    if open_count == close_count:
        print("Valid :",s[:open_count + close_count])#(()())
        print(len(s[:open_count + close_count]))#6
        break


######################################## first 10 Prime numbers

n = 2
count = 0
l1 = []
while count < 10:
    for i in range(2,n):#0 and 1 are not prime numbers, and 2 is the first prime number.
        if n % i == 0:
            break
    else:
        #print(n , end=" ")
        l1.append(n)
        count += 1
    n += 1
print(l1)#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
"""list1 = []
for num in range(2,30):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        list1.append(num)

print(list1)"""
#Program to check given number is prime or not?
n = 29

for i in range(2, n-1):
    if n % i == 0:
        print(n, "is not a prime number")
        break
else:
    print(n , "is a prime number")

#72. Programming to find factorial of 10?
#n! = n × (n-1) × (n-2) × ... × 1
#10! = 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 3628800
#Factorial of a number is the product of all positive integers less than or equal to that number.”
n = 10
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)#3628800

#Fibannocci series till 100

a = 0
b = 1

while a <= 100:
    print(a, end=" ")#0 1 1 2 3 5 8 13 21 34 55 89
    a,b = b, a+b

####################
a , b = 0 , 1
for i in range(20):
    if a>100:
        break
    print(a, end=" ")#0 1 1 2 3 5 8 13 21 34 55 89
    a,b = b, a+b

#
#Find most repeated substring in main string
#Print largest substring
str1 = "My name is winteck and my country name is india"

l1 = str1.split()
print(l1)#['My', 'name', 'is', 'winteck', 'and', 'my', 'country', 'name', 'is', 'india']

print(sorted(l1))#['My', 'and', 'country', 'india', 'is', 'is', 'my', 'name', 'name', 'winteck']

dict1 = {}
for i in l1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1 

print(dict1)#{'My': 1, 'name': 2, 'is': 2, 'winteck': 1, 'and': 1, 'my': 1, 'country': 1, 'india': 1}
max_val=max(dict1.values())#2

for i,j in dict1.items():
    if dict1[i] == max_val:
        print("Most repeated word is", i,"in",j,"times" )#Most repeated word is name in 2 times; Most repeated word is is in 2 times


##Print largest substring
lar_word = "" 
sec_lar_word = ""
for word in l1:
    if len(word) > len(lar_word):
        sec_lar_word = lar_word
        lar_word = word
    elif len(word) > len(sec_lar_word) and word != lar_word:#if we keep 'and' logic the sec_lar will be india.
        sec_lar_word = word

print(lar_word)#winteck
print(sec_lar_word)#india
################
#union, intersection, symmetric diff,diff

set1 = {1,2,3}
set2 = {2,3,4}
print(set1 & set2)#{2, 3}
print(set1.intersection(set2))##{2, 3}

print(set1 | set2)#{1, 2, 3, 4}
print(set1.union(set2))#{1, 2, 3, 4}

print(set1 ^ set2)#{1, 4}
print(set1.symmetric_difference(set2))##{1, 4}

print(set1 - set2)#{1}
print(set2 - set1)#{4}
print(set1.difference(set2))#{1}

#############################
##Program to create flat list from list of lists?
#Find max. number from list of lists
#program to create new list [6,15,24]

list1 = [[1,2,3],[4,5,6],[7,8,9]]

flat_list = []
for i in list1:
    for j in i:
        flat_list.append(j)

print(flat_list)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#Using list comprehension
list_comp = [j for i in list1 for j in i]
print(list_comp)#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Max_num
sorted_list = sorted(flat_list)
print(sorted_list)#[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(sorted_list))#9

##method2 for max_list
list1 = [[1,2,3],[4,5,6],[7,8,9]]
max_num = 0

for sublist in list1:
    for num in sublist:
        if num>max_num:
            max_num = num
print(max_num)#9


#[6,15,24], 0, 1, 3*2 , 3, 4, 3*5, 6,7,3*8,[3*2,3*5,3*8]

new_list = []
for i in range(2,9,3):
    #print(i)
    new_list.append(3*i)
print(new_list)
##method2 for new_list=[6,15,24], [[1+2+3],[4+5+6],[7+8+9]]--->correct method
list1 = [[1,2,3],[4,5,6],[7,8,9]]
new_list = []

for sublist in list1:
    total = 0
    for i in sublist:
        total += i
    new_list.append(total)
print(new_list)#[6,15,24]
#############################################################
#Separate even and odd numbers from a list.
list1 = [10,20,1,2,5,3]
even = []
odd = []

for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)#[10, 20, 2]
print(odd)#[1, 5, 3]

#Method 2

even = [i for i in list1 if i%2 == 0]
print(even)
odd = [i for i in list1 if i%2 !=0]
print(odd)

#Check if a list is sorted or not.

print(sorted(list1))#[1, 2, 3, 5, 10, 20]

list1 = [10,20,1,2,5,3]

n=len(list1)
for i in range(n):#range(6)
    for j in range(0, n-i-1):#range(0,6-0-1)
        if list1[j] > list1[j+1]:
            list1[j] , list1[j+1] = list1[j+1] , list1[j]

print(list1)#[1, 2, 3, 5, 10, 20]
#######################
#Find the sum of all elements in a list.

list1 = [10,20,1,2,5,3]
print(sum(list1))#41

total = 0
for i in list1:
    total += i
print(total)#41
#####################################
#Remove all occurrences of a given element[3] from a list.
list1 = [10,3,20,1,3,2,5,3]

for i in list1:
    if i == 3:
        list1.remove(i)
print(list1)#[10, 20, 1, 2, 5]

#Method 2
list1 = [10,3,20,1,3,2,5,3]

new_list = []
for i in list1:
    if i==3:
        pass
    else:
        new_list.append(i)

print(new_list)#[10, 20, 1, 2, 5]

####
list1 = [10,3,20,1,3,2,5,3]
list1.remove(3)#removes only first occurence
print(list1)#[10, 20, 1, 3, 2, 5, 3]

####
list1 = [10,3,20,1,3,2,5,3]

rem = [i for i in list1 if i!=3]
print(rem)#[10, 20, 1, 2, 5]
######
while 3 in list1:
    list1.remove(3)
print(list1)#[10, 20, 1, 2, 5]

###############
list1 = [10,3,20,1,3,2,5,3]

result = list(filter(lambda i:i!=3,list1))
print(result)#[10, 20, 1, 2, 5]
#########################################################
###Rotate a list to the left by k positions.

list1 = [10, 20,0,99, 1, 2, 5,3,6,8,7,6,8,0]
#k=2
#k = k%len(list1)
list2 = list1[2:] + list1[:2]
print(list2)#[0, 99, 1, 2, 5, 3, 6, 8, 7, 6, 8, 0, 10, 20]

##Find all pairs in a list whose sum is a given number.

list1 = [3,5,-1,9,7,6,1,2]

target = 8

seen = set()
for num in list1:
    rem =   target - num
    if rem in seen:
        print((num,rem))
    seen.add(num)

#print(seen)

##Method 2
list1 = [3,1,2,2,5,1,-1,9]
target =4

for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        if target == list1[i] + list1[j]:
            print((list1[i],list1[j]))

'''(3, 1)
(3, 1)
(2, 2)
(5, -1)'''

##Split a list into two equal halves.

n = len(list1)//2

print([list1[:n] , list1[n:]])#[[3, 1, 2, 2], [5, 1, -1, 9]]

fir_half = []
sec_half = []
for i in range(len(list1)):
    if i < n:
        fir_half.append(list1[i])
    else:
        sec_half.append(list1[i])
print(fir_half)#[3, 1, 2, 2]
print(sec_half)#[3, 1, 2, 2]

##Replace every element in a list with its square.

list1 = [1,3,5,7,2,4,6]
n = len(list1)

for i in range(n):
    list1.insert(i,list1[i]**2)
del list1[n:]

print(list1)#[1, 1, 1, 1, 1, 1, 1]

list1 = [1,3,5,7,2,4,6]

for i in range(len(list1)):
    list1[i] = list1[i]**2

print(list1)#[1, 9, 25, 49, 4, 16, 36]

###Method 2
list1 = [1,3,5,7,2,4,6]
list_comp = [i*i for i in list1]
print(list_comp)#[1, 9, 25, 49, 4, 16, 36]

##Merge two lists and remove duplicates.
##Find the common elements between two lists.
list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,1,2]

mer_list = list1 + list2#[1, 2, 3, 4, 5, 6, 5, 6, 7, 8, 1, 2]
print(list(set(mer_list)))#[1, 2, 3, 4, 5, 6, 7, 8]

#Method2
mer_list = []
seen = set()
comm = []
for i in list1+list2:
    if i not in seen:
        mer_list.append(i)
        seen.add(i)
    else:
        comm.append(i)
print(mer_list)#[1, 2, 3, 4, 5, 6, 7, 8]
print(comm)#[5, 6, 1, 2]
        

#Flatten a nested list (single level only).
l1 = [1,2,3,[4,5,6],[10,20,30]]
flatten = []

for i in l1:
    if isinstance(i,list):
        flatten.extend(i)
    else:
        flatten.append(i)
print(flatten)#[1, 2, 3, 4, 5, 6, 10, 20, 30]

##Method 2
l1 = [1,2,3,[4,5,6],[10,20,30]]

flatten = [j for i in l1 for j in (i if isinstance(i,list) else [i])]
print(flatten)#[1, 2, 3, 4, 5, 6, 10, 20, 30]

l2 = [1,2,3,-10,-20,0]

#find negative numbers from list 

neg_num = []
for i in l2:
    if i<0:
        neg_num.append(i)
print(neg_num)#[-10, -20]

#Method 2

neg_num = [i for i in l2 if i<0]
print(neg_num)#[-10, -20]

l1 = [1,4,5,8,10]
#Find missing numbers from a list of consecutive numbers.

cons_num = []

for i in range(min(l1),max(l1)+1):
    if i not in l1:
        cons_num.append(i)

print(cons_num)#[2, 3, 6, 7, 9]
#Method 2
cons = [i for i in range(1,11) if i not in l1]
print(cons)#[2, 3, 6, 7, 9]

########################

##Create a dictionary with name, age and location with the following values: "John" , 30 and "New york"

new_dict = {}
new_dict["Name"] = "John"
new_dict["Age"] = 30
new_dict["Location"] = "New York"

print(new_dict)#{'Name': 'John', 'Age': 30, 'Location': 'New York'}

##Given a dictionary person - {'Name': 'Alice', 'Age': 25, 'Location': 'London'} print the value of key "age"

person = {'Name': 'Alice', 'Age': 25, 'Location': 'London'}

print(person["Age"])#25

#Add a new key "Job" and value is "Engineer" to the dictionary person

person["Job"] = "Engineer"

print(person)#{'Name': 'Alice', 'Age': 25, 'Location': 'London', 'Job': 'Engineer'}

####################
##Given a dictionary person - {'Name': 'Alice', 'Age': 25, 'Location': 'London'} print the value of key "age"

person = {'Name': 'Alice', 'Age': 25, 'Location': 'London'}

print(person["Age"])#25

#Add a new key "Job" and value is "Engineer" to the dictionary person

person["Job"] = "Engineer"

print(person)#{'Name': 'Alice', 'Age': 25, 'Location': 'London', 'Job': 'Engineer'}

##Update the "Age" key in the dictionary person to 26?
person["Age"] = 26

print(person)#{'Name': 'Alice', 'Age': 26, 'Location': 'London', 'Job': 'Engineer'}

## Remove the "Location" key in dictionary person? [A. We can remove a key from a dictionary using pop() or del keyword]

del person["Location"]
#person.pop("Location")
print(person)#{'Name': 'Alice', 'Age': 26, 'Job': 'Engineer'}

##Check if the key "Location" exists in the dict
if "Location" in person:
    print("key exists",key)
else:
    print("Key doesn't exists")#Key doesn't exists

##Write a loop to print both keys and values of the dictionary person

person1 = {'Name': 'Alice', 'Age': 25, 'Location': 'London', 'Job': 'Engineer'}

print(person1.keys())#dict_keys(['Name', 'Age', 'Location', 'Job'])
print(person1.values())#dict_values(['Alice', 25, 'London', 'Engineer'])

##Method 2
keys = []
values = []
for k,v in person1.items():
    keys.append(k)
    values.append(v)

print(keys)#['Name', 'Age', 'Location', 'Job']
print(values)#['Alice', 25, 'London', 'Engineer']

######################################
##Merge two dictionaries
dict1 = {"a":10 , "b": 20}
dict2 = {"c":30 , "d":40}

#dict1.update(dict2)
print(dict1)#{'a': 10, 'b': 20, 'c': 30, 'd': 40}[if we use update method it updated dict1 with dict2]

print(dict1 | dict2)#{'a': 10, 'b': 20, 'c': 30, 'd': 40}[if we use | operator, there is no changes in dictionaries]
print(dict1)

#################################
#If the keys are same add the values in a new dictionary
#if keys are the same, add their values, otherwise keep the value as it is.

dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dict2 = {"a":30, "e":40, "c":30}

new_dict = {}
for k in dict1:
    new_dict[k] = dict1[k]
for k in dict2:
    if k in new_dict:
        new_dict[k] += dict2[k]

    else:
        new_dict[k] = dict2[k]
print(new_dict)#{'a': 40, 'b': 20, 'c': 60, 'd': 40, 'e': 40}

##method 2
print(dict1 | dict2)#{'a': 30, 'b': 20, 'c': 30, 'd': 40, 'e': 40}

#Method3
#dict1.update(dict2)
print(dict1)#{'a': 30, 'b': 20, 'c': 30, 'd': 40, 'e': 40}

#Method 4
res = {}
for k in dict1:
    res[k]=dict1[k]
for k in dict2:
    res[k] = res.get(k,0) + dict2[k]

print(res)#{'a': 40, 'b': 20, 'c': 60, 'd': 40, 'e': 40}

#####################################
#If the keys are same create a list as a value in new dictionary and add two num. o/p::{"a":[10,30],"b":20,"c":[30,30],"d":40,"e":40}
dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dict2 = {"a":30, "e":40, "c":30}

res = {}


for k in dict1:
    res[k]=dict1[k]

for k in dict2:
    if k in res:
        list1 = []
        list1.append(dict1[k])
        list1.append(dict2[k])
        res[k] = list1#res[k] = [dict1,dict2]
    else:
        res[k] = dict2[k]

print(res)#{'a': [10, 30], 'b': 20, 'c': [30, 30], 'd': 40, 'e': 40}

###Ignore common keys while creating a new dictionary and Print only the common keys

dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dict2 = {"a":30, "e":40, "c":30}

res = {}
#ignoring common keys o/p:{'b': 20, 'd': 40, 'e': 40}

for k in dict1:
    if k not in dict2:
        res[k] = dict1[k]

for k in dict2:
    if k not in dict1:
        res[k] = dict2[k]

print(res)#{'b': 20, 'd': 40, 'e': 40}

#Print only the common keys
comm_keys = {}
comm_lst = []
for k in dict1:
    if k in dict2:
        comm_keys[k] = dict1[k]
        comm_lst.append(k)
for k in dict2:
    if k in dict1:
        comm_keys[k] = dict2[k]
        #comm_lst.append(k)
print(comm_keys)#{'a': 30, 'c': 30}
print(comm_lst)#['a', 'c']

#Another method
s1 = set(dict1.keys())
s2 = set(dict2.keys())
print(s1)#{'b', 'a', 'c', 'd'}
print(s2)#{'c', 'e', 'a'}

print(s1.intersection(s2))#{'a', 'c'}[common keys only]
print(s1.union(s2))#{'b', 'c', 'e', 'd', 'a'}[all keys from 2 dictionaries]
print(s1.difference(s2))#{'d', 'b'}
print(s2.difference(s1))#{"e"}
print(s1.symmetric_difference(s2))#{'b', 'd', 'e'}
print(s2.symmetric_difference(s1))#{'b', 'd', 'e'}

###################################
#Find key with max value and min value
dict1 = {"a":40, "b":20, "c":70,"d":50,"e":40}

max_val = dict1["a"]
max_val_key = ""

for k in dict1:
    if dict1[k]>max_val:
        max_val = dict1[k]
        max_val_key = k

print("Maximum value is",max_val)#Maximum value is 70
print("Maximum value key is ",max_val_key)#Maximum value key is  c

#Find munimum value

min_val = dict1["a"]
min_val_key = ""

for k in dict1:
    if dict1[k]<min_val:
        min_val = dict1[k]
        min_val_key = k

print(min_val)#20
print(min_val_key)#b
##################################
#o/p: {"a":2,"b":3,"c":2}
str1 = "aabbbcc"

res = {}
for i in str1:
    if i not in res:
        res[i] = str1.count(i)

print(res)#{'a': 2, 'b': 3, 'c': 2}

########Method 2
out = {}
count = 0
for i in str1:
    if i not in out:
        out[i] = 1
    else:
        out[i] += 1

print(out)#{'a': 2, 'b': 3, 'c': 2}
###############################
#Given two lists, create a dictionary using 2 lists where each key corresponding to value, elements keys and value pair.o/p=#{'a': 1, 'b': 2, 'c': 3}

keys = ["a","b","c"]
values = [1,2,3]

new_dict = {}
for k,v in zip(keys,values):
    new_dict[k] = v

print(new_dict)#{'a': 1, 'b': 2, 'c': 3}

print(dict(zip(keys,values)))#

#Method 2
res = {}
for i in range(len(keys)):
    res[keys[i]] = values[i]

print(res)#{'a': 1, 'b': 2, 'c': 3}

#Using dict coprehension

new_dict = {keys[i]:values[i] for i in range(len(keys))}
print(new_dict)#{'a': 1, 'b': 2, 'c': 3}

###If we take un equal leanght inputs, When lists have unequal lengths, 
# zip() safely pairs elements up to the shortest list, or we can handle missing values manually using loops.

keys = ["a", "b", "c", "d"]
values = [1, 2, 3]
result = dict(zip(keys, values))
print(result)#{'a': 1, 'b': 2, 'c': 3}['d' is ignored because there is no value for it.]or [limit = min(len(keys), len(values))]

#########
result = {}

for i in range(len(keys)):
    if i < len(values):
        result[keys[i]] = values[i]
    else:
        result[keys[i]] = None

print(result)#{'a': 1, 'b': 2, 'c': 3, 'd': None}
################################################

##Given a dict {"name":"John", "age":30, "city":"New york"} convert it into list of tuple list of tuple

person = {"name":"John", "age":30, "city":"New york"}

print(list(person.items()))#[('name', 'John'), ('age', 30), ('city', 'New york')]

##method2

res = [(k,v) for k,v in person.items()]
print(res)#[('name', 'John'), ('age', 30), ('city', 'New york')]

####Method 3
res = []
for k,v in person.items():
    res.append((k,v))

print(res)#[('name', 'John'), ('age', 30), ('city', 'New york')]

##########################################
##list1 = ["a","b","c","a","b"],o/p = {2:"a",2:"b",1:"c"}
#{2: "a", 2: "b", 1: "c"} ❌ This is NOT valid in Python, because:Dictionary keys must be unique; Key 2 appears twice
#Python will overwrite the first value; So Python will finally store:{2: "b", 1: "c"}

list1 = ["a","b","c","a","b"]
res = {}
for i in list1:
    if i not in res:
        res[i]=1
    else:
        res[i] += 1

print(res)#{'a': 2, 'b': 2, 'c': 1}

out = {}
for k,v in res.items():#{'a': 2, 'b': 2, 'c': 1}#res
    #out[v] = k
#print(out)#{2: 'b', 1: 'c'}#Python will overwrite the first value
    if v in out:#after 2:a, b:2, 2 again listed so out[v].append(b)#alread we have [a]after appending it will be [a,b]
        out[v].append(k)#
    else:
        out[v] = [k]#out[2]='a',
print(out)#{2: ['a', 'b'], 1: ['c']} #This is logically correct; This is what interviewers expect
##Dictionary keys must be unique, so when multiple elements have the same count, we store them as a list under that count.
############################################
#words = ["cat","dog","elephant","bat","batman"] ; o/p = {3 : ["cat","dog","bat"], 8:["elephant","batman"]}

words = ["cat","dog","elephant","bat","batman"]

res = {}
for word in words:
    length = len(word)
    if length in res:
        res[length].append(word)
    else:
        res[length] = [word]
print(res)#{3: ['cat', 'dog', 'bat'], 8: ['elephant'], 6: ['batman']}[This logic based on length]

#####################if we want exact output

out = {}
for word in words:
    length = len(word)
    if length <= 3:
        key = 3
    else:
        key = 8
    if key in out:
        out[key].append(word)

    else:
        
        out[key] = [word]

print(out)#{3: ['cat', 'dog', 'bat'], 8: ['elephant', 'batman']}
########################################################

company = {
    "department1":{
        "name" : "sales",
        "emplyees":{
            "e1":{"name" : "John", "age":30,"position":"manager"},
            "e2":{"name": "Alice", "age":25,"position":"sales associate"}
        },
        "budjet":100000
    },
    "department2" : {
        "name" : "Engineering",
        "emplyees":{
            "e3":{"name" : "Bob", "age":35,"position":"team lead"},
            "e4":{"name": "Charlie", "age":28,"position":"software Engineer"}
        },
        "budjet":200000
    },
    "department3": {
        "name" : "Marketing",
        "emplyees":{
            "e5":{"name" : "Devid", "age":32,"position":"marketing manager"},
            "e6":{"name": "Eve", "age":27,"position":"SEO specialist"}
        },
        "budjet":50000
    }
}

#Print all keys from above dict

list1 = company.keys()#dict_keys(['department1', 'department2', 'department3'])
print(list1)

#Print "department1"
for k,v in company.items():
    print(k)#department1
    break

#To get the total budget of the cumpany[summing all department budgets]

tot_bud = 0
for k,v in company.items():#k is department,v is {name,employees,budget}
    for k1,v1 in v.items():#k1 is {name,employees,budget},v1 is values of name,employees,budget(100000,200000,50000)
        if k1 == "budjet":
            tot_bud += v[k1]#tot_bud = 0+100000, then 100000+200000, then 300000+50000

print(tot_bud)#350000

#########################
#To get age of "John"

step1 = company["department1"]["emplyees"]["e1"]["name"]#John
print("John")
########################################
#To get the position of Devid

step2 = company["department3"]["emplyees"]["e5"]["name"]#Devid
print(step2)

###########################
#which department has lowest budget
#None is used as a safe initial placeholder when finding min/max values dynamically.
#No department budget is less than 0; Condition dept["budjet"] < min_budget is never true; Result stays wrong

min_bud = None
min_dep = ""

for dep in company.values():
    if min_bud is None or dep["budjet"] < min_bud:
        min_bud = dep["budjet"]
        min_dep = dep["name"]

print(min_bud)#50000
print(min_dep)#Marketing

#########################################
#Method 2

first_key = list(company.keys())[0]
min_budget = company[first_key]["budjet"]
min_department = company[first_key]["name"]

for dept in company.values():
    if dept["budjet"] < min_budget:
        min_budget = dept["budjet"]
        min_department = dept["name"]

print(min_budget)
print(min_department)

###############################################
#Implement a function to find second largest number in a list
def largest(list1):
    max_num = list1[0]#1

    for i in list1:
        if i > max_num:
            max_num = i
    print("Max:", max_num)

    second_max = list1[0]#1
    for num in list1:
        if num != max_num and num > second_max:#2!=2 and 1>1
            second_max = num
           
    #print("Second Max:", second_max)
    return second_max


res =largest([10, 20, 4, 45, 99])
print("The second largest num is",res)

#####################################
#d1 = {"a":10, "b":20, "c":20,"d":30}

#write in function way key of a max. value

def maximum(d1):
    value = max(d1.values())#30
    
    max_key = ""
    for k,v in d1.items():
        if d1[k] == value:
            
            max_key = k
            return max_key
print(maximum({"a":10, "b":20, "c":20,"d":30}))