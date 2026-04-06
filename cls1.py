'''class Cls1():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("This is an instance method")
        print(a)
obj1=Cls1(100,200)
print(obj1.b)

'''

class Cls2():
    z=100
    def __init__(self,m,n):
        self.m=m
        self.n=n
        print(m,n)

    def method1(self,x,y):
        print(self.m)
        return x+y
obj=Cls2(1,2)
obj2=obj.method1(10,30)
print(obj2)
print(Cls2.z)
z=1000
print(z)