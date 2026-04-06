## Inheritence-->Single level inheritence
''' 
class Cls1:
    def method1(self):
        print("In method1")
class Cls2(Cls1):
    def method2(self):
        print("In method2")

obj=Cls2()#Cls2 inherits the properties of Cls1 so that it can access Cls1 as well
obj.method1()
obj.method2()

'''

##Multi inheritence

class Cls1:
    def __init__(self,a):
        self.a = a
        #print(self.a)
        
    def method1(self):
        print(self.a)

class Cls2(Cls1):
    def __init__(self,a,b):
        super().__init__(a)#super() itself acts an object so that we no need to mentioned self
        self.b=b
        #print(self.b)
    def method2(self):
        #self.method1()
        print(self.b)

class Cls3(Cls2):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def method3(self):
        print(self.c)

obj1=Cls3(100,200,300)
#obj1.method3()#We call method1(parent class)in child class using inheritence



##Multiple inheritence

class Parent_class1():
    def __init__(self,arg1):
        self.arg1=arg1

    def method1(self):
        return self.arg1

class Parent_class2():
    def __init__(self,arg2):
        self.arg2=arg2
    def method2(self):
        return self.arg2
    
class Parent_class3(Parent_class1,Parent_class2):
    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg1)
        #super().__init__(arg2)#We can not use super() at multiple times(and we should use super in last child class only)
        Parent_class2.__init__(self,arg2)
        self.arg3=arg3
    def method3(self):
        return self.arg3
    
obj3=Parent_class3(10,20,30)
print(obj3.method3())
print(obj3.method2())
print(obj3.method1())


##
class C1:
    def method1(self):
        print("In C1 method1")

class C2:
    def method1(self):
        print("In C2 method2")

class C3(C2,C1):
    def method3(self):
        print("In C3 method3")

obj4=C3()
print(C3.mro())
print(C2.mro())
obj4.method1()
#obj4.method2()
obj4.method3()











