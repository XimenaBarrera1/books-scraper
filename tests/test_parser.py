"""Tests para el módulo parser."""

from scraper.parser import parse_books, _clean_price, _extract_rating


def test_parse_books_returns_list(sample_html):
    """Debe devolver una lista."""
    result = parse_books(sample_html)
    assert isinstance(result, list)


def test_parse_books_count(sample_html):
    """Debe extraer exactamente 2 libros del HTML de prueba."""
    result = parse_books(sample_html)
    assert len(result) == 2


def test_parse_books_structure(sample_html):
    """Cada libro debe tener las claves esperadas."""
    result = parse_books(sample_html)
    for book in result:
        assert set(book.keys()) == {"title", "price", "rating", "availability"}


def test_parse_books_values(sample_html):
    """Los valores del primer libro deben ser correctos."""
    result = parse_books(sample_html)
    first = result[0]
    assert first["title"] == "Book One"
    assert first["price"] == 10.99
    assert first["rating"] == 5
    assert first["availability"] == "In stock"


def test_parse_books_empty_html():
    """Con HTML vacío debe devolver una lista vacía, no fallar."""
    result = parse_books("<html></html>")
    assert result == []


def test_clean_price():
    """_clean_price debe limpiar símbolos de moneda."""
    assert _clean_price("£51.77") == 51.77
    assert _clean_price("51.77") == 51.77
    assert _clean_price("Â£51.77") == 51.77  # caso del bug que tuviste
    assert _clean_price("$25.50") == 25.50


def test_extract_rating():
    """_extract_rating debe mapear las clases CSS a números."""
    assert _extract_rating(["star-rating", "Five"]) == 5
    assert _extract_rating(["star-rating", "Three"]) == 3
    assert _extract_rating(["star-rating", "One"]) == 1
    assert _extract_rating(["star-rating"]) == 0  # caso sin número