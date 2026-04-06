'''## Print max number by compare to both the methods

class Cls1:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    
class Cls2(Cls1):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d

    def add1(self):
        return self.c+self.d
    
obj=Cls2(10,20,50,6)
out=obj.add1()
out1=obj.add()

print(max(out,out1))
'''
##Public Attribute will be available across the class and we can access it outside the class also.
##Protected Attributes should not be accessed directly outside the class. Protected attributes will be initialized with prefix of "_" single underscore.
##Private Attributes can not access outside the class. These are accessible within the parent class only. It will be defined with prefix of "__" double underscore. It can be accessible with Name Mangling.
##Name Mangling:: The Private attribute can access with the class name is called Name Mangling. syntax::objectname._classname__attributename

class A:
    def __init__(self,a,b,c):
        self.a=a#public attribute
        self._b=b#protected attribute
        self.__c=c#private attribute
    def method1(self):
        print(self.a)
        print(self._b)
        print(self.__c)
class B(A):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
        pass
    def method2(self):
        print(self.a)
        print(self._b)
        #print(self.__c)#Its an error because it is a private attribute so we need to access it by its class name is called Name Mangling.
        print(self._A__c)

obj=B(1,2,3)
obj.method2()
obj.method1()
print(obj._b)
#print(obj.__c)
print(obj._A__c)#Name Mangling(syntax:objectname._classname__attributename)