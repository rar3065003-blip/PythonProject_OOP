from src.product import Product
from src.category import Category
import pytest


def test_print_mixin_product(capsys: pytest.CaptureFixture) -> None:
    Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, " "5)"
    )


def test_print_mixin_category(capsys: pytest.CaptureFixture) -> None:
    Category(
        name="Смартфоны не обычные",
        description="Смартфоны не обычные, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        products=[],
    )
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Category(Смартфоны не обычные, "
        "Смартфоны не обычные, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни)"
    )
