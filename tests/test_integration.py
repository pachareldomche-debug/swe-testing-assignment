from quick_calc import *

def test_full_operation():
    result = add(5,3)
    assert result == 8

def test_clear():
    result = clear()
    assert result == 0
