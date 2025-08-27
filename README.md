# lab_clase5_pytest_csv
#  Laboratorio 5 — Pytest + Módulo simple y validación de CSV (Python 3.12)

##  Objetivos
- Practicar pruebas unitarias con **pytest** sobre un módulo sencillo.  
- Leer y validar un **dataset CSV** usando la librería estándar `csv`.  
- Cubrir casos normales, casos límite y manejo de errores.  

## Parte A — Módulo simple probado con pytest

**Archivo:** `src/utils.py`  
Funciones implementadas:  
- `normalize_name(s: str) -> str`  
  - Limpia espacios, normaliza mayúsculas/minúsculas.  
- `safe_divide(a: float, b: float) -> float`  
  - División segura, lanza `ZeroDivisionError` si `b==0`.  
- `clamp(n: float, lo: float, hi: float) -> float`  
  - Restringe un valor dentro del rango `[lo, hi]`.  

**Pruebas:** `tests/test_utils.py`  
- Casos normales.  
- Casos límite (cadenas vacías, ceros, fuera de rango).  
- Errores esperados (`TypeError`, `ZeroDivisionError`, `ValueError`).  

---

## Parte B — Validación de CSV con pytest

**Dataset:** `data/products.csv` 


Cómo ejecutar las pruebas

Activar entorno virtual (si corresponde):

source .venv/bin/activate


Ejecutar todas las pruebas:

pytest -q


Ejecutar un archivo específico:

pytest -q tests/test_utils.py
pytest -q tests/test_csv_validation.py


Ejecutar una prueba específica:

pytest -q -k "test_safe_divide_zero"


(Opcional) Reporte de cobertura:

pip install pytest-cov
pytest --cov=src --cov-report=term-missing
