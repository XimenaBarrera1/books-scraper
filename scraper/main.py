"""Punto de entrada del scraper. Orquesta fetcher, parser y storage."""

from scraper.config import CATALOGUE_URL, MAX_PAGES, OUTPUT_FILE
from scraper.fetcher import fetch_page
from scraper.parser import parse_books
from scraper.storage import save_books

def scrape_all_pages(max_pages: int = MAX_PAGES) -> list[dict]:
    """
    Recorre varias páginas del catálogo y devuelve todos los libros.

    Args:
        max_pages: Número máximo de páginas a recorrer.

    Returns:
        Lista con todos los libros de todas las páginas.
    """
    
    all_books = []
    
    for page in range(1, max_pages + 1):
        url = CATALOGUE_URL.format(page=page)
        print(f"Scrapeando página {page}/{max_pages}: {url}")
        
        try:
            html = fetch_page(url)
            books = parse_books(html)
            all_books.extend(books)
            print(f" -> {len(books)} libros extraídos")
        except Exception as e:
            print(f" X Error en la página {page}: {e}")
            continue  # Continúa con la siguiente página incluso si hay un error
        
    return all_books

def main() -> None:
     """Función principal: scrapea, guarda y muestra resumen."""
     
     print(f"Iniciando scraper (maximo {MAX_PAGES} páginas) ...\n ")
     
     
     books = scrape_all_pages()
     
     if not books:
        print("\nNo se encontraron libros. Abortando.")
        return
    
     saved = save_books(books)
     print(f"\n✓ Total: {saved} libros guardados en {OUTPUT_FILE}")
    
if __name__ == "__main__":
    main()
    
            
        

