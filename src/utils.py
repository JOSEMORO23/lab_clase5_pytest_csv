# src/utils.py
from __future__ import annotations

def normalize_name(s: str) -> str:
    """
    Recibe un nombre y devuelve:
    - espacios colapsados
    - sin espacios al inicio/fin
    - primera letra de cada palabra en mayúscula
    """
    if not isinstance(s, str):
        raise TypeError("s debe ser str")
    base = " ".join(s.strip().split())
    return base.title()

def safe_divide(a: float, b: float) -> float:
    """
    Divide a/b. Lanza ZeroDivisionError si b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

def clamp(n: float, lo: float, hi: float) -> float:
    """
    Limita n al rango [lo, hi]. Requiere lo <= hi.
    """
    if lo > hi:
        raise ValueError("lo debe ser <= hi")
    return max(lo, min(n, hi))
