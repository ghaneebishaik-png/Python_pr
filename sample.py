#Count the number of vowels in a given string

str1 = "Winteck Software Solutions"
vowels = "aeiouAEIOU"

count = 0
for i in str1:
    if i in vowels:
        count +=1
print("No.of vowels in the string is",count)#9

#Reverse a string without using built-in reverse functions.
rev_str = ""
for i in range(len(str1)-1, -1, -1):
    rev_str += str1[i]

print(rev_str)#snoituloS erawtfoS kcetniW

print(str1[::-1])#snoituloS erawtfoS kcetniW

#Remove all spaces from a string.

print(str1.replace(" ", ""))#WinteckSoftwareSolutions
#Method 2
without_space = ""
for i in str1:
    if i == " ":
        pass
    else:
        without_space += i

print(without_space)#WinteckSoftwareSolutions

#Find the longest word in a sentence.

list1 = str1.split()
print(list1)#['Winteck', 'Software', 'Solutions']

long_num = len(list1[0])

for i in list1:
    if len(i) > long_num:
        long_num = len(i)
print(i)#Solutions

print(long_num)#9

#Replace all vowels in a string with *.

new_str = ""
for i in str1:
    if i in vowels:
        new_str += "*"
    else:
        new_str += i

print(new_str)#W*nt*ck S*ftw*r* S*l*t**ns

#Count uppercase and lowercase letters in a string.

count_u = 0
count_l = 0

for i in str1:
    if i.isupper():
        count_u += 1
    elif i.islower():
        count_l += 1

print(count_u)
print(count_l)

#Remove all duplicate characters from a string.

"""rem_duplicate = set(str1)
print(str(rem_duplicate))
res = ""
for i in rem_duplicate:
    res += i

print(res)#SfWinkwacls ueotr"""

rem_dup = ""
for i in str1:
    if i not in rem_dup:
        rem_dup += i
print(rem_dup)#Winteck Sofwarlus

#Find the first non-repeating character in a string.

non_rep = ""

for i in str1:
    if str1.count(i) == 1:
        non_rep = i
        break
print(non_rep)#W

#Check if a string contains only digits.

str2 = "Winteck Software 99 Solutions88"
dig = ""
for i in str2:
    if i.isdigit():
        dig += i

print(dig)#9988

#Find the number of words in a string

words = str1.split()

print(len(words))#3

#Capitalize the first letter of each word in a string.

str3 = "winteck software solutions"

print(str3.title())#Winteck Software Solutions

#method 2

l2 = str3.split()
print(l2)#['winteck', 'software', 'solutions']

fir_cap = ""
for word in l2:
   fir_cap +=  "".join(word.capitalize()) + " "

print(fir_cap)#Winteck Software Solutions

#Find the most frequent character in a string.

str1 = "Winteck Software Solutions"
fre_char = {}
char = ""
for i in str1:
    if i not in char or i == " ":
        char += i
    else:
        fre_char[i] = str1.count(i)

print(char)#Winteck Sofwar lus#non repeated chars and rep space
print(fre_char)#{'t': 3, 'e': 2, 'S': 2, 'o': 3, 'i': 2, 'n': 2}

max_rep_keys = []
max_rep_val = max(fre_char.values())#3
print(max_rep_val)
for k,v in fre_char.items():
    if v == max_rep_val:
        #print("char for max repeated value: ",k)
        max_rep_keys.append(k)

print(max_rep_keys)#['t', 'o']

#Split a string into characters and store them in a list.

#print(str1.split())

list1 = []
for i in str1:
    list1.append(i)
print(list1)#['W', 'i', 'n', 't', 'e', 'c', 'k', ' ', 'S', 'o', 'f', 't', 'w', 'a', 'r', 'e', ' ', 'S', 'o', 'l', 'u', 't', 'i', 'o', 'n', 's']

print(list(str1))#['W', 'i', 'n', 't', 'e', 'c', 'k', ' ', 'S', 'o', 'f', 't', 'w', 'a', 'r', 'e', ' ', 'S', 'o', 'l', 'u', 't', 'i', 'o', 'n', 's']

list2 = [char for char in str1]
print(list2)#['W', 'i', 'n', 't', 'e', 'c', 'k', ' ', 'S', 'o', 'f', 't', 'w', 'a', 'r', 'e', ' ', 'S', 'o', 'l', 'u', 't', 'i', 'o', 'n', 's']

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
#################################
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


##############LIST#####################

list1 = [10,20,1,2,5,3]
#Find the largest and smallest element in a list.

lar_ele = max(list1)
sma_ele = min(list1)
print(lar_ele)#20
print(sma_ele)#1

#Method 2

min_val = list1[0]
max_val = list1[0]

for i in list1:
    if i > max_val:
        max_val = i

    elif i < min_val:
        min_val = i
print(max_val)#20
print(min_val)#1

##Remove duplicate elements from a list.
list1 = [10,20,1,2,5,3,10,5,1,1,1]
rem_dup = []
#print(list(set(list1)))#[1, 2, 3, 5, 10, 20]

for i in list1:
    if i not in rem_dup:
        rem_dup.append(i)
print(rem_dup)#[10, 20, 1, 2, 5, 3]

#Count how many times each element appears in a list.

dict1 = {}
for i in list1:
    if i not in dict1:
        dict1[i] = list1.count(i)

print(dict1)#{10: 2, 20: 1, 1: 4, 2: 1, 5: 2, 3: 1}

#Reverse a list without using reverse().
list1 = [10,20,1,2,5,3]
rev_l = []
for i in range(len(list1)-1,-1,-1):
    rev_l.append(list1[i])

print(rev_l)#[3, 5, 2, 1, 20, 10]

#Find the second largest number in a list.

sec_max_val = list1[0]

for i in list1:
    if i > sec_max_val and i != max_val:#T * T = T
        sec_max_val = i

print(sec_max_val)#10

#Separate even and odd numbers from a list.
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

#Find the sum of all elements in a list.

list1 = [10,20,1,2,5,3]
print(sum(list1))#41

total = 0
for i in range(len(list1)):
    total += list1[i]
print(total)#41

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

#################################
dict1 = {"apple": 5, "banana": 2, "cherry": 7, "date": 3}

dict2 = {}
list1 = list(dict1.values())
print(list1)#[5, 2, 7, 3]
list2 = []

print(sorted(list1))#[2, 3, 5, 7]
for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
print(list2)
