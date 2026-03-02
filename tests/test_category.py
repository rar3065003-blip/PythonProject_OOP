from src.category import Category


def test_category_init(
    category_characters_1: Category, category_characters_2: Category, category_characters_3: Category
) -> None:
    assert category_characters_1.name == "Смартфоны"
    assert category_characters_1.description == (
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни"
    )
    assert category_characters_1.products == []

    assert Category.category_count == 3
    assert Category.product_count == 0
