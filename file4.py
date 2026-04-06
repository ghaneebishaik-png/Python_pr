import sys
#sys.path.insert(0,"E:\\")
#import module1

##How to pass the input arguments from commandline
print(sys.argv)#python file4.py 10 , 20, 30
#['file4.py', '10', '20', '30']

print(sys.argv[0])
print(sys.argv[1])#python file4.py 44,55, 66
#['file4.py', '44', '55', '66']
#file4.py
#44

x=(sys.argv[1])
y=(sys.argv[2])
print(x+y)