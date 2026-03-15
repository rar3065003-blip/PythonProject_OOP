from unittest.mock import patch

from _pytest.capture import CaptureFixture

from src.product import Product


def test_product_init(product_characters: Product) -> None:
    assert product_characters.name == "Samsung Galaxy S23 Ultra"
    assert product_characters.description == "256GB, Серый цвет, 200MP камера"
    assert product_characters.price == 180000.0
    assert product_characters.quantity == 5


def test_price_setter_valid_value() -> None:
    """Тест: установка корректной цены"""
    product = Product(name="Test", description="", price=100.0, quantity=1)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_zero_value(capsys: CaptureFixture) -> None:
    """Тест: установка нулевой цены"""
    product = Product(name="Test", description="", price=100.0, quantity=1)
    original_price = product.price
    product.price = 0
    assert product.price == original_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной" in captured.out


def test_price_setter_negative_value(capsys: CaptureFixture) -> None:
    """Тест: установка отрицательной цены"""
    product = Product(name="Test", description="", price=100.0, quantity=1)
    original_price = product.price
    product.price = -50.0
    assert product.price == original_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной" in captured.out


def test_create_new_product() -> None:
    """Тест: создание нового продукта, когда его нет в списке"""
    product_list: list = []
    new_data = {"name": "New Phone", "description": "Новый смартфон", "price": 30000.0, "quantity": 5}

    result = Product.new_product(product_data=new_data, product_list=product_list)

    assert isinstance(result, Product)
    assert result.name == "New Phone"
    assert result.description == "Новый смартфон"
    assert result.price == 30000.0
    assert result.quantity == 5


def test_update_existing_product_higher_price() -> None:
    """Тест: обновление существующего продукта с более высокой ценой"""
    existing_product = Product(
        name="Samsung Galaxy S24", description="512GB, Чёрный цвет", price=250000.0, quantity=1  # текущая цена
    )
    product_list = [existing_product]

    update_data = {
        "name": "Samsung Galaxy S24",  # то же имя
        "description": "Обновлённое описание",
        "price": 300000.0,  # выше текущей цены
        "quantity": 3,
    }

    result = Product.new_product(product_data=update_data, product_list=product_list)

    assert result is existing_product
    assert result.price == 300000.0
    assert result.quantity == 4
    assert result.description != "Обновлённое описание"


def test___str__() -> None:
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Samsung Galaxy S24 Ultra", "250GB, Серый цвет, 210MP камера", 1800.0, 1)
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product_2) == "Samsung Galaxy S24 Ultra, 1800.0 руб. Остаток: 1 шт."


def test___add__() -> None:
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Samsung Galaxy S24 Ultra", "250GB, Серый цвет, 210MP камера", 1800.0, 1)
    result = product_1.price + product_2.price
    assert result == 181800.0


def test___add__zero() -> None:
    product_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
    product_2 = Product("Samsung Galaxy S24 Ultra", "250GB, Серый цвет, 210MP камера", 0.0, 1)
    result = product_1 + product_2
    assert result == 0.0


def test_check_change_price_yes() -> None:
    product = Product("Товар", "Описание", 100.0, 5)
    with patch("builtins.input") as mock_input:
        mock_input.return_value = "y"
        result = product.check_change_price(80.0)
        assert result == 80.0
        assert product.price == 80.0


def test_check_change_price_no() -> None:
    product = Product("Товар", "Описание", 100.0, 5)
    with patch("builtins.input") as mock_input:
        mock_input.return_value = "n"
        result = product.check_change_price(80.0)
        assert result == 100.0
        assert product.price == 100.0


def test_check_change_price_maybe() -> None:
    product = Product("Товар", "Описание", 100.0, 5)
    with patch("builtins.input") as mock_input:
        mock_input.return_value = "maybe"
        result = product.check_change_price(80.0)
        assert result is None
        assert product.price == 100.0
