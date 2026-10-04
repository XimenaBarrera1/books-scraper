"""Configuración centralizada del scraper."""

from pathlib import Path

# URL del sitio objetivo
BASE_URL = "https://books.toscrape.com/"

# Plantilla de URL para cada página del catálogo
# {page} se reemplaza por el número de página
CATALOGUE_URL = "https://books.toscrape.com/catalogue/page-{page}.html"

# Número máximo de páginas a scrapear
MAX_PAGES = 3

# Ruta donde se guardará el CSV
DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_FILE = DATA_DIR / "books.csv"

# Headers para simular un navegador real
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}