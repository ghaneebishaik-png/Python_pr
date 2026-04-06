#class is blueprint of creating an object.
#Object is an instance of a class. Object is used to access class attributes and methods. We can create n number of objects by using single class.
#self is first argument of an instance method and it is mandatory. By using self we can accessing all properties of a class.
#Constructor: __init__: It is a special method is used to initialize all attributes. And first argument should be self.
#class variable defined inside the class and out side the method.
#instance variable defined inside the instance method.

class Cls1:
    class_variable = 1000
    def __init__(self,a,b,c):
        self.a=a#instance variable
        self.b=b
        self.c=c
    def method1(self):
        print(self.a)
        #print(Cls1.class_variable)#1000
        print(self.class_variable)#1000

obj1 = Cls1(10,20,30)
obj1.method1()
#print(Cls1.class_variable)#1000
print(obj1.b)
print(Cls1(1,2,3).c)

##Inheritence: Inheriting the properties of parent class in child class.
#Single level inheritence: Inheriting the properties of single parent class in child class

class Parent_class:

    def method1(self):
        print("Parent class method")

class Child_class(Parent_class):

    def method2(self):
        print("Child class method")

object = Child_class()
object.method1()#With child class object we can access both parent class and child class methods.
object.method2()

##Multilevel inheritence: Inheriting the properties of parent class in child class and child class properties in another child class.

class Pc1:

    def __init__(self,a):
        self.a=a

    def method1(self):
        print(self.a)

class Cc1(Pc1):

    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def method2(self):
        print(self.b)

class Cc2(Cc1):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
    def method3(self):
        print(self.c)

obj2 = Cc2(500,50,5)
obj2.method1()
obj2.method2()
obj2.method3()

##Multiple Inheritence is Inheriting multiple parent class properties in a child class.

class P1:

    def __init__(self,arg1):
        self.arg1 = arg1

    def meth1(self):
        return self.arg1
    
class P2:

    def __init__(self,arg2):
        self.arg2 = arg2

    def meth2(self):
        return self.arg2
    
class C1(P2,P1):

    def __init__(self,arg1,arg2,arg3):
        super().__init__(arg2)#super() is used for inheriting parent class properties in child class. We can use super() or class name to inherit the class constor in child class.
        P1.__init__(self,arg1)
        self.arg3 = arg3
    
    def meth3(self):
        return self.arg3
    
obj4 = C1(600,60,6)
print(obj4.meth3())

print(obj4.meth2())
print(obj4.meth1())
print(C1.mro())#How python look for methods in case of inheritence.


###Assignment: Create Multilevel inheritence

class A:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c = c
        self.d = d

    def add1(self):
        return self.c + self.d
    
obj5 = B(10,2,30,5)
#print(obj5.add())
print(max(obj5.add() , obj5.add1()))

##public attributes:: It will be available across the class and accessed/modified out side of the class also.

class Cls1:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def method1(self):
        print(self.a)#10

class Cls2(Cls1):
    def method2(self):
        print(self.b)#20

obj6 = Cls2(10,20,30)
obj6.method1()
obj6.method2()
print(obj6.c)#30

##Protected attributes:: It should not be accessed directly outside the class, protected attributes will be initialized with prifix '_'(underscore)

class Cls3:
    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.c = c
    def meth1(self):
        print(self._b)

class Cls4(Cls3):
    def meth2(self):
        print(self._b)

obj7 = Cls4(40,50,60)
obj7.meth1()
obj7.meth2()
print(obj7._b)

##Private attributes:: We cann't access private attributes outside the class. We can access it only in parent class only. We will define with '__' double underscore.
#If we want to access private attributes outside the class by using name mangling(obj._Cls1__attribute)

class Cls5:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.__c = c

    def meth1(self):
        print(self.__c)#90

class Cls6(Cls5):
    def meth2(self):
        #print(self.__c)#Out of the parent class it won't be accessed
        pass

obj8 = Cls6(70,80,90)
obj8.meth1()
obj8.meth2()
#print(obj8.__c)#Out of the class it cann't be accessed. By accessing this we use name mangling.

print(obj8._Cls5__c)#90


##Encapsulation:: It is a process of making atrributes in private and restricting the direct access to the attributes. It is a process of binding data in a single class.
#We can access the data by using setter and getter methods.

class Cls1:

    def __init__(self,a,b):
        self.a = a
        self._b = b

    def setter(self,c):#setter and getter are normal functions we can give other names as well
        self.__c = c

    def getter(self):
        return self.__c
    
obj = Cls1(10,20)
print(obj.setter(30))
print(obj.getter())#30


##Polimorphism: It is nothing but many forms. It allows same method names but behaves differently based on input.
#1.By using inbuilt functions 2.Method overload 3. Method override
#Method overload:: Python doesn't support method overloading. We can overload the method by using variable length positional arguments.

class Cls1:
    def meth1(*args):
        print(args)

obj = Cls1()
obj.meth1(100)
obj.meth1(100,200,300)
obj.meth1("a","b")

##Method override::In parent class and child class having same method names if we impliment inheritence, the method in the parent class will be overrride in the child class.

class Par_cls:
    def meth1(self):
        print("Parent class")

class Child(Par_cls):
    def meth1(self):
        print("Child class")

obj = Child()
obj.meth1()

##Abstract method:: Hiding internal details of class and showing required features only.

from abc import ABC, abstractmethod

class Cls1(ABC):
    @abstractmethod
    def method1(self):
        pass

class Cls2(Cls1):
    def method1(self):
        print("method2")

obj1 = Cls2()
obj1.method1()
#obj1.method2()