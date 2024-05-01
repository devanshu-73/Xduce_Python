import pytest,sys
sys.path.append('..')
from data.functions import add,sub,mul,div

def test_add():
    res = add(10,5)
    assert res == 15

def test_sub():
    res = sub(10,5)
    assert res == 5

def test_mul():
    res = mul(10,5)
    assert res == 50

def test_div():
    res = div(10,5)
    assert res == 2
