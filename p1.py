#String is a collection of characters used to store text data. It can include letters, numbers, symbols and spaces written inside quotes.
#In python string enclosed in single quote and double quote('' , "").
#A multilined string is a string that contains text on more than oneline. It allows you to write multiple lines without using \n.
#Multilined string is used for documentation.

#List all supported methods of Strings with examples 
#print(dir(str))

'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
 'rfind', 'rindex', 'rjust','rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
   'translate', 'upper', 'zfill'
'''
#How to find index of a given character
s1 = "abcdks"
print(s1.index("d"))#3

#What is the difference between find() and index() methods
print(s1.find("d"))#3

#print(s1.index("g"))#ValueError
print(s1.find("g"))#-1
#Both methods locate substrings, but find() returns -1 when not found, whereas index() raises an exception
"""
#What is string slicing in Python?
#Extracting a part(substring) form a string using index position.
'''string[start:stop:step]
start = where to start(included)
stop = where to stop(excluded)
step = how many characters to skip'''

#What does s[2:5] return for s = "abcdefgh"?
s = "abcdefgh"
print(s[2:5])#cde
print(type(s[2:5]))#str

print(s[::2])#aceg

#How do you get the last character of a string s = "python"?
s = "python"
print(s[-1])#n
print(s[-1:])#n

#What does s[3:-2] return for s = "programming"?
s = "programming"
print(s[3:-2])#grammi
#How would you reverse a string s = "hello" using slicing
s = "hello"

print(s[::-1])#olleh

#Given the string s = "data science", how do you extract "science" using slicing?
s = "data science"
print(s[5::])#science

#How do you extract every second character from s = "abcdefgh"?
s = "abcdefgh"

print(s[1::2])#bdfh

#If s = "hello world", what will s[1:8:2] return?
s = "hello world"
print(s[1:8:2])#el o

#What is the result of s[-3:-1] for s = "python"?
s = "python"
print(s[-3:-1])#ho

#How can you get the substring "lo wo" from s = "hello world" using slicing?
s = "hello world"
print(s[3:8])#lo wo

#For s = "abcdefgh", how can you get a substring "cdefg" using slicing?
s = "abcdefgh"
print(s[2:-1])#cdefg

#How do you extract the substring "python" from s = "I love python programming"?
s = "I love python programming"
print(s.index("python"))#7
print(s[7:13])#python

#Given s = "123456789", how do you get the substring "45678" using slicing?
s = "123456789"
print(s[3:-1])#45678

##For a string s = "abcdefgh", what does s[-5:-1:2] return? 
s = "abcdefgh"
print(s[-5:-1:2])#df

#How can you use slicing to replace the first two characters of s = "hello" with "HE"?
s = "hello"
s = "HE" + s[2::]
print(s)#HEllo (Python strings are immutable, so methods like upper() don’t modify the original string — they return a new string)

#Given s = "a1b2c3d4e5", how do you extract the numeric characters "12345"?
s = "a1b2c3d4e5"
print(s[1::2])#12345

#What is the result of s[::4] for s = "abcdefgh"?
s = "abcdefgh"
print(s[::4])#ae

print(s.find("l"))#-1
print(s.index("l"))#ValueError: substring not found


#######################################
#nums = [1,2,10,5,7] output : true
#nums = [2,3,1,2]  output : False
#nums = [1,1,1]  output : false


# l1 = [1,2,10,5,7]
l1 = [2,3,1,2]
# l1 = [1,1,1]

count = 0
index = -1
for i in range(1, len(l1)):
    if l1[i] <= l1[i-1]:
        count += 1
        index = i
        
        if count > 1:
            print(False)
            break
else:
    if count == 0:
        print(True)
    else:
        if index >= 2 and l1[index] <= l1[index-2]:
            l1.pop(index)
        else:
            l1.pop(index-1)
        print(True)
        print(l1)


####################################################
l= [3,6,1,5,2,3,6,7,3,9,3,9,1]

count = 0
# res = []
# for num in l:
#     if num == 3:
#         count += 1
#         if count == 2:
#             continue
#     res.append(num)
# print(res)

for index, value in enumerate(l):
    if value == 3:
        count += 1
        if count == 2:
            l.pop(value)
            break
        print(l)


##################################################
class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        super().__init__()   # Call parent constructor
        self.y = 1

def main():
    b = Derived_Test()
    print(b.x, b.y)

main()
"""
###########################################
_9b=27
print(_9b)

import subprocess

cmd = "ipconfig"
output = subprocess.getoutput(cmd)
print(output)


##############################

a=10
b=20

print(f"{a} and {b} is {a+b}")










