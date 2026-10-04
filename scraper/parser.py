"""Módulo encargado de extraer datos del HTML."""

from bs4 import BeautifulSoup

# Mapeo de clases CSS de rating a números
RATING_MAP = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,   
    "Five":5
}

def parse_books(html: str) -> list[dict]:
    
    """
    Extrae la lista de libros del HTML.

    Args:
        html: El HTML de una página de books.toscrape.com.

    Returns:
        Lista de diccionarios, uno por libro, con las claves:
        title, price, rating, availability.
    """
    soup =BeautifulSoup(html, "html.parser")
    books = []
    
    for article in soup.select("article.product_pod"):
         title = article.h3.a["title"]
         price = _clean_price(article.select_one("p.price_color").text)
         rating = _extract_rating(article.select_one("p.star-rating")["class"])
         availability = article.select_one("p.instock.availability").text.strip()
         
         
         books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })
    return books

def _clean_price(raw_price: str) -> float:
    """
    Convierte un precio en texto a float, ignorando símbolos de moneda.

    Funciona con '£51.77', 'Â£51.77', '$51.77', '€51,77', etc.
    """
    cleaned = "".join(c for c in raw_price if c.isdigit() or c == ".")
    return float(cleaned)


def _extract_rating(class_list: list[str]) -> int:
    """Extrae el número de rating desde las clases CSS del elemento."""
    for cls in class_list:
        if cls in RATING_MAP:
            return RATING_MAP[cls]
    return 0