"""

s="aaabbccdab"#out="a3b2c2d1a1b1"
out=""
count=1
for i in range(1,len(s)):#5
    if s[i]==s[i-1]:#c == b faulse go to else statement
        count += 1#2
    else:
        out += s[i-1]+str(count)#out= b+2
        count = 1
out += s[-1]+str(count)
print(out)



# Reverse a number without converting to a string

num = 1023456
rev_num = 0#6

while num>0:#102345>0
    digit = num%10#6 extracts last digit
    rev_num = rev_num * 10 + digit#65
    num = num // 10 #remove the last digit that is 12345

print(rev_num)


#python program for inp is l1=[1,0,0,1,1,0] and out=[0,0,0,1,1,1] without empty list
#l1=[1,0,0,1,1,0]
#l1.sort()
#print(l1)
l1 = [1, 0, 0, 1, 1, 0]

count_0 = l1.count(0)#3
count_1 = l1.count(1)#3

for i in range(count_0):#3 means 0,1,2
    l1[i] = 0#1

for i in range(count_0, count_0 + count_1):#3,3+3
    l1[i] = 1#1

print(l1)

#print longest string inp="aaabbccccccddddccaa", out="cccccc"
inp="aaabbccccccddddccaa"

max_char = inp[0]#a
max_len = 1

current_char = inp[0]#a
current_len = 1#3#2#1

for i in range(0,len(inp)):#0 1 2
    if inp[i] == current_char:#c == b
         current_len +=1#2
              
    else:
         current_char = inp[i]#b#c
         current_len = 1
    if max_len < current_len:
        max_char = current_char
        max_len = current_len
#print(max_char * max_len)
#print(max_char,max_len)

print(max_char*max_len)#cccccc
"""

#inp=[10,20,30,100,40,50,60] and the out=[40,50,60,100,10,20,30] the middle index 100 should be there only.

inp=[10,20,30,100,40,50,60]

mid = len(inp) // 2 #3
print(inp[mid])
#print(inp[mid+1:]+[inp[mid]]+inp[:mid])
print(inp[mid+1:]+inp[mid:mid+1]+inp[:mid])


