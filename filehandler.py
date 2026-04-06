with open("C:/Users/GHANEEBI/Python practice/file1.txt","r") as fh:
    #data=fh.read()
    lines=fh.readlines()
    #line=fh.readline()
#print(data)
print(lines)
#print(line)

#copy first 4 lines to a newfile

print(lines[0:4])