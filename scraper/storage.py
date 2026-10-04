"""Módulo encargado de guardar los datos en un archivo CSV."""

import csv
from pathlib import Path

from scraper.config import OUTPUT_FILE

def save_books(books: list[dict], output_path: Path = OUTPUT_FILE) -> int:
    """
    Guarda la lista de libros en un archivo CSV.

    Args:
        books: Lista de diccionarios con los datos de cada libro.
        output_path: Ruta donde se guardará el CSV.

    Returns:
        La cantidad de libros guardados.
    """
    if not books:
        return 0

    # Asegura que la carpeta exista (si no, la crea)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["title", "price", "rating", "availability"]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

    return len(books)