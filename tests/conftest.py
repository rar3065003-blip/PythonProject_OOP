import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture()
def lawngrass_1() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def lawngrass_2() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture()
def smartphone_1() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture()
def smartphone_2() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
