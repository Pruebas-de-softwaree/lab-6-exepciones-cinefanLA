import pytest
from Exceptions2 import ExceptionsDemo, MyException  

demo = ExceptionsDemo()

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

def test_divide_type_error():
    with pytest.raises(TypeError):
        demo.divide("10", 2)

