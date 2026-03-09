import pytest
from src.product import Product



def test_product_init(product_characters: Product) -> None:
    assert product_characters.name == "Samsung Galaxy S23 Ultra"
    assert product_characters.description == "256GB, Серый цвет, 200MP камера"
    assert product_characters.price == 180000.0
    assert product_characters.quantity == 5


def test_price_setter_valid_value():
    """Тест: установка корректной цены"""
    product = Product(name="Test", description="", price=100.0, quantity=1)
    product.price = 200.0
    assert product.price == 200.0


def test_price_setter_zero_value(capsys):
    """Тест: установка нулевой цены"""
    product = Product(name="Test", description="", price=100.0, quantity=1)
    original_price = product.price
    product.price = 0
    assert product.price == original_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной" in captured.out


def test_price_setter_negative_value(capsys):
    """Тест: установка отрицательной цены"""
    product = Product(name="Test", description="", price=100.0, quantity=1)
    original_price = product.price
    product.price = -50.0
    assert product.price == original_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной" in captured.out

def test_create_new_product():
    """Тест: создание нового продукта, когда его нет в списке"""
    product_list = []
    new_data = {
        'name': 'New Phone',
        'description': 'Новый смартфон',
        'price': 30000.0,
        'quantity': 5
    }

    result = Product.new_product(product_data=new_data,
                                 product_list=product_list)


    assert isinstance(result, Product)
    assert result.name == 'New Phone'
    assert result.description == 'Новый смартфон'
    assert result.price == 30000.0
    assert result.quantity == 5

def test_update_existing_product_higher_price():
    """Тест: обновление существующего продукта с более высокой ценой"""
    existing_product = Product(
        name='Samsung Galaxy S24',
        description='512GB, Чёрный цвет',
        price=250000.0,  # текущая цена
        quantity=1
    )
    product_list = [existing_product]

    update_data = {
        'name': 'Samsung Galaxy S24',  # то же имя
        'description': 'Обновлённое описание',
        'price': 300000.0,  # выше текущей цены
        'quantity': 3
    }

    result = Product.new_product(product_data=update_data, product_list=product_list)

    assert result is existing_product
    assert result.price == 300000.0
    assert result.quantity == 4
    assert result.description != 'Обновлённое описание'

