##Encapsulation::It is a process of making the attributes in private and restricting the direct access to atributes.
# And it is a process of binding data(attributes,methods) into a single class. We can access the attributes 
# by using setter and getter methods.

'''
class Cls1:
    def __init__(self,a,b,c):#(self,a,b)
        self.a=a
        self._b=b
        self.__c=0
        print(self.__c)

    def sette(self,c):#Here again we assign the c value with setter method by passing new value
        self.__c = c
        print(self.__c)

    def gette(self):
        return self.__c
    
    
obj1=Cls1(10,20,30)    
#obj1=Cls1(10,20)
obj1.sette(100)
print(obj1.gette())

##Instance Method::We can access both class level attributes and instance attributes, It is having all the advantages of OOPS

class A:
    a=10
    def __init__(self,arg1):
        self.arg1=arg1
    def method2(self):
        print("Method2")
        print(A.a)
    def method1(self):
        self.method2()#Instance method access all the variables
        return self.arg1
    
obj=A(200)
print(obj.method1())

##Class method:: Class methods are created to access/modify only class level attributes.
#First argument of class method should be 'classname'. We need to decorate with @classmethod decorator.
# We cannot access instance attributes with classname.

class Class_A:
    x=20
    def __init__(self,arg1):
        self.arg1=arg1
    @classmethod
    def method3(cls):
        Class_A.x=200
        #return self.arg1
        
obj3=Class_A(10000)
print(obj3.method3())
print(obj3.x)
print(Class_A.x)


##Static method:: We are not going to access/modify the class/instance attributes/methods. We can make the method as static method.
#Static methods are independent of class and it doesn't required any arguments. We need to decorate with @staticmethod.
#Used as a standalone functions within the class and used to implement helper functions.
class B:
    def __init__(self,arg1):
        self.arg1=arg1
    
    def instance_method(self):
        return self.arg1
    @staticmethod
    def static_method():
        print("Stand alone method")

obj4=B(300)
print(obj4.instance_method())
obj4.static_method()


class Cls3:
    def method3(*args):
        print(args)

obj5=Cls3()
obj5.method3(10)
obj5.method3("a",300)
obj5.method3(40,50,60)

'''

from abc import ABC,abstractmethod

class Cls4(ABC):
    def show_details(self):
        pass
    @abstractmethod
    def functionality(self):
        pass

class Cls5(Cls4):
    def functionality(self):
        print("Functionality of Cls5")

obj5=Cls5()
obj5.functionality()

