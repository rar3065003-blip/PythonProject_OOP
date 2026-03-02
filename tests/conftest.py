import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_characters() -> Product:
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture()
def category_characters_1() -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        products=[],
    )


@pytest.fixture()
def category_characters_2() -> Category:
    return Category(
        name="Смартфоны не обычные",
        description="Смартфоны не обычные, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        products=[],
    )


@pytest.fixture()
def category_characters_3() -> Category:
    return Category(
        name="Смартфоны обычные",
        description="Смартфоны обычные, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        products=[],
    )
