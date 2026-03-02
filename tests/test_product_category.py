from src.product import Product


def test_product_init(product_characters):
    assert product_characters.name == "Samsung Galaxy S23 Ultra"
