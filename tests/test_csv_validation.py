# tests/test_csv_validation.py
import csv
from pathlib import Path
import pytest

CSV_PATH = Path("data/products.csv")

def leer_filtrado():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows, reader.fieldnames

def test_archivo_existe():
    assert CSV_PATH.exists(), "El CSV no existe en data/products.csv"

def test_columnas_obligatorias_presentes():
    rows, headers = leer_filtrado()
    requeridas = {"id", "name", "category", "price", "stock"}
    assert set(headers) >= requeridas

def test_tipos_basicos_y_no_negativos():
    rows, _ = leer_filtrado()
    for r in rows:
        # tipos
        _id = int(r["id"])
        price = float(r["price"])
        stock = int(r["stock"])
        # reglas
        assert _id >= 1
        assert price >= 0.0
        assert stock >= 0

def test_ids_unicos():
    rows, _ = leer_filtrado()
    ids = [int(r["id"]) for r in rows]
    assert len(ids) == len(set(ids)), "IDs duplicados"

def test_precios_mayores_a_cero_para_items_con_stock():
    rows, _ = leer_filtrado()
    # Si hay stock > 0, esperamos price > 0.0
    for r in rows:
        stock = int(r["stock"])
        price = float(r["price"])
        if stock > 0:
            assert price > 0.0, f"Producto con stock>0 y price no positivo: {r}"