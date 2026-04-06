##Assert

import pytest
import sys
'''
cluster = 3

def test_01():
    assert cluster > 2

def test_02():
    assert 10 + 10 == 20

def test_03():
    if cluster > 2:
        assert True

'''
##Markers:: Markers are used for controlling the flow of execution of pytest testcases.

@pytest.mark.order(3)
def test_04():
    print("Test1")

@pytest.mark.order(1)
def test_05():
    print("Test2")

@pytest.mark.order(2)
def test_06():
    print("Test3")


@pytest.mark.skip(reason = 'BUG 001 , In open state')
def test_07():
    print("Test10")
@pytest.mark.skipif(sys.platform == "win32" , reason = 'Unsupported platform')
def test_08():
    print("Test11")

def test_09():
    print("Test 12")