#Function to read data and return file contents.

def display_file_contents(filename,mode="read"):
    f1=open(filename,"r")
    if mode == "readlines":
        return f1.readlines()
    elif mode=="readline":
        return f1.readline()
    return f1.read()

#Display file contents(file1.txt)

def search_keyword(filename,keyword):
    file_content=display_file_contents(filename)
    if keyword in file_content:
        return True
    return False

def count_lines_file(filename):
    contents = display_file_contents(filename,mode="readlines")
    return len(contents)

def get_first_line(filename):
    line=display_file_contents(filename,mode="readline")
    return line

#def no_of_characters(filename,mode)

def get_no_of_char(filename):
    global lst
    lst=[]
    char=display_file_contents(filename,mode="read")
    #print(char)
    #for i in char:
        #print(char)
        #lst.append(i)
        #print(lst)
    count=len(char)
    return count



#first func call
out=display_file_contents("C:/Users/GHANEEBI/Python practice/file1.txt",mode="readline")#mode="readlines"
print(out)

filename="C:/Users/GHANEEBI/Python practice/file1.txt"
out1=search_keyword(filename,"Ghaneeba")#Ghaneebi which is True
print(out1)

out2=count_lines_file(filename)
print(out2)

out3=get_first_line(filename)
print(out3)

out4 = get_no_of_char(filename)
print(out4)
#print(lst)