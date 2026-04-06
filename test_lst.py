import pytest

lst = []

@pytest.fixture
def fixture1():
    #setup is fixture1
    print("Adding elements to list")
    lst.extend([1,2,3,4,5,6])
    print(lst)#after this line go to test_lst_len block

    #cleanup execute after every function 
    yield
    lst.clear()
    print(lst)
    print("Removed all elements in the list")#After this line move to next function test_max_lst then move to fixture1 decorator

def test_lst_len(fixture1):#first execute this func then arg is decorator move to decorator block that is fixture1 and execute that block
    if len(lst) % 2 == 0:
        print("Even lst")#after this go to cleanup block
    else:
        print("Odd lst")

def test_max_lst(fixture1):
    print(max(lst))