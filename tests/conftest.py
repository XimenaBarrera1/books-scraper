"""Fixtures compartidos para los tests."""

import pytest


@pytest.fixture
def sample_html() -> str:
    """HTML mínimo con 2 libros, simulando la estructura real del sitio."""
    return """
    <html>
        <body>
            <article class="product_pod">
                <h3><a title="Book One" href="#">Book One</a></h3>
                <p class="star-rating Five"></p>
                <div class="product_price">
                    <p class="price_color">£10.99</p>
                    <p class="instock availability">In stock</p>
                </div>
            </article>
            <article class="product_pod">
                <h3><a title="Book Two" href="#">Book Two</a></h3>
                <p class="star-rating Three"></p>
                <div class="product_price">
                    <p class="price_color">£25.50</p>
                    <p class="instock availability">In stock</p>
                </div>
            </article>
        </body>
    </html>
    """