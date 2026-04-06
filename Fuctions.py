### Fuctions
"""
def common():
    global x
    x=10
    print("inside-x", x)
    print(locals())
    print(globals())
z=300
common()
print("outside_x",x)

def common(l1,l2):
    global l3
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    print(l3)
    #return l3
x=[10,20,30,40]
y=[40,30,90]
out=common(x,y)
print("outside", l3)

print(len(x))"""


def func1(a,b):
    print(f"The value of a is {a} and b is {b}")
    print(a+b)
#result=func1(10,20)
#print(result)

#global
x=100
def fun1():
    global x
    x=20
    return x
print(x)
print(fun1())
print(x)