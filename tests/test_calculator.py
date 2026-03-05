from quick_calc import *

def test_add():
    assert add(5,3) == 8

def test_subtract():
    assert subtract(10,4) == 6

def test_multiply():
    assert multiply(6,7) == 42

def test_divide():
    assert divide(8,2) == 4

def test_divide_by_zero():
    assert divide(5,0) == "Error"

def test_negative_numbers():
    assert add(-5,3) == -2

def test_decimal_numbers():
    assert divide(5,2) == 2.5

def test_large_numbers():
    assert multiply(1000000,2) == 2000000
