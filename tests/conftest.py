import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_characters():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture()
def category1_characters():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[],
        category_count=0,
        product_count=0,
    )
