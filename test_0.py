import pytest

def suma(a, b):
    return a + b

def test_suma_positivos():
    assert suma(2, 4) == 6

def test_suma_negativos():
    assert suma(-1, -1) == -2

def division(a, b):
    return a / b

def test_division_por_cero():
    with pytest.raises(TypeError):
        division('5', 0)
