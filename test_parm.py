##Parametrize:: To test our test cases with multiple inputs
import pytest
@pytest.mark.parametrize("input,expected",[(1,2),(2,4),(3,10),(4,8)])

def test_double(input , expected):
    assert input * 2 == expected