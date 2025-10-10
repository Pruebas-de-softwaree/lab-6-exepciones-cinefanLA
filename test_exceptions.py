import pytest
from Exceptions2 import ExceptionsDemo, MyException  

demo = ExceptionsDemo()

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        demo.divide(10, 0)

def test_divide_type_error():
    with pytest.raises(TypeError):
        demo.divide("10", 2)

def test_access_list_index_error():
    with pytest.raises(IndexError):
        demo.access_list([1, 2, 3], 5)

def test_access_list_type_error():
    with pytest.raises(TypeError):
        demo.access_list(1, 0)

def test_access_dict_key_error():
    with pytest.raises(KeyError):
        demo.access_dict({"a": 1, "b": 2}, "z")

def test_access_dict_type_error():
    with pytest.raises(TypeError):
        demo.access_dict("not_a_dict", "b")

def test_read_file_not_found():
    with pytest.raises(FileNotFoundError):
        demo.read_file("archivo_que_no_existe.txt")

def test_access_attribute_error():
    with pytest.raises(AttributeError):
        demo.access_attribute(object())