"""Módulo encargado de descargar el HTML de las páginas."""

import requests

from scraper.config import HEADERS

def fetch_page(url: str) -> str:
    """
    Descarga el HTML de una URL.

    Args:
        url: La dirección de la página web.

    Returns:
        El HTML de la página como string.

    Raises:
        requests.HTTPError: Si la respuesta no es exitosa (4xx, 5xx).
        requests.RequestException: Si hay un error de red.
    """
    response = requests.get(url, headers= HEADERS, timeout=10)
    response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
    return response.text