import pytest
import data.functions as functions

def test_add():
    res = functions.add(10,5)
    assert res == 15

def test_sub():
    res = functions.sub(10,5)
    assert res == 5

# if __name__ == '__main__':
