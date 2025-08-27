# tests/test_utils.py
import math
import pytest
#from utils import normalize_name, safe_divide, clamp
from src.utils import normalize_name, safe_divide, clamp


def test_normalize_name_basico():
    assert normalize_name("  juan  perez ") == "Juan Perez"

@pytest.mark.parametrize("entrada,esperado", [
    ("ana", "Ana"),
    ("ANA  GARCIA", "Ana Garcia"),
    ("", ""),                 # cadena vacía -> vacía
])
def test_normalize_name_param(entrada, esperado):
    assert normalize_name(entrada) == esperado

def test_normalize_name_tipo_invalido():
    with pytest.raises(TypeError):
        normalize_name(None)  # type: ignore[arg-type]

def test_safe_divide_ok():
    assert math.isclose(safe_divide(10, 4), 2.5)

def test_safe_divide_zero():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)

@pytest.mark.parametrize("n,lo,hi,esperado", [
    (5, 0, 10, 5),
    (-1, 0, 10, 0),
    (20, 0, 10, 10),
])
def test_clamp(n, lo, hi, esperado):
    assert clamp(n, lo, hi) == esperado

def test_clamp_rango_invalido():
    with pytest.raises(ValueError):
        clamp(1, 5, 2)
