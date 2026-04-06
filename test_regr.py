import pytest

@pytest.mark.regression
def test_01():
    print("Test1")

@pytest.mark.sanity
def test_02():
    print("Test2")

@pytest.mark.smoke
def test_03():
    print("test3")


