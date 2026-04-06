####PYTEST####

#Pytest is a python framework for creating and executing test cases. We need to install and import pytest in our test cases.

#Fixture:: It is a special function in pytest and it is used for setup and cleanup activities. We need to decorate normal function with decorator function called @pytest.fixture to make it as a pytest fixture.

import pytest

@pytest.fixture

def fixture1():
    print("setup code")
    yield
    print("Clean up code")

def test_sample1(fixture1):
    print("In sample1 test case")#go to filepath folder and do 'pytest test_sample1.py' and the output is 100% 1 passed(in green color)



