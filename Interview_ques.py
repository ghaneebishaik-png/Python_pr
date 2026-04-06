###############TERRALOGY#######################

# Problem: Write a Python program that returns all possible permutations of a string.
# Example: Input: "abc"
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
 
str1 = "abc"
list1 =[]
for i in range(len(str1)):#a
    for j in range(len(str1)):#a
        for k in range(len(str1)):#b
            if i != j and j !=k and i !=k:
                list1.append((str1[i] + str1[j] + str1[k]))
print(list1)

#######################################

try:
    x = 0
    print(10/x)
except:
    print("error")
else:
    print("success")

finally:
    print("thank for coding")

################################################


"""Design a Banking System Using Abstraction:
    Create an abstract class Account with abstract methods deposit(), withdraw(), and get_balance().
    Create two subclasses: SavingsAccount and CheckingAccount. Implement the methods:

SavingsAccount should have an interest rate and should allow deposits/withdrawals but cannot drop below a minimum balance.
CheckingAccount should allow overdraft but charge a fee for overdraft.

    Write a function that displays the balance of each account after performing some transactions."""
    
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,balance):
        self.balance = balance
        
    @abstractmethod    
    def deposit(self,amount):
        pass
    
    @abstractmethod   
    def withdraw(self, amount):
        pass
    
    def get_balance(self):
        return self.balance
        
    #--------------------------------------
    
class SavingAccount(Account):
    
    def __init__(self,balance):
        self.min_balance = 500
        super().__init__(balance)
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if self.balance-amount >=self.min_balance:
            self.balance -=amount
        else:
            print("no balance")
        
class CheckingAccount(Account):
    def __init__(self,balance):
        self.fee = 50
        super().__init__(balance)
        
    def deposit(self,amount):
        self.balance +=amount
        
    def withdraw(self,amount):
        self.balance -=amount
        
        if self.balance <0:
            self.balance-=self.fee
            
s = SavingAccount(1000)
c = CheckingAccount(500)

s.withdraw(300)
c.withdraw(700)

print("savings account balance : ",s.balance)
print("check Balance : ",c.get_balance())
    

################################################################
# Sort a Dictionary by Value
# Given a dictionary, sort it by values in descending order using dictionary comprehension.
Input =  {"apple": 5, "banana": 2, "cherry": 7, "date": 3}
# Output: {'cherry': 7, 'apple': 5, 'date': 3, 'banana': 2}

result = {}

while Input:
    max_key = None
    max_value = -1#5
    
    for k in Input :
        if Input[k] > max_value:#5>-1
            max_value = Input[k]#5
            max_key = k
            
    result = { **result, **{max_key:max_value}}
    
    del Input[max_key]
    
print(result)

######################################
def prime_generator(n):
    for num in range(2,n+1):
        is_prime = True
        for i in range(2,int(num** 0.5)+1):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
n =20
for prime in prime_generator(n):
    print(prime)

#######################################################
def my_decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after the function")
    return wrapper

@my_decorator
def say_hello():
    print("hello")
say_hello()

############################################################

nums = [1,2,3,4]
def square(x):
    return x*x
result = map(square,nums)
print(list(result))

#################################
try:
    x = 10/0
except ZeroDivisionError:
    print("cant divide by zero")
    
#error
if True:
    print("hello")

######################################
import pytest

@pytest.mark.parametrize("a,b,expected",[(1,2,3),(2,3,5),(5,5,10)])
def test_add(a,b,expected):
    assert a+b == expected

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        