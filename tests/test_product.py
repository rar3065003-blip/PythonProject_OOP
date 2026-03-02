from src.product import Product


def test_product_init(product_characters: Product) -> None:
    assert product_characters.name == "Samsung Galaxy S23 Ultra"
    assert product_characters.description == "256GB, Серый цвет, 200MP камера"
    assert product_characters.price == 180000.0
    assert product_characters.quantity == 5
