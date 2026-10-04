# 📚 Books Scraper

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen.svg)](#-testing)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://peps.python.org/pep-0008/)

A Python web scraper that extracts book data (title, price, rating, availability) from [books.toscrape.com](https://books.toscrape.com/) and saves it to a CSV file.

Built with a clean, modular architecture that separates fetching, parsing, and storage — making the code easy to test, extend, and maintain.

---

## ✨ Features

- **Multi-page scraping** — automatically navigates through the catalog pages
- **Clean architecture** — fetcher, parser, and storage are fully separated
- **Robust error handling** — a failing page doesn't stop the whole scraper
- **Encoding-safe** — handles currency symbols regardless of file encoding
- **Fully tested** — unit tests for all parsing logic with `pytest`
- **Configurable** — number of pages, output path, and headers in one place

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.13** | Core language |
| **Requests** | HTTP client for downloading HTML |
| **BeautifulSoup4** | HTML parsing and data extraction |
| **pytest** | Unit testing framework |
| **CSV (stdlib)** | Data storage format |

---

## 📁 Project Structure

```
books-scraper/
├── scraper/
│   ├── __init__.py
│   ├── config.py          # Configuration (URLs, headers, paths)
│   ├── fetcher.py         # Downloads HTML from URLs
│   ├── parser.py          # Extracts structured data from HTML
│   ├── storage.py         # Saves data to CSV
│   └── main.py            # Orchestrator: fetch → parse → save
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Shared pytest fixtures
│   └── test_parser.py     # Unit tests for the parser
├── data/
│   └── .gitkeep           # Output directory for the CSV
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

### Architecture Overview

The project follows a **layered architecture** where each module has a single responsibility:

```
┌─────────────────┐
│   main.py       │  Orchestrates the flow
└────────┬────────┘
         │
    ┌────┴─────┬──────────┬──────────┐
    ▼          ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│fetcher │ │parser  │ │storage │ │config  │
│  ↓     │ │  ↓     │ │  ↓     │ │        │
│ HTTP   │ │ HTML   │ │  CSV   │ │Settings│
└────────┘ └────────┘ └────────┘ └────────┘
```

- **`fetcher.py`** — knows how to download HTML. Nothing else.
- **`parser.py`** — knows how to extract data from HTML. Nothing else.
- **`storage.py`** — knows how to save data. Nothing else.
- **`main.py`** — coordinates everything.

This separation means: if you want to save to a database instead of CSV, you only change `storage.py`. If the site changes its HTML, you only change `parser.py`.

---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- pip

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/XimenaBarrera1/books-scraper.git
   cd books-scraper
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - **Windows:**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Run the scraper from the project root:

```bash
python -m scraper.main
```

### Example output

```
Iniciando scraper (maximo 3 páginas) ...

Scrapeando página 1/3: https://books.toscrape.com/catalogue/page-1.html
 -> 20 libros extraidos
Scrapeando página 2/3: https://books.toscrape.com/catalogue/page-2.html
 -> 20 libros extraidos
Scrapeando página 3/3: https://books.toscrape.com/catalogue/page-3.html
 -> 20 libros extraidos

✓ Total: 60 libros guardados en .../data/books.csv
```

The result is saved to `data/books.csv`:

```csv
title,price,rating,availability
A Light in the Attic,51.77,3,In stock
Tipping the Velvet,53.74,1,In stock
Soumission,50.1,1,In stock
Sharp Objects,47.82,4,In stock
```

### Configuration

All settings live in `scraper/config.py`:

```python
BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = "https://books.toscrape.com/catalogue/page-{page}.html"
MAX_PAGES = 3               # ← change this to scrape more pages
OUTPUT_FILE = DATA_DIR / "books.csv"
HEADERS = {...}             # User-Agent to avoid being blocked
```

To scrape more pages, just change `MAX_PAGES`. To target a different site, update the URLs.

---

## 🧪 Testing

The project uses `pytest` for unit tests. Run them with:

```bash
pytest -v
```

Expected output:

```
tests/test_parser.py::test_parse_books_returns_list PASSED   [ 14%]
tests/test_parser.py::test_parse_books_count PASSED          [ 28%]
tests/test_parser.py::test_parse_books_structure PASSED      [ 42%]
tests/test_parser.py::test_parse_books_values PASSED         [ 57%]
tests/test_parser.py::test_parse_books_empty_html PASSED     [ 71%]
tests/test_parser.py::test_clean_price PASSED                [ 85%]
tests/test_parser.py::test_extract_rating PASSED             [100%]

======================= 7 passed in 0.14s =======================
```

### What is tested?

| Test | What it verifies |
|------|------------------|
| `test_parse_books_returns_list` | The parser returns a list |
| `test_parse_books_count` | It extracts the correct number of books |
| `test_parse_books_structure` | Each book has the expected keys |
| `test_parse_books_values` | Extracted values are correct |
| `test_parse_books_empty_html` | It handles empty HTML gracefully |
| `test_clean_price` | Price parsing handles encoding variations |
| `test_extract_rating` | CSS classes map to correct numbers |

The tests use **fixtures with local HTML** instead of hitting the real website, making them fast, deterministic, and independent of network access.

---

## 🧠 Design Decisions

### Why `BeautifulSoup` with `html.parser`?

`html.parser` is built into Python's standard library — no extra dependencies. For a project of this size it's more than fast enough. For larger-scale scraping, `lxml` would be a better choice.

### Why CSV over a database?

CSV is:
- **Portable** — opens in Excel, Google Sheets, or any text editor
- **Human-readable** — easy to inspect and debug
- **Zero-dependency** — no database server to install

For a portfolio project focused on scraping, CSV is the right choice.

### Why isolate errors per page?

In `main.py`, each page fetch is wrapped in a `try/except`:

```python
try:
    html = fetch_page(url)
    books = parse_books(html)
except Exception as e:
    print(f"Error en página {page}: {e}")
    continue
```

If page 5 fails, pages 1–4 and 6–N still succeed. This makes the scraper **resilient** to transient network errors or temporary server issues.

---

## 📌 Limitations

- **No pagination detection** — it stops at `MAX_PAGES`, not at the real last page
- **No retry logic** — a failed request is skipped, not retried
- **Single site** — the parser is tailored to books.toscrape.com's HTML structure

These are intentional trade-offs for a learning-focused project. See the [Roadmap](#-roadmap) for potential improvements.

---

## 🗺️ Roadmap

- [ ] Add retry logic with exponential backoff (using `tenacity`)
- [ ] Add pagination auto-detection (stop when there are no more pages)
- [ ] Add a `--pages N` CLI argument with `argparse`
- [ ] Support exporting to JSON and SQLite
- [ ] Add logging with the `logging` module
- [ ] Add a GitHub Actions CI workflow

---

## 👤 Author

**Ximena Barrera**

- GitHub: [@XimenaBarrera1](https://github.com/XimenaBarrera1)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [books.toscrape.com](https://books.toscrape.com/) — a sandbox site created specifically for learning web scraping
- [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests documentation](https://requests.readthedocs.io/)