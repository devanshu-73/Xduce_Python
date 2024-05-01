import pytest
import time
import rectangle as r


@pytest.fixture
def rec():
    return r.Rectangle(30,40)

def test_area(rec):
    # result = r.Rectangle(30,40)

    assert rec.area() == 30*40

def test_perimeter(rec):
    # result=r.Rectangle(30,40) 

    assert rec.perimeter() == (30*2) + (40*2)

#if we find any function performing slow we can use @pytest.mark.slow to indicate it's a slow function 
@pytest.mark.slow
def test_slow(rec):
    time.sleep(5)
    assert rec.perimeter() == (30*2) + (40*2)

# if we have to skip any of the program we use @pytest.mark.skip
@pytest.mark.skip(reason='this Function is performing very slow and its taking too much time')
def test_slow(rec):
    time.sleep(5)
    assert rec.perimeter() == (30*2) + (40*2)

#if any of the function has not working so we can indicate it's as fail with help of @pytest.mark.xfail
@pytest.mark.xfail(reason="this function is not working ")
def test_peri():
    assert rec.perimeter != (20*2) + (40*2)

