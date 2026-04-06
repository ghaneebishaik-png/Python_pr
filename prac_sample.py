str1 = "Winteck Software Solutions"
vowels = "aeiouAEIOU"
dict1 = {}
count =0
for i in str1:
    if i in vowels:
        dict1[i]=str1.count(i)
        count += 1

print(dict1)
print(count)

rev_str = ""
for i in range(len(str1)-1,-1,-1):
    rev_str += str1[i]
print(rev_str)

print(str1.replace(" ",""))

l1 = str1.split()
print(l1)

longest = l1[0]
for i in l1:
    if len(i) >len(longest):
        longest = i
print(longest)
print(len(longest))

str2 =""
for i in str1:
    if i in vowels:
        str2 += "*"
    else:
        str2 += i
print(str2)

count_u = 0
count_l = 0
for i in str1:
    if i.isupper():
        count_u += 1
    elif i.islower():
        count_l += 1

print(count_u)
print(count_l)

str3 = ""
non_rep = ""

for i in str1:
    if i not in str3:
        str3 += i
    else:
        non_rep += i
        break

print(str3)
print(non_rep)
unique = ""
for i in str1:
    if str1.count(i) == 1:
        unique = i
        break
print(unique)

str2="uique string with digits 99 ghaneebi"
for i in str2:
    if i.isdigit():
        print(i)

l1 = str2.split()

print(len(l1))
print(str2.title())
word = ""
for i in l1:
    word += i.capitalize() + " "
print(word)

l2 = [i.capitalize() for i in l1 ]
print(l2)
print(" ".join(l2))
