from src.category import Category
from src.product import Product

"""Тестирование категорий свойств продуктов"""


def test_category_init(
    category_characters_1: Category, category_characters_2: Category, category_characters_3: Category
) -> None:
    assert category_characters_1.name == "Смартфоны"
    assert category_characters_1.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни"
    )
    assert category_characters_1.products == ""
    assert Category.category_count == 3
    assert Category.product_count == 0


def test_add_product() -> None:
    category = Category("Смартфон", "Смартфон", [])
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 190000.0, 1)
    init_product_count = Category.product_count

    category.add_product(product)

    assert Category.product_count == 1
    assert Category.product_count == init_product_count + 1


def test_products() -> None:
    Category.product_count = 0
    category = Category(name="Na_kolenke_sobrano", description=" ", products=[])

    product = Product(name="Na_kolenke_sobrano", description=" ", price=250.0, quantity=5)

    category.add_product(product)
    updated_count = category.product_count
    result = category.products
    assert updated_count == 1
    assert result == "Na_kolenke_sobrano, 250.0 руб. Остаток: 5 шт.\n"


def test___str__(category_characters_1: Category) -> None:

    assert str(category_characters_1) == "Смартфоны, количество продуктов: 0 шт."


def test_middle_price_all_product(product_wo_quantity: Category, category_middle_amount: Category) -> None:
    assert product_wo_quantity.middle_price_all_product() == 0
    assert category_middle_amount.middle_price_all_product() == 110600.0
