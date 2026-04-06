#How to create a file and perform write operation in that file

file1 = open("C:/Users/GHANEEBI/Python practice/file1.txt","w")
#print(newfile1.read())

file1.write("This is first line and \n")
file1.write("This is second line\n")
file1.write("a\n")
file1.write("b\tc")
file1.close()

#Read operation

fr=open("C:/Users/GHANEEBI/Python practice/file1.txt","r")
#print(fr.read())
#print(fr.readline())
print(fr.readlines())
#data=fr.read()
#print(data)
#print(type(data))
fr.close()

#append content to the file

fa=open("C:/Users/GHANEEBI/Python practice/file1.txt","a")

fa.write("\nGhaneebi")

